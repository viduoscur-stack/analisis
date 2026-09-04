"""
ORA LAB — Estudio de tokenización para ORA LINK (fase experimental).

Script STANDALONE. No modifica ningún archivo existente del proyecto.
No ejecuta nada contra Ollama ni contra Gemma como generador — solo
tokeniza texto con el mismo tokenizer real ya cacheado
(google/gemma-4-E2B-it, vía tokenizer_lab.get_tokenizer()), igual que
el resto del proyecto. Es instantáneo: tokenizar no requiere generación.

Uso:
    .venv\\Scripts\\python.exe tokenizer_study.py

Salida:
    results/ora_link_tokenizer_study/tokenizer_study.json
"""

from __future__ import annotations

import itertools
import json
import random
import string
from pathlib import Path

from tokenizer_lab import get_tokenizer

OUT_DIR = Path("results") / "ora_link_tokenizer_study"
OUT_DIR.mkdir(parents=True, exist_ok=True)

tokenizer = get_tokenizer()


def tok_info(text: str) -> dict:
    """Tokeniza `text` con el tokenizer real y devuelve toda la evidencia
    necesaria: cantidad de tokens, IDs exactos, y (si el tokenizer lo
    soporta) la representación de cada token individual."""
    ids = tokenizer.encode(text, add_special_tokens=False)
    try:
        pieces = tokenizer.convert_ids_to_tokens(ids)
    except Exception as e:
        pieces = f"NOT_AVAILABLE ({e})"
    return {"text": text, "n_tokens": len(ids), "ids": ids, "pieces": pieces}


# ============================================================
# 1. ALFABETO DE SÍMBOLOS
# ============================================================
SYMBOLS = list(string.punctuation)
assert len(SYMBOLS) == 32, f"esperaba 32 símbolos ASCII imprimibles, hay {len(SYMBOLS)}: {SYMBOLS}"

alfabeto = [tok_info(s) for s in SYMBOLS]

# ============================================================
# 2. PARES DE SÍMBOLOS (producto cartesiano completo: 32x32=1024)
# ============================================================
pares = [tok_info(a + b) for a, b in itertools.product(SYMBOLS, repeat=2)]
pares_1tok = [p for p in pares if p["n_tokens"] == 1]
pares_2tok = [p for p in pares if p["n_tokens"] == 2]
pares_mas_de_2 = [p for p in pares if p["n_tokens"] > 2]

# ============================================================
# 3. TRIPLETAS (muestra controlada, no cartesiano completo de 32768)
# ============================================================
random.seed(42)
triplet_texts: set[str] = set()

# a) mismo símbolo x3 (32 casos) — ¿repetir un símbolo de 1 token lo mantiene en 1?
for s in SYMBOLS:
    triplet_texts.add(s * 3)

# b) extender los pares "conocidos de interés" (mencionados en el laboratorio
#    original: ^^, ~~, @@, ##, &*, |^) con cada símbolo, antes y después
PARES_CONOCIDOS = ["^^", "~~", "@@", "##", "&*", "|^"]
for base in PARES_CONOCIDOS:
    for s in SYMBOLS:
        triplet_texts.add(base + s)
        triplet_texts.add(s + base)

# c) muestra aleatoria del espacio completo de tripletas (32^3 = 32768),
#    para no sesgar el resultado solo hacia lo que ya sospechábamos
todas_las_triplas = list(itertools.product(SYMBOLS, repeat=3))
muestra_aleatoria = random.sample(todas_las_triplas, 1000)
for t in muestra_aleatoria:
    triplet_texts.add("".join(t))

tripletas = [tok_info(t) for t in sorted(triplet_texts)]

# ============================================================
# 4. TOKENS NATURALES VS SÍMBOLOS
# ============================================================
PALABRAS_FRECUENTES = [
    "de", "la", "el", "que", "y", "en", "para", "con", "es", "no",
    "una", "un", "por", "del", "los", "las",
]
ESTRUCTURAS_FRECUENTES = ["de ", "la ", "que ", " y ", " en ", " para "]
naturales = (
    [tok_info(w) for w in PALABRAS_FRECUENTES]
    + [tok_info(w) for w in ESTRUCTURAS_FRECUENTES]
)

# ============================================================
# 5. MARCADORES / ESTRUCTURAS ESPECIALES
# ============================================================
MARCADORES = [
    "<|channel|thought", "<|channel>thought", "<|message>", "<|end|>",
    "^^", "~~", "@@", "&&", "&*", "|^", "##",
]
marcadores = [tok_info(m) for m in MARCADORES]

# ============================================================
# 7. PROPIEDAD FUNDAMENTAL: sensibilidad al contexto
# (para cada símbolo de 1 token y cada par de 1 token, hasta un límite
#  razonable para no disparar el tiempo de corrida)
# ============================================================
simbolos_1tok = [a["text"] for a in alfabeto if a["n_tokens"] == 1]
candidatos_contexto = list(dict.fromkeys(simbolos_1tok + [p["text"] for p in pares_1tok]))[:80]

contexto_resultados = []
for c in candidatos_contexto:
    variantes = {
        "solo": c,
        "solo_x2": c * 2,
        "solo_x3": c * 3,
        "espacio_antes": " " + c,
        "espacio_despues": c + " ",
        "espacio_ambos": " " + c + " ",
        "pegado_antes_de_palabra": c + "hola",
        "pegado_despues_de_palabra": "hola" + c,
        "rodeando_palabra": c + "hola" + c,
    }
    if c != c.upper():
        variantes["mayusculas"] = c.upper()
    fila = {"candidato": c, "n_tokens_base": tok_info(c)["n_tokens"]}
    for nombre, texto in variantes.items():
        fila[nombre] = tok_info(texto)["n_tokens"]
    contexto_resultados.append(fila)

# ============================================================
# Guardar todo
# ============================================================
resultado = {
    "alfabeto": alfabeto,
    "pares_conteo": {
        "total": len(pares),
        "1tok": len(pares_1tok),
        "2tok": len(pares_2tok),
        "mas_de_2": len(pares_mas_de_2),
        "pct_1tok": round(100 * len(pares_1tok) / len(pares), 2),
        "pct_2tok": round(100 * len(pares_2tok) / len(pares), 2),
        "pct_mas_de_2": round(100 * len(pares_mas_de_2) / len(pares), 2),
    },
    "pares_1tok": pares_1tok,
    "pares_2tok": pares_2tok,
    "pares_mas_de_2": pares_mas_de_2,
    "tripletas": tripletas,
    "naturales": naturales,
    "marcadores": marcadores,
    "contexto": contexto_resultados,
}

out_path = OUT_DIR / "tokenizer_study.json"
out_path.write_text(json.dumps(resultado, indent=2, ensure_ascii=False), encoding="utf-8")

print(f"Alfabeto: {len(alfabeto)} símbolos medidos")
print(
    f"Pares: {len(pares)} totales -> "
    f"{len(pares_1tok)} de 1 token ({resultado['pares_conteo']['pct_1tok']}%), "
    f"{len(pares_2tok)} de 2 tokens ({resultado['pares_conteo']['pct_2tok']}%), "
    f"{len(pares_mas_de_2)} de más de 2 ({resultado['pares_conteo']['pct_mas_de_2']}%)"
)
print(f"Tripletas muestreadas: {len(tripletas)}")
print(f"Candidatos de contexto probados: {len(contexto_resultados)}")
print(f"\nGuardado completo en: {out_path.resolve()}")

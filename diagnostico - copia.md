{
  "timestamp_utc": "2026-09-06T05:05:33.727018+00:00",
  "modelo": "gemma4:e2b",
  "duracion_generacion_seg": 55.86,
  "n_muestras": 98,
  "baseline_nvidia_smi": {
    "vram_used_mb": 5685,
    "vram_total_mb": 6144,
    "gpu_util_pct": 10
  },
  "baseline_sistema": {
    "cpu_pct": 33.3,
    "ram_used_mb": 17773,
    "ram_total_mb": 24511
  },
  "ollama_ps_antes_de_generar": "NAME              ID              SIZE      PROCESSOR          CONTEXT    UNTIL   \nqwen3.5:latest    6488c96fa5fa    6.1 GB    43%/57% CPU/GPU    4096       Forever",
  "ollama_ps_despues_de_generar": "NAME          ID              SIZE      PROCESSOR    CONTEXT    UNTIL   \ngemma4:e2b    7fbdbf8f5e45    1.7 GB    100% GPU     4096       Forever",
  "ollama_show_verbose": "Model\n    architecture        gemma4    \n    parameters          5.1B      \n    context length      131072    \n    embedding length    1536      \n    quantization        Q4_K_M    \n    requires            0.20.0    \n\n  Capabilities\n    completion    \n    vision        \n    audio         \n    tools         \n    thinking      \n\n  Parameters\n    temperature    1       \n    top_k          64      \n    top_p          0.95    \n\n  Metadata\n    gemma4.attention.head_count                   8                          \n    gemma4.attention.head_count_kv                1                          \n    gemma4.attention.key_length                   512                        \n    gemma4.attention.key_length_swa               256                        \n    gemma4.attention.layer_norm_rms_epsilon       1e-06                      \n    gemma4.attention.shared_kv_layers             20                         \n    gemma4.attention.sliding_window               512                        \n    gemma4.attention.sliding_window_pattern       [true ...+34 more]         \n    gemma4.attention.value_length                 512                        \n    gemma4.attention.value_length_swa             256                        \n    gemma4.audio.attention.head_count             8                          \n    gemma4.audio.attention.layer_norm_epsilon     1e-06                      \n    gemma4.audio.block_count                      12                         \n    gemma4.audio.conv_kernel_size                 5                          \n    gemma4.audio.embedding_length                 1024                       \n    gemma4.audio.feed_forward_length              4096                       \n    gemma4.block_count                            35                         \n    gemma4.context_length                         131072                     \n    gemma4.embedding_length                       1536                       \n    gemma4.embedding_length_per_layer_input       256                        \n    gemma4.feed_forward_length                    [6144 ...+34 more]         \n    gemma4.final_logit_softcapping                30                         \n    gemma4.rope.dimension_count                   512                        \n    gemma4.rope.dimension_count_swa               256                        \n    gemma4.rope.freq_base                         1e+06                      \n    gemma4.rope.freq_base_swa                     10000                      \n    gemma4.vision.attention.head_count            12                         \n    gemma4.vision.attention.layer_norm_epsilon    1e-06                      \n    gemma4.vision.block_count                     16                         \n    gemma4.vision.embedding_length                768                        \n    gemma4.vision.feed_forward_length             3072                       \n    gemma4.vision.num_channels                    3                          \n    gemma4.vision.patch_size                      16                         \n    gemma4.vision.projector.scale_factor          3                          \n    general.architecture                          gemma4                     \n    general.file_type                             15                         \n    general.parameter_count                       5.123179235e+09            \n    general.quantization_version                  2                          \n    tokenizer.ggml.add_bos_token                  false                      \n    tokenizer.ggml.add_eos_token                  false                      \n    tokenizer.ggml.add_mask_token                 false                      \n    tokenizer.ggml.add_padding_token              false                      \n    tokenizer.ggml.add_unknown_token              false                      \n    tokenizer.ggml.bos_token_id                   2                          \n    tokenizer.ggml.eos_token_id                   1                          \n    tokenizer.ggml.eos_token_ids                  [1 106 ...+1 more]         \n    tokenizer.ggml.mask_token_id                  4                          \n    tokenizer.ggml.merges                         [                          \n                                                                               \n                                                    ...+514905 more]           \n    tokenizer.ggml.model                          llama                      \n    tokenizer.ggml.padding_token_id               0                          \n    tokenizer.ggml.pre                            gemma4                     \n    tokenizer.ggml.scores                         [0 1 2 ...+262141 more]    \n    tokenizer.ggml.token_type                     [3 3 3 ...+262141 more]    \n    tokenizer.ggml.tokens                         [<pad> ...+262143 more]    \n    tokenizer.ggml.unknown_token_id               3                          \n\n  Tensors\n    blk.0.attn_k.weight                  Q4_K    [1536 256]       \n    blk.0.attn_k_norm.weight             F32     [256]            \n    blk.0.attn_norm.weight               F32     [1536]           \n    blk.0.attn_output.weight             Q4_K    [2048 1536]      \n    blk.0.attn_q.weight                  Q4_K    [1536 2048]      \n    blk.0.attn_q_norm.weight             F32     [256]            \n    blk.0.attn_v.weight                  Q6_K    [1536 256]       \n    blk.0.ffn_down.weight                Q6_K    [6144 1536]      \n    blk.0.ffn_gate.weight                Q4_K    [1536 6144]      \n    blk.0.ffn_norm.weight                F32     [1536]           \n    blk.0.ffn_up.weight                  Q4_K    [1536 6144]      \n    blk.0.inp_gate.weight                Q4_K    [1536 256]       \n    blk.0.layer_output_scale.weight      F32     [1]              \n    blk.0.post_attention_norm.weight     F32     [1536]           \n    blk.0.post_ffw_norm.weight           F32     [1536]           \n    blk.0.post_norm.weight               F32     [1536]           \n    blk.0.proj.weight                    Q4_K    [256 1536]       \n    blk.1.attn_k.weight                  Q4_K    [1536 256]       \n    blk.1.attn_k_norm.weight             F32     [256]            \n    blk.1.attn_norm.weight               F32     [1536]           \n    blk.1.attn_output.weight             Q4_K    [2048 1536]      \n    blk.1.attn_q.weight                  Q4_K    [1536 2048]      \n    blk.1.attn_q_norm.weight             F32     [256]            \n    blk.1.attn_v.weight                  Q6_K    [1536 256]       \n    blk.1.ffn_down.weight                Q6_K    [6144 1536]      \n    blk.1.ffn_gate.weight                Q4_K    [1536 6144]      \n    blk.1.ffn_norm.weight                F32     [1536]           \n    blk.1.ffn_up.weight                  Q4_K    [1536 6144]      \n    blk.1.inp_gate.weight                Q4_K    [1536 256]       \n    blk.1.layer_output_scale.weight      F32     [1]              \n    blk.1.post_attention_norm.weight     F32     [1536]           \n    blk.1.post_ffw_norm.weight           F32     [1536]           \n    blk.1.post_norm.weight               F32     [1536]           \n    blk.1.proj.weight                    Q4_K    [256 1536]       \n    blk.2.attn_k.weight                  Q4_K    [1536 256]       \n    blk.2.attn_k_norm.weight             F32     [256]            \n    blk.2.attn_norm.weight               F32     [1536]           \n    blk.2.attn_output.weight             Q4_K    [2048 1536]      \n    blk.2.attn_q.weight                  Q4_K    [1536 2048]      \n    blk.2.attn_q_norm.weight             F32     [256]            \n    blk.2.attn_v.weight                  Q6_K    [1536 256]       \n    blk.2.ffn_down.weight                Q6_K    [6144 1536]      \n    blk.2.ffn_gate.weight                Q4_K    [1536 6144]      \n    blk.2.ffn_norm.weight                F32     [1536]           \n    blk.2.ffn_up.weight                  Q4_K    [1536 6144]      \n    blk.2.inp_gate.weight                Q4_K    [1536 256]       \n    blk.2.layer_output_scale.weight      F32     [1]              \n    blk.2.post_attention_norm.weight     F32     [1536]           \n    blk.2.post_ffw_norm.weight           F32     [1536]           \n    blk.2.post_norm.weight               F32     [1536]           \n    blk.2.proj.weight                    Q4_K    [256 1536]       \n    blk.3.attn_k.weight                  Q4_K    [1536 256]       \n    blk.3.attn_k_norm.weight             F32     [256]            \n    blk.3.attn_norm.weight               F32     [1536]           \n    blk.3.attn_output.weight             Q4_K    [2048 1536]      \n    blk.3.attn_q.weight                  Q4_K    [1536 2048]      \n    blk.3.attn_q_norm.weight             F32     [256]            \n    blk.3.attn_v.weight                  Q6_K    [1536 256]       \n    blk.3.ffn_down.weight                Q6_K    [6144 1536]      \n    blk.3.ffn_gate.weight                Q4_K    [1536 6144]      \n    blk.3.ffn_norm.weight                F32     [1536]           \n    blk.3.ffn_up.weight                  Q4_K    [1536 6144]      \n    blk.3.inp_gate.weight                Q4_K    [1536 256]       \n    blk.3.layer_output_scale.weight      F32     [1]              \n    blk.3.post_attention_norm.weight     F32     [1536]           \n    blk.3.post_ffw_norm.weight           F32     [1536]           \n    blk.3.post_norm.weight               F32     [1536]           \n    blk.3.proj.weight                    Q4_K    [256 1536]       \n    blk.4.attn_k.weight                  Q4_K    [1536 512]       \n    blk.4.attn_k_norm.weight             F32     [512]            \n    blk.4.attn_norm.weight               F32     [1536]           \n    blk.4.attn_output.weight             Q4_K    [4096 1536]      \n    blk.4.attn_q.weight                  Q4_K    [1536 4096]      \n    blk.4.attn_q_norm.weight             F32     [512]            \n    blk.4.attn_v.weight                  Q6_K    [1536 512]       \n    blk.4.ffn_down.weight                Q4_K    [6144 1536]      \n    blk.4.ffn_gate.weight                Q4_K    [1536 6144]      \n    blk.4.ffn_norm.weight                F32     [1536]           \n    blk.4.ffn_up.weight                  Q4_K    [1536 6144]      \n    blk.4.inp_gate.weight                Q4_K    [1536 256]       \n    blk.4.layer_output_scale.weight      F32     [1]              \n    blk.4.post_attention_norm.weight     F32     [1536]           \n    blk.4.post_ffw_norm.weight           F32     [1536]           \n    blk.4.post_norm.weight               F32     [1536]           \n    blk.4.proj.weight                    Q4_K    [256 1536]       \n    blk.5.attn_k.weight                  Q4_K    [1536 256]       \n    blk.5.attn_k_norm.weight             F32     [256]            \n    blk.5.attn_norm.weight               F32     [1536]           \n    blk.5.attn_output.weight             Q4_K    [2048 1536]      \n    blk.5.attn_q.weight                  Q4_K    [1536 2048]      \n    blk.5.attn_q_norm.weight             F32     [256]            \n    blk.5.attn_v.weight                  Q6_K    [1536 256]       \n    blk.5.ffn_down.weight                Q4_K    [6144 1536]      \n    blk.5.ffn_gate.weight                Q4_K    [1536 6144]      \n    blk.5.ffn_norm.weight                F32     [1536]           \n    blk.5.ffn_up.weight                  Q4_K    [1536 6144]      \n    blk.5.inp_gate.weight                Q4_K    [1536 256]       \n    blk.5.layer_output_scale.weight      F32     [1]              \n    blk.5.post_attention_norm.weight     F32     [1536]           \n    blk.5.post_ffw_norm.weight           F32     [1536]           \n    blk.5.post_norm.weight               F32     [1536]           \n    blk.5.proj.weight                    Q4_K    [256 1536]       \n    blk.6.attn_k.weight                  Q4_K    [1536 256]       \n    blk.6.attn_k_norm.weight             F32     [256]            \n    blk.6.attn_norm.weight               F32     [1536]           \n    blk.6.attn_output.weight             Q4_K    [2048 1536]      \n    blk.6.attn_q.weight                  Q4_K    [1536 2048]      \n    blk.6.attn_q_norm.weight             F32     [256]            \n    blk.6.attn_v.weight                  Q6_K    [1536 256]       \n    blk.6.ffn_down.weight                Q6_K    [6144 1536]      \n    blk.6.ffn_gate.weight                Q4_K    [1536 6144]      \n    blk.6.ffn_norm.weight                F32     [1536]           \n    blk.6.ffn_up.weight                  Q4_K    [1536 6144]      \n    blk.6.inp_gate.weight                Q4_K    [1536 256]       \n    blk.6.layer_output_scale.weight      F32     [1]              \n    blk.6.post_attention_norm.weight     F32     [1536]           \n    blk.6.post_ffw_norm.weight           F32     [1536]           \n    blk.6.post_norm.weight               F32     [1536]           \n    blk.6.proj.weight                    Q4_K    [256 1536]       \n    blk.7.attn_k.weight                  Q4_K    [1536 256]       \n    blk.7.attn_k_norm.weight             F32     [256]            \n    blk.7.attn_norm.weight               F32     [1536]           \n    blk.7.attn_output.weight             Q4_K    [2048 1536]      \n    blk.7.attn_q.weight                  Q4_K    [1536 2048]      \n    blk.7.attn_q_norm.weight             F32     [256]            \n    blk.7.attn_v.weight                  Q4_K    [1536 256]       \n    blk.7.ffn_down.weight                Q4_K    [6144 1536]      \n    blk.7.ffn_gate.weight                Q4_K    [1536 6144]      \n    blk.7.ffn_norm.weight                F32     [1536]           \n    blk.7.ffn_up.weight                  Q4_K    [1536 6144]      \n    blk.7.inp_gate.weight                Q4_K    [1536 256]       \n    blk.7.layer_output_scale.weight      F32     [1]              \n    blk.7.post_attention_norm.weight     F32     [1536]           \n    blk.7.post_ffw_norm.weight           F32     [1536]           \n    blk.7.post_norm.weight               F32     [1536]           \n    blk.7.proj.weight                    Q4_K    [256 1536]       \n    blk.8.attn_k.weight                  Q4_K    [1536 256]       \n    blk.8.attn_k_norm.weight             F32     [256]            \n    blk.8.attn_norm.weight               F32     [1536]           \n    blk.8.attn_output.weight             Q4_K    [2048 1536]      \n    blk.8.attn_q.weight                  Q4_K    [1536 2048]      \n    blk.8.attn_q_norm.weight             F32     [256]            \n    blk.8.attn_v.weight                  Q4_K    [1536 256]       \n    blk.8.ffn_down.weight                Q4_K    [6144 1536]      \n    blk.8.ffn_gate.weight                Q4_K    [1536 6144]      \n    blk.8.ffn_norm.weight                F32     [1536]           \n    blk.8.ffn_up.weight                  Q4_K    [1536 6144]      \n    blk.8.inp_gate.weight                Q4_K    [1536 256]       \n    blk.8.layer_output_scale.weight      F32     [1]              \n    blk.8.post_attention_norm.weight     F32     [1536]           \n    blk.8.post_ffw_norm.weight           F32     [1536]           \n    blk.8.post_norm.weight               F32     [1536]           \n    blk.8.proj.weight                    Q4_K    [256 1536]       \n    blk.9.attn_k.weight                  Q4_K    [1536 512]       \n    blk.9.attn_k_norm.weight             F32     [512]            \n    blk.9.attn_norm.weight               F32     [1536]           \n    blk.9.attn_output.weight             Q4_K    [4096 1536]      \n    blk.9.attn_q.weight                  Q4_K    [1536 4096]      \n    blk.9.attn_q_norm.weight             F32     [512]            \n    blk.9.attn_v.weight                  Q6_K    [1536 512]       \n    blk.9.ffn_down.weight                Q6_K    [6144 1536]      \n    blk.9.ffn_gate.weight                Q4_K    [1536 6144]      \n    blk.9.ffn_norm.weight                F32     [1536]           \n    blk.9.ffn_up.weight                  Q4_K    [1536 6144]      \n    blk.9.inp_gate.weight                Q4_K    [1536 256]       \n    blk.9.layer_output_scale.weight      F32     [1]              \n    blk.9.post_attention_norm.weight     F32     [1536]           \n    blk.9.post_ffw_norm.weight           F32     [1536]           \n    blk.9.post_norm.weight               F32     [1536]           \n    blk.9.proj.weight                    Q4_K    [256 1536]       \n    blk.10.attn_k.weight                 Q4_K    [1536 256]       \n    blk.10.attn_k_norm.weight            F32     [256]            \n    blk.10.attn_norm.weight              F32     [1536]           \n    blk.10.attn_output.weight            Q4_K    [2048 1536]      \n    blk.10.attn_q.weight                 Q4_K    [1536 2048]      \n    blk.10.attn_q_norm.weight            F32     [256]            \n    blk.10.attn_v.weight                 Q4_K    [1536 256]       \n    blk.10.ffn_down.weight               Q4_K    [6144 1536]      \n    blk.10.ffn_gate.weight               Q4_K    [1536 6144]      \n    blk.10.ffn_norm.weight               F32     [1536]           \n    blk.10.ffn_up.weight                 Q4_K    [1536 6144]      \n    blk.10.inp_gate.weight               Q4_K    [1536 256]       \n    blk.10.layer_output_scale.weight     F32     [1]              \n    blk.10.post_attention_norm.weight    F32     [1536]           \n    blk.10.post_ffw_norm.weight          F32     [1536]           \n    blk.10.post_norm.weight              F32     [1536]           \n    blk.10.proj.weight                   Q4_K    [256 1536]       \n    blk.11.attn_k.weight                 Q4_K    [1536 256]       \n    blk.11.attn_k_norm.weight            F32     [256]            \n    blk.11.attn_norm.weight              F32     [1536]           \n    blk.11.attn_output.weight            Q4_K    [2048 1536]      \n    blk.11.attn_q.weight                 Q4_K    [1536 2048]      \n    blk.11.attn_q_norm.weight            F32     [256]            \n    blk.11.attn_v.weight                 Q4_K    [1536 256]       \n    blk.11.ffn_down.weight               Q4_K    [6144 1536]      \n    blk.11.ffn_gate.weight               Q4_K    [1536 6144]      \n    blk.11.ffn_norm.weight               F32     [1536]           \n    blk.11.ffn_up.weight                 Q4_K    [1536 6144]      \n    blk.11.inp_gate.weight               Q4_K    [1536 256]       \n    blk.11.layer_output_scale.weight     F32     [1]              \n    blk.11.post_attention_norm.weight    F32     [1536]           \n    blk.11.post_ffw_norm.weight          F32     [1536]           \n    blk.11.post_norm.weight              F32     [1536]           \n    blk.11.proj.weight                   Q4_K    [256 1536]       \n    blk.12.attn_k.weight                 Q4_K    [1536 256]       \n    blk.12.attn_k_norm.weight            F32     [256]            \n    blk.12.attn_norm.weight              F32     [1536]           \n    blk.12.attn_output.weight            Q4_K    [2048 1536]      \n    blk.12.attn_q.weight                 Q4_K    [1536 2048]      \n    blk.12.attn_q_norm.weight            F32     [256]            \n    blk.12.attn_v.weight                 Q6_K    [1536 256]       \n    blk.12.ffn_down.weight               Q6_K    [6144 1536]      \n    blk.12.ffn_gate.weight               Q4_K    [1536 6144]      \n    blk.12.ffn_norm.weight               F32     [1536]           \n    blk.12.ffn_up.weight                 Q4_K    [1536 6144]      \n    blk.12.inp_gate.weight               Q4_K    [1536 256]       \n    blk.12.layer_output_scale.weight     F32     [1]              \n    blk.12.post_attention_norm.weight    F32     [1536]           \n    blk.12.post_ffw_norm.weight          F32     [1536]           \n    blk.12.post_norm.weight              F32     [1536]           \n    blk.12.proj.weight                   Q4_K    [256 1536]       \n    blk.13.attn_k.weight                 Q4_K    [1536 256]       \n    blk.13.attn_k_norm.weight            F32     [256]            \n    blk.13.attn_norm.weight              F32     [1536]           \n    blk.13.attn_output.weight            Q4_K    [2048 1536]      \n    blk.13.attn_q.weight                 Q4_K    [1536 2048]      \n    blk.13.attn_q_norm.weight            F32     [256]            \n    blk.13.attn_v.weight                 Q4_K    [1536 256]       \n    blk.13.ffn_down.weight               Q4_K    [6144 1536]      \n    blk.13.ffn_gate.weight               Q4_K    [1536 6144]      \n    blk.13.ffn_norm.weight               F32     [1536]           \n    blk.13.ffn_up.weight                 Q4_K    [1536 6144]      \n    blk.13.inp_gate.weight               Q4_K    [1536 256]       \n    blk.13.layer_output_scale.weight     F32     [1]              \n    blk.13.post_attention_norm.weight    F32     [1536]           \n    blk.13.post_ffw_norm.weight          F32     [1536]           \n    blk.13.post_norm.weight              F32     [1536]           \n    blk.13.proj.weight                   Q4_K    [256 1536]       \n    blk.14.attn_k.weight                 Q4_K    [1536 512]       \n    blk.14.attn_k_norm.weight            F32     [512]            \n    blk.14.attn_norm.weight              F32     [1536]           \n    blk.14.attn_output.weight            Q4_K    [4096 1536]      \n    blk.14.attn_q.weight                 Q4_K    [1536 4096]      \n    blk.14.attn_q_norm.weight            F32     [512]            \n    blk.14.attn_v.weight                 Q4_K    [1536 512]       \n    blk.14.ffn_down.weight               Q4_K    [6144 1536]      \n    blk.14.ffn_gate.weight               Q4_K    [1536 6144]      \n    blk.14.ffn_norm.weight               F32     [1536]           \n    blk.14.ffn_up.weight                 Q4_K    [1536 6144]      \n    blk.14.inp_gate.weight               Q4_K    [1536 256]       \n    blk.14.layer_output_scale.weight     F32     [1]              \n    blk.14.post_attention_norm.weight    F32     [1536]           \n    blk.14.post_ffw_norm.weight          F32     [1536]           \n    blk.14.post_norm.weight              F32     [1536]           \n    blk.14.proj.weight                   Q4_K    [256 1536]       \n    blk.15.attn_k.weight                 Q4_K    [1536 256]       \n    blk.15.attn_k_norm.weight            F32     [256]            \n    blk.15.attn_norm.weight              F32     [1536]           \n    blk.15.attn_output.weight            Q4_K    [2048 1536]      \n    blk.15.attn_q.weight                 Q4_K    [1536 2048]      \n    blk.15.attn_q_norm.weight            F32     [256]            \n    blk.15.attn_v.weight                 Q6_K    [1536 256]       \n    blk.15.ffn_down.weight               Q6_K    [12288 1536]     \n    blk.15.ffn_gate.weight               Q4_K    [1536 12288]     \n    blk.15.ffn_norm.weight               F32     [1536]           \n    blk.15.ffn_up.weight                 Q4_K    [1536 12288]     \n    blk.15.inp_gate.weight               Q4_K    [1536 256]       \n    blk.15.layer_output_scale.weight     F32     [1]              \n    blk.15.post_attention_norm.weight    F32     [1536]           \n    blk.15.post_ffw_norm.weight          F32     [1536]           \n    blk.15.post_norm.weight              F32     [1536]           \n    blk.15.proj.weight                   Q4_K    [256 1536]       \n    blk.16.attn_k.weight                 Q4_K    [1536 256]       \n    blk.16.attn_k_norm.weight            F32     [256]            \n    blk.16.attn_norm.weight              F32     [1536]           \n    blk.16.attn_output.weight            Q4_K    [2048 1536]      \n    blk.16.attn_q.weight                 Q4_K    [1536 2048]      \n    blk.16.attn_q_norm.weight            F32     [256]            \n    blk.16.attn_v.weight                 Q4_K    [1536 256]       \n    blk.16.ffn_down.weight               Q4_K    [12288 1536]     \n    blk.16.ffn_gate.weight               Q4_K    [1536 12288]     \n    blk.16.ffn_norm.weight               F32     [1536]           \n    blk.16.ffn_up.weight                 Q4_K    [1536 12288]     \n    blk.16.inp_gate.weight               Q4_K    [1536 256]       \n    blk.16.layer_output_scale.weight     F32     [1]              \n    blk.16.post_attention_norm.weight    F32     [1536]           \n    blk.16.post_ffw_norm.weight          F32     [1536]           \n    blk.16.post_norm.weight              F32     [1536]           \n    blk.16.proj.weight                   Q4_K    [256 1536]       \n    blk.17.attn_k.weight                 Q4_K    [1536 256]       \n    blk.17.attn_k_norm.weight            F32     [256]            \n    blk.17.attn_norm.weight              F32     [1536]           \n    blk.17.attn_output.weight            Q4_K    [2048 1536]      \n    blk.17.attn_q.weight                 Q4_K    [1536 2048]      \n    blk.17.attn_q_norm.weight            F32     [256]            \n    blk.17.attn_v.weight                 Q4_K    [1536 256]       \n    blk.17.ffn_down.weight               Q4_K    [12288 1536]     \n    blk.17.ffn_gate.weight               Q4_K    [1536 12288]     \n    blk.17.ffn_norm.weight               F32     [1536]           \n    blk.17.ffn_up.weight                 Q4_K    [1536 12288]     \n    blk.17.inp_gate.weight               Q4_K    [1536 256]       \n    blk.17.layer_output_scale.weight     F32     [1]              \n    blk.17.post_attention_norm.weight    F32     [1536]           \n    blk.17.post_ffw_norm.weight          F32     [1536]           \n    blk.17.post_norm.weight              F32     [1536]           \n    blk.17.proj.weight                   Q4_K    [256 1536]       \n    blk.18.attn_k.weight                 Q4_K    [1536 256]       \n    blk.18.attn_k_norm.weight            F32     [256]            \n    blk.18.attn_norm.weight              F32     [1536]           \n    blk.18.attn_output.weight            Q4_K    [2048 1536]      \n    blk.18.attn_q.weight                 Q4_K    [1536 2048]      \n    blk.18.attn_q_norm.weight            F32     [256]            \n    blk.18.attn_v.weight                 Q6_K    [1536 256]       \n    blk.18.ffn_down.weight               Q6_K    [12288 1536]     \n    blk.18.ffn_gate.weight               Q4_K    [1536 12288]     \n    blk.18.ffn_norm.weight               F32     [1536]           \n    blk.18.ffn_up.weight                 Q4_K    [1536 12288]     \n    blk.18.inp_gate.weight               Q4_K    [1536 256]       \n    blk.18.layer_output_scale.weight     F32     [1]              \n    blk.18.post_attention_norm.weight    F32     [1536]           \n    blk.18.post_ffw_norm.weight          F32     [1536]           \n    blk.18.post_norm.weight              F32     [1536]           \n    blk.18.proj.weight                   Q4_K    [256 1536]       \n    blk.19.attn_k.weight                 Q4_K    [1536 512]       \n    blk.19.attn_k_norm.weight            F32     [512]            \n    blk.19.attn_norm.weight              F32     [1536]           \n    blk.19.attn_output.weight            Q4_K    [4096 1536]      \n    blk.19.attn_q.weight                 Q4_K    [1536 4096]      \n    blk.19.attn_q_norm.weight            F32     [512]            \n    blk.19.attn_v.weight                 Q4_K    [1536 512]       \n    blk.19.ffn_down.weight               Q4_K    [12288 1536]     \n    blk.19.ffn_gate.weight               Q4_K    [1536 12288]     \n    blk.19.ffn_norm.weight               F32     [1536]           \n    blk.19.ffn_up.weight                 Q4_K    [1536 12288]     \n    blk.19.inp_gate.weight               Q4_K    [1536 256]       \n    blk.19.layer_output_scale.weight     F32     [1]              \n    blk.19.post_attention_norm.weight    F32     [1536]           \n    blk.19.post_ffw_norm.weight          F32     [1536]           \n    blk.19.post_norm.weight              F32     [1536]           \n    blk.19.proj.weight                   Q4_K    [256 1536]       \n    blk.20.attn_k.weight                 Q4_K    [1536 256]       \n    blk.20.attn_k_norm.weight            F32     [256]            \n    blk.20.attn_norm.weight              F32     [1536]           \n    blk.20.attn_output.weight            Q4_K    [2048 1536]      \n    blk.20.attn_q.weight                 Q4_K    [1536 2048]      \n    blk.20.attn_q_norm.weight            F32     [256]            \n    blk.20.attn_v.weight                 Q4_K    [1536 256]       \n    blk.20.ffn_down.weight               Q4_K    [12288 1536]     \n    blk.20.ffn_gate.weight               Q4_K    [1536 12288]     \n    blk.20.ffn_norm.weight               F32     [1536]           \n    blk.20.ffn_up.weight                 Q4_K    [1536 12288]     \n    blk.20.inp_gate.weight               Q4_K    [1536 256]       \n    blk.20.layer_output_scale.weight     F32     [1]              \n    blk.20.post_attention_norm.weight    F32     [1536]           \n    blk.20.post_ffw_norm.weight          F32     [1536]           \n    blk.20.post_norm.weight              F32     [1536]           \n    blk.20.proj.weight                   Q4_K    [256 1536]       \n    blk.21.attn_k.weight                 Q4_K    [1536 256]       \n    blk.21.attn_k_norm.weight            F32     [256]            \n    blk.21.attn_norm.weight              F32     [1536]           \n    blk.21.attn_output.weight            Q4_K    [2048 1536]      \n    blk.21.attn_q.weight                 Q4_K    [1536 2048]      \n    blk.21.attn_q_norm.weight            F32     [256]            \n    blk.21.attn_v.weight                 Q6_K    [1536 256]       \n    blk.21.ffn_down.weight               Q6_K    [12288 1536]     \n    blk.21.ffn_gate.weight               Q4_K    [1536 12288]     \n    blk.21.ffn_norm.weight               F32     [1536]           \n    blk.21.ffn_up.weight                 Q4_K    [1536 12288]     \n    blk.21.inp_gate.weight               Q4_K    [1536 256]       \n    blk.21.layer_output_scale.weight     F32     [1]              \n    blk.21.post_attention_norm.weight    F32     [1536]           \n    blk.21.post_ffw_norm.weight          F32     [1536]           \n    blk.21.post_norm.weight              F32     [1536]           \n    blk.21.proj.weight                   Q4_K    [256 1536]       \n    blk.22.attn_k.weight                 Q4_K    [1536 256]       \n    blk.22.attn_k_norm.weight            F32     [256]            \n    blk.22.attn_norm.weight              F32     [1536]           \n    blk.22.attn_output.weight            Q4_K    [2048 1536]      \n    blk.22.attn_q.weight                 Q4_K    [1536 2048]      \n    blk.22.attn_q_norm.weight            F32     [256]            \n    blk.22.attn_v.weight                 Q4_K    [1536 256]       \n    blk.22.ffn_down.weight               Q4_K    [12288 1536]     \n    blk.22.ffn_gate.weight               Q4_K    [1536 12288]     \n    blk.22.ffn_norm.weight               F32     [1536]           \n    blk.22.ffn_up.weight                 Q4_K    [1536 12288]     \n    blk.22.inp_gate.weight               Q4_K    [1536 256]       \n    blk.22.layer_output_scale.weight     F32     [1]              \n    blk.22.post_attention_norm.weight    F32     [1536]           \n    blk.22.post_ffw_norm.weight          F32     [1536]           \n    blk.22.post_norm.weight              F32     [1536]           \n    blk.22.proj.weight                   Q4_K    [256 1536]       \n    blk.23.attn_k.weight                 Q4_K    [1536 256]       \n    blk.23.attn_k_norm.weight            F32     [256]            \n    blk.23.attn_norm.weight              F32     [1536]           \n    blk.23.attn_output.weight            Q4_K    [2048 1536]      \n    blk.23.attn_q.weight                 Q4_K    [1536 2048]      \n    blk.23.attn_q_norm.weight            F32     [256]            \n    blk.23.attn_v.weight                 Q4_K    [1536 256]       \n    blk.23.ffn_down.weight               Q4_K    [12288 1536]     \n    blk.23.ffn_gate.weight               Q4_K    [1536 12288]     \n    blk.23.ffn_norm.weight               F32     [1536]           \n    blk.23.ffn_up.weight                 Q4_K    [1536 12288]     \n    blk.23.inp_gate.weight               Q4_K    [1536 256]       \n    blk.23.layer_output_scale.weight     F32     [1]              \n    blk.23.post_attention_norm.weight    F32     [1536]           \n    blk.23.post_ffw_norm.weight          F32     [1536]           \n    blk.23.post_norm.weight              F32     [1536]           \n    blk.23.proj.weight                   Q4_K    [256 1536]       \n    blk.24.attn_k.weight                 Q4_K    [1536 512]       \n    blk.24.attn_k_norm.weight            F32     [512]            \n    blk.24.attn_norm.weight              F32     [1536]           \n    blk.24.attn_output.weight            Q4_K    [4096 1536]      \n    blk.24.attn_q.weight                 Q4_K    [1536 4096]      \n    blk.24.attn_q_norm.weight            F32     [512]            \n    blk.24.attn_v.weight                 Q6_K    [1536 512]       \n    blk.24.ffn_down.weight               Q6_K    [12288 1536]     \n    blk.24.ffn_gate.weight               Q4_K    [1536 12288]     \n    blk.24.ffn_norm.weight               F32     [1536]           \n    blk.24.ffn_up.weight                 Q4_K    [1536 12288]     \n    blk.24.inp_gate.weight               Q4_K    [1536 256]       \n    blk.24.layer_output_scale.weight     F32     [1]              \n    blk.24.post_attention_norm.weight    F32     [1536]           \n    blk.24.post_ffw_norm.weight          F32     [1536]           \n    blk.24.post_norm.weight              F32     [1536]           \n    blk.24.proj.weight                   Q4_K    [256 1536]       \n    blk.25.attn_k.weight                 Q4_K    [1536 256]       \n    blk.25.attn_k_norm.weight            F32     [256]            \n    blk.25.attn_norm.weight              F32     [1536]           \n    blk.25.attn_output.weight            Q4_K    [2048 1536]      \n    blk.25.attn_q.weight                 Q4_K    [1536 2048]      \n    blk.25.attn_q_norm.weight            F32     [256]            \n    blk.25.attn_v.weight                 Q4_K    [1536 256]       \n    blk.25.ffn_down.weight               Q4_K    [12288 1536]     \n    blk.25.ffn_gate.weight               Q4_K    [1536 12288]     \n    blk.25.ffn_norm.weight               F32     [1536]           \n    blk.25.ffn_up.weight                 Q4_K    [1536 12288]     \n    blk.25.inp_gate.weight               Q4_K    [1536 256]       \n    blk.25.layer_output_scale.weight     F32     [1]              \n    blk.25.post_attention_norm.weight    F32     [1536]           \n    blk.25.post_ffw_norm.weight          F32     [1536]           \n    blk.25.post_norm.weight              F32     [1536]           \n    blk.25.proj.weight                   Q4_K    [256 1536]       \n    blk.26.attn_k.weight                 Q4_K    [1536 256]       \n    blk.26.attn_k_norm.weight            F32     [256]            \n    blk.26.attn_norm.weight              F32     [1536]           \n    blk.26.attn_output.weight            Q4_K    [2048 1536]      \n    blk.26.attn_q.weight                 Q4_K    [1536 2048]      \n    blk.26.attn_q_norm.weight            F32     [256]            \n    blk.26.attn_v.weight                 Q4_K    [1536 256]       \n    blk.26.ffn_down.weight               Q4_K    [12288 1536]     \n    blk.26.ffn_gate.weight               Q4_K    [1536 12288]     \n    blk.26.ffn_norm.weight               F32     [1536]           \n    blk.26.ffn_up.weight                 Q4_K    [1536 12288]     \n    blk.26.inp_gate.weight               Q4_K    [1536 256]       \n    blk.26.layer_output_scale.weight     F32     [1]              \n    blk.26.post_attention_norm.weight    F32     [1536]           \n    blk.26.post_ffw_norm.weight          F32     [1536]           \n    blk.26.post_norm.weight              F32     [1536]           \n    blk.26.proj.weight                   Q4_K    [256 1536]       \n    blk.27.attn_k.weight                 Q4_K    [1536 256]       \n    blk.27.attn_k_norm.weight            F32     [256]            \n    blk.27.attn_norm.weight              F32     [1536]           \n    blk.27.attn_output.weight            Q4_K    [2048 1536]      \n    blk.27.attn_q.weight                 Q4_K    [1536 2048]      \n    blk.27.attn_q_norm.weight            F32     [256]            \n    blk.27.attn_v.weight                 Q6_K    [1536 256]       \n    blk.27.ffn_down.weight               Q6_K    [12288 1536]     \n    blk.27.ffn_gate.weight               Q4_K    [1536 12288]     \n    blk.27.ffn_norm.weight               F32     [1536]           \n    blk.27.ffn_up.weight                 Q4_K    [1536 12288]     \n    blk.27.inp_gate.weight               Q4_K    [1536 256]       \n    blk.27.layer_output_scale.weight     F32     [1]              \n    blk.27.post_attention_norm.weight    F32     [1536]           \n    blk.27.post_ffw_norm.weight          F32     [1536]           \n    blk.27.post_norm.weight              F32     [1536]           \n    blk.27.proj.weight                   Q4_K    [256 1536]       \n    blk.28.attn_k.weight                 Q4_K    [1536 256]       \n    blk.28.attn_k_norm.weight            F32     [256]            \n    blk.28.attn_norm.weight              F32     [1536]           \n    blk.28.attn_output.weight            Q4_K    [2048 1536]      \n    blk.28.attn_q.weight                 Q4_K    [1536 2048]      \n    blk.28.attn_q_norm.weight            F32     [256]            \n    blk.28.attn_v.weight                 Q4_K    [1536 256]       \n    blk.28.ffn_down.weight               Q4_K    [12288 1536]     \n    blk.28.ffn_gate.weight               Q4_K    [1536 12288]     \n    blk.28.ffn_norm.weight               F32     [1536]           \n    blk.28.ffn_up.weight                 Q4_K    [1536 12288]     \n    blk.28.inp_gate.weight               Q4_K    [1536 256]       \n    blk.28.layer_output_scale.weight     F32     [1]              \n    blk.28.post_attention_norm.weight    F32     [1536]           \n    blk.28.post_ffw_norm.weight          F32     [1536]           \n    blk.28.post_norm.weight              F32     [1536]           \n    blk.28.proj.weight                   Q4_K    [256 1536]       \n    blk.29.attn_k.weight                 Q4_K    [1536 512]       \n    blk.29.attn_k_norm.weight            F32     [512]            \n    blk.29.attn_norm.weight              F32     [1536]           \n    blk.29.attn_output.weight            Q4_K    [4096 1536]      \n    blk.29.attn_q.weight                 Q4_K    [1536 4096]      \n    blk.29.attn_q_norm.weight            F32     [512]            \n    blk.29.attn_v.weight                 Q4_K    [1536 512]       \n    blk.29.ffn_down.weight               Q4_K    [12288 1536]     \n    blk.29.ffn_gate.weight               Q4_K    [1536 12288]     \n    blk.29.ffn_norm.weight               F32     [1536]           \n    blk.29.ffn_up.weight                 Q4_K    [1536 12288]     \n    blk.29.inp_gate.weight               Q4_K    [1536 256]       \n    blk.29.layer_output_scale.weight     F32     [1]              \n    blk.29.post_attention_norm.weight    F32     [1536]           \n    blk.29.post_ffw_norm.weight          F32     [1536]           \n    blk.29.post_norm.weight              F32     [1536]           \n    blk.29.proj.weight                   Q4_K    [256 1536]       \n    blk.30.attn_k.weight                 Q4_K    [1536 256]       \n    blk.30.attn_k_norm.weight            F32     [256]            \n    blk.30.attn_norm.weight              F32     [1536]           \n    blk.30.attn_output.weight            Q4_K    [2048 1536]      \n    blk.30.attn_q.weight                 Q4_K    [1536 2048]      \n    blk.30.attn_q_norm.weight            F32     [256]            \n    blk.30.attn_v.weight                 Q6_K    [1536 256]       \n    blk.30.ffn_down.weight               Q6_K    [12288 1536]     \n    blk.30.ffn_gate.weight               Q4_K    [1536 12288]     \n    blk.30.ffn_norm.weight               F32     [1536]           \n    blk.30.ffn_up.weight                 Q4_K    [1536 12288]     \n    blk.30.inp_gate.weight               Q4_K    [1536 256]       \n    blk.30.layer_output_scale.weight     F32     [1]              \n    blk.30.post_attention_norm.weight    F32     [1536]           \n    blk.30.post_ffw_norm.weight          F32     [1536]           \n    blk.30.post_norm.weight              F32     [1536]           \n    blk.30.proj.weight                   Q4_K    [256 1536]       \n    blk.31.attn_k.weight                 Q4_K    [1536 256]       \n    blk.31.attn_k_norm.weight            F32     [256]            \n    blk.31.attn_norm.weight              F32     [1536]           \n    blk.31.attn_output.weight            Q4_K    [2048 1536]      \n    blk.31.attn_q.weight                 Q4_K    [1536 2048]      \n    blk.31.attn_q_norm.weight            F32     [256]            \n    blk.31.attn_v.weight                 Q4_K    [1536 256]       \n    blk.31.ffn_down.weight               Q6_K    [12288 1536]     \n    blk.31.ffn_gate.weight               Q4_K    [1536 12288]     \n    blk.31.ffn_norm.weight               F32     [1536]           \n    blk.31.ffn_up.weight                 Q4_K    [1536 12288]     \n    blk.31.inp_gate.weight               Q4_K    [1536 256]       \n    blk.31.layer_output_scale.weight     F32     [1]              \n    blk.31.post_attention_norm.weight    F32     [1536]           \n    blk.31.post_ffw_norm.weight          F32     [1536]           \n    blk.31.post_norm.weight              F32     [1536]           \n    blk.31.proj.weight                   Q4_K    [256 1536]       \n    blk.32.attn_k.weight                 Q4_K    [1536 256]       \n    blk.32.attn_k_norm.weight            F32     [256]            \n    blk.32.attn_norm.weight              F32     [1536]           \n    blk.32.attn_output.weight            Q4_K    [2048 1536]      \n    blk.32.attn_q.weight                 Q4_K    [1536 2048]      \n    blk.32.attn_q_norm.weight            F32     [256]            \n    blk.32.attn_v.weight                 Q4_K    [1536 256]       \n    blk.32.ffn_down.weight               Q6_K    [12288 1536]     \n    blk.32.ffn_gate.weight               Q4_K    [1536 12288]     \n    blk.32.ffn_norm.weight               F32     [1536]           \n    blk.32.ffn_up.weight                 Q4_K    [1536 12288]     \n    blk.32.inp_gate.weight               Q4_K    [1536 256]       \n    blk.32.layer_output_scale.weight     F32     [1]              \n    blk.32.post_attention_norm.weight    F32     [1536]           \n    blk.32.post_ffw_norm.weight          F32     [1536]           \n    blk.32.post_norm.weight              F32     [1536]           \n    blk.32.proj.weight                   Q4_K    [256 1536]       \n    blk.33.attn_k.weight                 Q4_K    [1536 256]       \n    blk.33.attn_k_norm.weight            F32     [256]            \n    blk.33.attn_norm.weight              F32     [1536]           \n    blk.33.attn_output.weight            Q4_K    [2048 1536]      \n    blk.33.attn_q.weight                 Q4_K    [1536 2048]      \n    blk.33.attn_q_norm.weight            F32     [256]            \n    blk.33.attn_v.weight                 Q6_K    [1536 256]       \n    blk.33.ffn_down.weight               Q6_K    [12288 1536]     \n    blk.33.ffn_gate.weight               Q4_K    [1536 12288]     \n    blk.33.ffn_norm.weight               F32     [1536]           \n    blk.33.ffn_up.weight                 Q4_K    [1536 12288]     \n    blk.33.inp_gate.weight               Q4_K    [1536 256]       \n    blk.33.layer_output_scale.weight     F32     [1]              \n    blk.33.post_attention_norm.weight    F32     [1536]           \n    blk.33.post_ffw_norm.weight          F32     [1536]           \n    blk.33.post_norm.weight              F32     [1536]           \n    blk.33.proj.weight                   Q4_K    [256 1536]       \n    blk.34.attn_k.weight                 Q4_K    [1536 512]       \n    blk.34.attn_k_norm.weight            F32     [512]            \n    blk.34.attn_norm.weight              F32     [1536]           \n    blk.34.attn_output.weight            Q4_K    [4096 1536]      \n    blk.34.attn_q.weight                 Q4_K    [1536 4096]      \n    blk.34.attn_q_norm.weight            F32     [512]            \n    blk.34.attn_v.weight                 Q4_K    [1536 512]       \n    blk.34.ffn_down.weight               Q6_K    [12288 1536]     \n    blk.34.ffn_gate.weight               Q4_K    [1536 12288]     \n    blk.34.ffn_norm.weight               F32     [1536]           \n    blk.34.ffn_up.weight                 Q4_K    [1536 12288]     \n    blk.34.inp_gate.weight               Q4_K    [1536 256]       \n    blk.34.layer_output_scale.weight     F32     [1]              \n    blk.34.post_attention_norm.weight    F32     [1536]           \n    blk.34.post_ffw_norm.weight          F32     [1536]           \n    blk.34.post_norm.weight              F32     [1536]           \n    blk.34.proj.weight                   Q4_K    [256 1536]       \n    a.blk.0.attn_k.input_max             F32     [1]              \n    a.blk.0.attn_k.input_min             F32     [1]              \n    a.blk.0.attn_k.output_max            F32     [1]              \n    a.blk.0.attn_k.output_min            F32     [1]              \n    a.blk.0.attn_k.weight                BF16    [1024 1024]      \n    a.blk.0.attn_out.input_max           F32     [1]              \n    a.blk.0.attn_out.input_min           F32     [1]              \n    a.blk.0.attn_out.output_max          F32     [1]              \n    a.blk.0.attn_out.output_min          F32     [1]              \n    a.blk.0.attn_out.weight              BF16    [1024 1024]      \n    a.blk.0.attn_q.input_max             F32     [1]              \n    a.blk.0.attn_q.input_min             F32     [1]              \n    a.blk.0.attn_q.output_max            F32     [1]              \n    a.blk.0.attn_q.output_min            F32     [1]              \n    a.blk.0.attn_q.weight                BF16    [1024 1024]      \n    a.blk.0.attn_v.input_max             F32     [1]              \n    a.blk.0.attn_v.input_min             F32     [1]              \n    a.blk.0.attn_v.output_max            F32     [1]              \n    a.blk.0.attn_v.output_min            F32     [1]              \n    a.blk.0.attn_v.weight                BF16    [1024 1024]      \n    a.blk.0.conv_dw.weight               F32     [5 1024]         \n    a.blk.0.conv_norm.weight             F32     [1024]           \n    a.blk.0.conv_pw1.input_max           F32     [1]              \n    a.blk.0.conv_pw1.input_min           F32     [1]              \n    a.blk.0.conv_pw1.output_max          F32     [1]              \n    a.blk.0.conv_pw1.output_min          F32     [1]              \n    a.blk.0.conv_pw1.weight              BF16    [1024 2048]      \n    a.blk.0.conv_pw2.input_max           F32     [1]              \n    a.blk.0.conv_pw2.input_min           F32     [1]              \n    a.blk.0.conv_pw2.output_max          F32     [1]              \n    a.blk.0.conv_pw2.output_min          F32     [1]              \n    a.blk.0.conv_pw2.weight              BF16    [1024 1024]      \n    a.blk.0.ffn_down.input_max           F32     [1]              \n    a.blk.0.ffn_down.input_min           F32     [1]              \n    a.blk.0.ffn_down.output_max          F32     [1]              \n    a.blk.0.ffn_down.output_min          F32     [1]              \n    a.blk.0.ffn_down.weight              BF16    [4096 1024]      \n    a.blk.0.ffn_down_1.input_max         F32     [1]              \n    a.blk.0.ffn_down_1.input_min         F32     [1]              \n    a.blk.0.ffn_down_1.output_max        F32     [1]              \n    a.blk.0.ffn_down_1.output_min        F32     [1]              \n    a.blk.0.ffn_down_1.weight            BF16    [4096 1024]      \n    a.blk.0.ffn_norm.weight              F32     [1024]           \n    a.blk.0.ffn_norm_1.weight            F32     [1024]           \n    a.blk.0.ffn_post_norm.weight         F32     [1024]           \n    a.blk.0.ffn_post_norm_1.weight       F32     [1024]           \n    a.blk.0.ffn_up.input_max             F32     [1]              \n    a.blk.0.ffn_up.input_min             F32     [1]              \n    a.blk.0.ffn_up.output_max            F32     [1]              \n    a.blk.0.ffn_up.output_min            F32     [1]              \n    a.blk.0.ffn_up.weight                BF16    [1024 4096]      \n    a.blk.0.ffn_up_1.input_max           F32     [1]              \n    a.blk.0.ffn_up_1.input_min           F32     [1]              \n    a.blk.0.ffn_up_1.output_max          F32     [1]              \n    a.blk.0.ffn_up_1.output_min          F32     [1]              \n    a.blk.0.ffn_up_1.weight              BF16    [1024 4096]      \n    a.blk.0.layer_pre_norm.weight        F32     [1024]           \n    a.blk.0.linear_pos.weight            BF16    [1024 1024]      \n    a.blk.0.ln1.weight                   F32     [1024]           \n    a.blk.0.ln2.weight                   F32     [1024]           \n    a.blk.0.norm_conv.weight             F32     [1024]           \n    a.blk.0.per_dim_scale.weight         F32     [128]            \n    a.blk.1.attn_k.input_max             F32     [1]              \n    a.blk.1.attn_k.input_min             F32     [1]              \n    a.blk.1.attn_k.output_max            F32     [1]              \n    a.blk.1.attn_k.output_min            F32     [1]              \n    a.blk.1.attn_k.weight                BF16    [1024 1024]      \n    a.blk.1.attn_out.input_max           F32     [1]              \n    a.blk.1.attn_out.input_min           F32     [1]              \n    a.blk.1.attn_out.output_max          F32     [1]              \n    a.blk.1.attn_out.output_min          F32     [1]              \n    a.blk.1.attn_out.weight              BF16    [1024 1024]      \n    a.blk.1.attn_q.input_max             F32     [1]              \n    a.blk.1.attn_q.input_min             F32     [1]              \n    a.blk.1.attn_q.output_max            F32     [1]              \n    a.blk.1.attn_q.output_min            F32     [1]              \n    a.blk.1.attn_q.weight                BF16    [1024 1024]      \n    a.blk.1.attn_v.input_max             F32     [1]              \n    a.blk.1.attn_v.input_min             F32     [1]              \n    a.blk.1.attn_v.output_max            F32     [1]              \n    a.blk.1.attn_v.output_min            F32     [1]              \n    a.blk.1.attn_v.weight                BF16    [1024 1024]      \n    a.blk.1.conv_dw.weight               F32     [5 1024]         \n    a.blk.1.conv_norm.weight             F32     [1024]           \n    a.blk.1.conv_pw1.input_max           F32     [1]              \n    a.blk.1.conv_pw1.input_min           F32     [1]              \n    a.blk.1.conv_pw1.output_max          F32     [1]              \n    a.blk.1.conv_pw1.output_min          F32     [1]              \n    a.blk.1.conv_pw1.weight              BF16    [1024 2048]      \n    a.blk.1.conv_pw2.input_max           F32     [1]              \n    a.blk.1.conv_pw2.input_min           F32     [1]              \n    a.blk.1.conv_pw2.output_max          F32     [1]              \n    a.blk.1.conv_pw2.output_min          F32     [1]              \n    a.blk.1.conv_pw2.weight              BF16    [1024 1024]      \n    a.blk.1.ffn_down.input_max           F32     [1]              \n    a.blk.1.ffn_down.input_min           F32     [1]              \n    a.blk.1.ffn_down.output_max          F32     [1]              \n    a.blk.1.ffn_down.output_min          F32     [1]              \n    a.blk.1.ffn_down.weight              BF16    [4096 1024]      \n    a.blk.1.ffn_down_1.input_max         F32     [1]              \n    a.blk.1.ffn_down_1.input_min         F32     [1]              \n    a.blk.1.ffn_down_1.output_max        F32     [1]              \n    a.blk.1.ffn_down_1.output_min        F32     [1]              \n    a.blk.1.ffn_down_1.weight            BF16    [4096 1024]      \n    a.blk.1.ffn_norm.weight              F32     [1024]           \n    a.blk.1.ffn_norm_1.weight            F32     [1024]           \n    a.blk.1.ffn_post_norm.weight         F32     [1024]           \n    a.blk.1.ffn_post_norm_1.weight       F32     [1024]           \n    a.blk.1.ffn_up.input_max             F32     [1]              \n    a.blk.1.ffn_up.input_min             F32     [1]              \n    a.blk.1.ffn_up.output_max            F32     [1]              \n    a.blk.1.ffn_up.output_min            F32     [1]              \n    a.blk.1.ffn_up.weight                BF16    [1024 4096]      \n    a.blk.1.ffn_up_1.input_max           F32     [1]              \n    a.blk.1.ffn_up_1.input_min           F32     [1]              \n    a.blk.1.ffn_up_1.output_max          F32     [1]              \n    a.blk.1.ffn_up_1.output_min          F32     [1]              \n    a.blk.1.ffn_up_1.weight              BF16    [1024 4096]      \n    a.blk.1.layer_pre_norm.weight        F32     [1024]           \n    a.blk.1.linear_pos.weight            BF16    [1024 1024]      \n    a.blk.1.ln1.weight                   F32     [1024]           \n    a.blk.1.ln2.weight                   F32     [1024]           \n    a.blk.1.norm_conv.weight             F32     [1024]           \n    a.blk.1.per_dim_scale.weight         F32     [128]            \n    a.blk.10.attn_k.input_max            F32     [1]              \n    a.blk.10.attn_k.input_min            F32     [1]              \n    a.blk.10.attn_k.output_max           F32     [1]              \n    a.blk.10.attn_k.output_min           F32     [1]              \n    a.blk.10.attn_k.weight               BF16    [1024 1024]      \n    a.blk.10.attn_out.input_max          F32     [1]              \n    a.blk.10.attn_out.input_min          F32     [1]              \n    a.blk.10.attn_out.output_max         F32     [1]              \n    a.blk.10.attn_out.output_min         F32     [1]              \n    a.blk.10.attn_out.weight             BF16    [1024 1024]      \n    a.blk.10.attn_q.input_max            F32     [1]              \n    a.blk.10.attn_q.input_min            F32     [1]              \n    a.blk.10.attn_q.output_max           F32     [1]              \n    a.blk.10.attn_q.output_min           F32     [1]              \n    a.blk.10.attn_q.weight               BF16    [1024 1024]      \n    a.blk.10.attn_v.input_max            F32     [1]              \n    a.blk.10.attn_v.input_min            F32     [1]              \n    a.blk.10.attn_v.output_max           F32     [1]              \n    a.blk.10.attn_v.output_min           F32     [1]              \n    a.blk.10.attn_v.weight               BF16    [1024 1024]      \n    a.blk.10.conv_dw.weight              F32     [5 1024]         \n    a.blk.10.conv_norm.weight            F32     [1024]           \n    a.blk.10.conv_pw1.input_max          F32     [1]              \n    a.blk.10.conv_pw1.input_min          F32     [1]              \n    a.blk.10.conv_pw1.output_max         F32     [1]              \n    a.blk.10.conv_pw1.output_min         F32     [1]              \n    a.blk.10.conv_pw1.weight             BF16    [1024 2048]      \n    a.blk.10.conv_pw2.input_max          F32     [1]              \n    a.blk.10.conv_pw2.input_min          F32     [1]              \n    a.blk.10.conv_pw2.output_max         F32     [1]              \n    a.blk.10.conv_pw2.output_min         F32     [1]              \n    a.blk.10.conv_pw2.weight             BF16    [1024 1024]      \n    a.blk.10.ffn_down.input_max          F32     [1]              \n    a.blk.10.ffn_down.input_min          F32     [1]              \n    a.blk.10.ffn_down.output_max         F32     [1]              \n    a.blk.10.ffn_down.output_min         F32     [1]              \n    a.blk.10.ffn_down.weight             BF16    [4096 1024]      \n    a.blk.10.ffn_down_1.input_max        F32     [1]              \n    a.blk.10.ffn_down_1.input_min        F32     [1]              \n    a.blk.10.ffn_down_1.output_max       F32     [1]              \n    a.blk.10.ffn_down_1.output_min       F32     [1]              \n    a.blk.10.ffn_down_1.weight           BF16    [4096 1024]      \n    a.blk.10.ffn_norm.weight             F32     [1024]           \n    a.blk.10.ffn_norm_1.weight           F32     [1024]           \n    a.blk.10.ffn_post_norm.weight        F32     [1024]           \n    a.blk.10.ffn_post_norm_1.weight      F32     [1024]           \n    a.blk.10.ffn_up.input_max            F32     [1]              \n    a.blk.10.ffn_up.input_min            F32     [1]              \n    a.blk.10.ffn_up.output_max           F32     [1]              \n    a.blk.10.ffn_up.output_min           F32     [1]              \n    a.blk.10.ffn_up.weight               BF16    [1024 4096]      \n    a.blk.10.ffn_up_1.input_max          F32     [1]              \n    a.blk.10.ffn_up_1.input_min          F32     [1]              \n    a.blk.10.ffn_up_1.output_max         F32     [1]              \n    a.blk.10.ffn_up_1.output_min         F32     [1]              \n    a.blk.10.ffn_up_1.weight             BF16    [1024 4096]      \n    a.blk.10.layer_pre_norm.weight       F32     [1024]           \n    a.blk.10.linear_pos.weight           BF16    [1024 1024]      \n    a.blk.10.ln1.weight                  F32     [1024]           \n    a.blk.10.ln2.weight                  F32     [1024]           \n    a.blk.10.norm_conv.weight            F32     [1024]           \n    a.blk.10.per_dim_scale.weight        F32     [128]            \n    a.blk.11.attn_k.input_max            F32     [1]              \n    a.blk.11.attn_k.input_min            F32     [1]              \n    a.blk.11.attn_k.output_max           F32     [1]              \n    a.blk.11.attn_k.output_min           F32     [1]              \n    a.blk.11.attn_k.weight               BF16    [1024 1024]      \n    a.blk.11.attn_out.input_max          F32     [1]              \n    a.blk.11.attn_out.input_min          F32     [1]              \n    a.blk.11.attn_out.output_max         F32     [1]              \n    a.blk.11.attn_out.output_min         F32     [1]              \n    a.blk.11.attn_out.weight             BF16    [1024 1024]      \n    a.blk.11.attn_q.input_max            F32     [1]              \n    a.blk.11.attn_q.input_min            F32     [1]              \n    a.blk.11.attn_q.output_max           F32     [1]              \n    a.blk.11.attn_q.output_min           F32     [1]              \n    a.blk.11.attn_q.weight               BF16    [1024 1024]      \n    a.blk.11.attn_v.input_max            F32     [1]              \n    a.blk.11.attn_v.input_min            F32     [1]              \n    a.blk.11.attn_v.output_max           F32     [1]              \n    a.blk.11.attn_v.output_min           F32     [1]              \n    a.blk.11.attn_v.weight               BF16    [1024 1024]      \n    a.blk.11.conv_dw.weight              F32     [5 1024]         \n    a.blk.11.conv_norm.weight            F32     [1024]           \n    a.blk.11.conv_pw1.input_max          F32     [1]              \n    a.blk.11.conv_pw1.input_min          F32     [1]              \n    a.blk.11.conv_pw1.output_max         F32     [1]              \n    a.blk.11.conv_pw1.output_min         F32     [1]              \n    a.blk.11.conv_pw1.weight             BF16    [1024 2048]      \n    a.blk.11.conv_pw2.input_max          F32     [1]              \n    a.blk.11.conv_pw2.input_min          F32     [1]              \n    a.blk.11.conv_pw2.output_max         F32     [1]              \n    a.blk.11.conv_pw2.output_min         F32     [1]              \n    a.blk.11.conv_pw2.weight             BF16    [1024 1024]      \n    a.blk.11.ffn_down.input_max          F32     [1]              \n    a.blk.11.ffn_down.input_min          F32     [1]              \n    a.blk.11.ffn_down.output_max         F32     [1]              \n    a.blk.11.ffn_down.output_min         F32     [1]              \n    a.blk.11.ffn_down.weight             BF16    [4096 1024]      \n    a.blk.11.ffn_down_1.input_max        F32     [1]              \n    a.blk.11.ffn_down_1.input_min        F32     [1]              \n    a.blk.11.ffn_down_1.output_max       F32     [1]              \n    a.blk.11.ffn_down_1.output_min       F32     [1]              \n    a.blk.11.ffn_down_1.weight           BF16    [4096 1024]      \n    a.blk.11.ffn_norm.weight             F32     [1024]           \n    a.blk.11.ffn_norm_1.weight           F32     [1024]           \n    a.blk.11.ffn_post_norm.weight        F32     [1024]           \n    a.blk.11.ffn_post_norm_1.weight      F32     [1024]           \n    a.blk.11.ffn_up.input_max            F32     [1]              \n    a.blk.11.ffn_up.input_min            F32     [1]              \n    a.blk.11.ffn_up.output_max           F32     [1]              \n    a.blk.11.ffn_up.output_min           F32     [1]              \n    a.blk.11.ffn_up.weight               BF16    [1024 4096]      \n    a.blk.11.ffn_up_1.input_max          F32     [1]              \n    a.blk.11.ffn_up_1.input_min          F32     [1]              \n    a.blk.11.ffn_up_1.output_max         F32     [1]              \n    a.blk.11.ffn_up_1.output_min         F32     [1]              \n    a.blk.11.ffn_up_1.weight             BF16    [1024 4096]      \n    a.blk.11.layer_pre_norm.weight       F32     [1024]           \n    a.blk.11.linear_pos.weight           BF16    [1024 1024]      \n    a.blk.11.ln1.weight                  F32     [1024]           \n    a.blk.11.ln2.weight                  F32     [1024]           \n    a.blk.11.norm_conv.weight            F32     [1024]           \n    a.blk.11.per_dim_scale.weight        F32     [128]            \n    a.blk.2.attn_k.input_max             F32     [1]              \n    a.blk.2.attn_k.input_min             F32     [1]              \n    a.blk.2.attn_k.output_max            F32     [1]              \n    a.blk.2.attn_k.output_min            F32     [1]              \n    a.blk.2.attn_k.weight                BF16    [1024 1024]      \n    a.blk.2.attn_out.input_max           F32     [1]              \n    a.blk.2.attn_out.input_min           F32     [1]              \n    a.blk.2.attn_out.output_max          F32     [1]              \n    a.blk.2.attn_out.output_min          F32     [1]              \n    a.blk.2.attn_out.weight              BF16    [1024 1024]      \n    a.blk.2.attn_q.input_max             F32     [1]              \n    a.blk.2.attn_q.input_min             F32     [1]              \n    a.blk.2.attn_q.output_max            F32     [1]              \n    a.blk.2.attn_q.output_min            F32     [1]              \n    a.blk.2.attn_q.weight                BF16    [1024 1024]      \n    a.blk.2.attn_v.input_max             F32     [1]              \n    a.blk.2.attn_v.input_min             F32     [1]              \n    a.blk.2.attn_v.output_max            F32     [1]              \n    a.blk.2.attn_v.output_min            F32     [1]              \n    a.blk.2.attn_v.weight                BF16    [1024 1024]      \n    a.blk.2.conv_dw.weight               F32     [5 1024]         \n    a.blk.2.conv_norm.weight             F32     [1024]           \n    a.blk.2.conv_pw1.input_max           F32     [1]              \n    a.blk.2.conv_pw1.input_min           F32     [1]              \n    a.blk.2.conv_pw1.output_max          F32     [1]              \n    a.blk.2.conv_pw1.output_min          F32     [1]              \n    a.blk.2.conv_pw1.weight              BF16    [1024 2048]      \n    a.blk.2.conv_pw2.input_max           F32     [1]              \n    a.blk.2.conv_pw2.input_min           F32     [1]              \n    a.blk.2.conv_pw2.output_max          F32     [1]              \n    a.blk.2.conv_pw2.output_min          F32     [1]              \n    a.blk.2.conv_pw2.weight              BF16    [1024 1024]      \n    a.blk.2.ffn_down.input_max           F32     [1]              \n    a.blk.2.ffn_down.input_min           F32     [1]              \n    a.blk.2.ffn_down.output_max          F32     [1]              \n    a.blk.2.ffn_down.output_min          F32     [1]              \n    a.blk.2.ffn_down.weight              BF16    [4096 1024]      \n    a.blk.2.ffn_down_1.input_max         F32     [1]              \n    a.blk.2.ffn_down_1.input_min         F32     [1]              \n    a.blk.2.ffn_down_1.output_max        F32     [1]              \n    a.blk.2.ffn_down_1.output_min        F32     [1]              \n    a.blk.2.ffn_down_1.weight            BF16    [4096 1024]      \n    a.blk.2.ffn_norm.weight              F32     [1024]           \n    a.blk.2.ffn_norm_1.weight            F32     [1024]           \n    a.blk.2.ffn_post_norm.weight         F32     [1024]           \n    a.blk.2.ffn_post_norm_1.weight       F32     [1024]           \n    a.blk.2.ffn_up.input_max             F32     [1]              \n    a.blk.2.ffn_up.input_min             F32     [1]              \n    a.blk.2.ffn_up.output_max            F32     [1]              \n    a.blk.2.ffn_up.output_min            F32     [1]              \n    a.blk.2.ffn_up.weight                BF16    [1024 4096]      \n    a.blk.2.ffn_up_1.input_max           F32     [1]              \n    a.blk.2.ffn_up_1.input_min           F32     [1]              \n    a.blk.2.ffn_up_1.output_max          F32     [1]              \n    a.blk.2.ffn_up_1.output_min          F32     [1]              \n    a.blk.2.ffn_up_1.weight              BF16    [1024 4096]      \n    a.blk.2.layer_pre_norm.weight        F32     [1024]           \n    a.blk.2.linear_pos.weight            BF16    [1024 1024]      \n    a.blk.2.ln1.weight                   F32     [1024]           \n    a.blk.2.ln2.weight                   F32     [1024]           \n    a.blk.2.norm_conv.weight             F32     [1024]           \n    a.blk.2.per_dim_scale.weight         F32     [128]            \n    a.blk.3.attn_k.input_max             F32     [1]              \n    a.blk.3.attn_k.input_min             F32     [1]              \n    a.blk.3.attn_k.output_max            F32     [1]              \n    a.blk.3.attn_k.output_min            F32     [1]              \n    a.blk.3.attn_k.weight                BF16    [1024 1024]      \n    a.blk.3.attn_out.input_max           F32     [1]              \n    a.blk.3.attn_out.input_min           F32     [1]              \n    a.blk.3.attn_out.output_max          F32     [1]              \n    a.blk.3.attn_out.output_min          F32     [1]              \n    a.blk.3.attn_out.weight              BF16    [1024 1024]      \n    a.blk.3.attn_q.input_max             F32     [1]              \n    a.blk.3.attn_q.input_min             F32     [1]              \n    a.blk.3.attn_q.output_max            F32     [1]              \n    a.blk.3.attn_q.output_min            F32     [1]              \n    a.blk.3.attn_q.weight                BF16    [1024 1024]      \n    a.blk.3.attn_v.input_max             F32     [1]              \n    a.blk.3.attn_v.input_min             F32     [1]              \n    a.blk.3.attn_v.output_max            F32     [1]              \n    a.blk.3.attn_v.output_min            F32     [1]              \n    a.blk.3.attn_v.weight                BF16    [1024 1024]      \n    a.blk.3.conv_dw.weight               F32     [5 1024]         \n    a.blk.3.conv_norm.weight             F32     [1024]           \n    a.blk.3.conv_pw1.input_max           F32     [1]              \n    a.blk.3.conv_pw1.input_min           F32     [1]              \n    a.blk.3.conv_pw1.output_max          F32     [1]              \n    a.blk.3.conv_pw1.output_min          F32     [1]              \n    a.blk.3.conv_pw1.weight              BF16    [1024 2048]      \n    a.blk.3.conv_pw2.input_max           F32     [1]              \n    a.blk.3.conv_pw2.input_min           F32     [1]              \n    a.blk.3.conv_pw2.output_max          F32     [1]              \n    a.blk.3.conv_pw2.output_min          F32     [1]              \n    a.blk.3.conv_pw2.weight              BF16    [1024 1024]      \n    a.blk.3.ffn_down.input_max           F32     [1]              \n    a.blk.3.ffn_down.input_min           F32     [1]              \n    a.blk.3.ffn_down.output_max          F32     [1]              \n    a.blk.3.ffn_down.output_min          F32     [1]              \n    a.blk.3.ffn_down.weight              BF16    [4096 1024]      \n    a.blk.3.ffn_down_1.input_max         F32     [1]              \n    a.blk.3.ffn_down_1.input_min         F32     [1]              \n    a.blk.3.ffn_down_1.output_max        F32     [1]              \n    a.blk.3.ffn_down_1.output_min        F32     [1]              \n    a.blk.3.ffn_down_1.weight            BF16    [4096 1024]      \n    a.blk.3.ffn_norm.weight              F32     [1024]           \n    a.blk.3.ffn_norm_1.weight            F32     [1024]           \n    a.blk.3.ffn_post_norm.weight         F32     [1024]           \n    a.blk.3.ffn_post_norm_1.weight       F32     [1024]           \n    a.blk.3.ffn_up.input_max             F32     [1]              \n    a.blk.3.ffn_up.input_min             F32     [1]              \n    a.blk.3.ffn_up.output_max            F32     [1]              \n    a.blk.3.ffn_up.output_min            F32     [1]              \n    a.blk.3.ffn_up.weight                BF16    [1024 4096]      \n    a.blk.3.ffn_up_1.input_max           F32     [1]              \n    a.blk.3.ffn_up_1.input_min           F32     [1]              \n    a.blk.3.ffn_up_1.output_max          F32     [1]              \n    a.blk.3.ffn_up_1.output_min          F32     [1]              \n    a.blk.3.ffn_up_1.weight              BF16    [1024 4096]      \n    a.blk.3.layer_pre_norm.weight        F32     [1024]           \n    a.blk.3.linear_pos.weight            BF16    [1024 1024]      \n    a.blk.3.ln1.weight                   F32     [1024]           \n    a.blk.3.ln2.weight                   F32     [1024]           \n    a.blk.3.norm_conv.weight             F32     [1024]           \n    a.blk.3.per_dim_scale.weight         F32     [128]            \n    a.blk.4.attn_k.input_max             F32     [1]              \n    a.blk.4.attn_k.input_min             F32     [1]              \n    a.blk.4.attn_k.output_max            F32     [1]              \n    a.blk.4.attn_k.output_min            F32     [1]              \n    a.blk.4.attn_k.weight                BF16    [1024 1024]      \n    a.blk.4.attn_out.input_max           F32     [1]              \n    a.blk.4.attn_out.input_min           F32     [1]              \n    a.blk.4.attn_out.output_max          F32     [1]              \n    a.blk.4.attn_out.output_min          F32     [1]              \n    a.blk.4.attn_out.weight              BF16    [1024 1024]      \n    a.blk.4.attn_q.input_max             F32     [1]              \n    a.blk.4.attn_q.input_min             F32     [1]              \n    a.blk.4.attn_q.output_max            F32     [1]              \n    a.blk.4.attn_q.output_min            F32     [1]              \n    a.blk.4.attn_q.weight                BF16    [1024 1024]      \n    a.blk.4.attn_v.input_max             F32     [1]              \n    a.blk.4.attn_v.input_min             F32     [1]              \n    a.blk.4.attn_v.output_max            F32     [1]              \n    a.blk.4.attn_v.output_min            F32     [1]              \n    a.blk.4.attn_v.weight                BF16    [1024 1024]      \n    a.blk.4.conv_dw.weight               F32     [5 1024]         \n    a.blk.4.conv_norm.weight             F32     [1024]           \n    a.blk.4.conv_pw1.input_max           F32     [1]              \n    a.blk.4.conv_pw1.input_min           F32     [1]              \n    a.blk.4.conv_pw1.output_max          F32     [1]              \n    a.blk.4.conv_pw1.output_min          F32     [1]              \n    a.blk.4.conv_pw1.weight              BF16    [1024 2048]      \n    a.blk.4.conv_pw2.input_max           F32     [1]              \n    a.blk.4.conv_pw2.input_min           F32     [1]              \n    a.blk.4.conv_pw2.output_max          F32     [1]              \n    a.blk.4.conv_pw2.output_min          F32     [1]              \n    a.blk.4.conv_pw2.weight              BF16    [1024 1024]      \n    a.blk.4.ffn_down.input_max           F32     [1]              \n    a.blk.4.ffn_down.input_min           F32     [1]              \n    a.blk.4.ffn_down.output_max          F32     [1]              \n    a.blk.4.ffn_down.output_min          F32     [1]              \n    a.blk.4.ffn_down.weight              BF16    [4096 1024]      \n    a.blk.4.ffn_down_1.input_max         F32     [1]              \n    a.blk.4.ffn_down_1.input_min         F32     [1]              \n    a.blk.4.ffn_down_1.output_max        F32     [1]              \n    a.blk.4.ffn_down_1.output_min        F32     [1]              \n    a.blk.4.ffn_down_1.weight            BF16    [4096 1024]      \n    a.blk.4.ffn_norm.weight              F32     [1024]           \n    a.blk.4.ffn_norm_1.weight            F32     [1024]           \n    a.blk.4.ffn_post_norm.weight         F32     [1024]           \n    a.blk.4.ffn_post_norm_1.weight       F32     [1024]           \n    a.blk.4.ffn_up.input_max             F32     [1]              \n    a.blk.4.ffn_up.input_min             F32     [1]              \n    a.blk.4.ffn_up.output_max            F32     [1]              \n    a.blk.4.ffn_up.output_min            F32     [1]              \n    a.blk.4.ffn_up.weight                BF16    [1024 4096]      \n    a.blk.4.ffn_up_1.input_max           F32     [1]              \n    a.blk.4.ffn_up_1.input_min           F32     [1]              \n    a.blk.4.ffn_up_1.output_max          F32     [1]              \n    a.blk.4.ffn_up_1.output_min          F32     [1]              \n    a.blk.4.ffn_up_1.weight              BF16    [1024 4096]      \n    a.blk.4.layer_pre_norm.weight        F32     [1024]           \n    a.blk.4.linear_pos.weight            BF16    [1024 1024]      \n    a.blk.4.ln1.weight                   F32     [1024]           \n    a.blk.4.ln2.weight                   F32     [1024]           \n    a.blk.4.norm_conv.weight             F32     [1024]           \n    a.blk.4.per_dim_scale.weight         F32     [128]            \n    a.blk.5.attn_k.input_max             F32     [1]              \n    a.blk.5.attn_k.input_min             F32     [1]              \n    a.blk.5.attn_k.output_max            F32     [1]              \n    a.blk.5.attn_k.output_min            F32     [1]              \n    a.blk.5.attn_k.weight                BF16    [1024 1024]      \n    a.blk.5.attn_out.input_max           F32     [1]              \n    a.blk.5.attn_out.input_min           F32     [1]              \n    a.blk.5.attn_out.output_max          F32     [1]              \n    a.blk.5.attn_out.output_min          F32     [1]              \n    a.blk.5.attn_out.weight              BF16    [1024 1024]      \n    a.blk.5.attn_q.input_max             F32     [1]              \n    a.blk.5.attn_q.input_min             F32     [1]              \n    a.blk.5.attn_q.output_max            F32     [1]              \n    a.blk.5.attn_q.output_min            F32     [1]              \n    a.blk.5.attn_q.weight                BF16    [1024 1024]      \n    a.blk.5.attn_v.input_max             F32     [1]              \n    a.blk.5.attn_v.input_min             F32     [1]              \n    a.blk.5.attn_v.output_max            F32     [1]              \n    a.blk.5.attn_v.output_min            F32     [1]              \n    a.blk.5.attn_v.weight                BF16    [1024 1024]      \n    a.blk.5.conv_dw.weight               F32     [5 1024]         \n    a.blk.5.conv_norm.weight             F32     [1024]           \n    a.blk.5.conv_pw1.input_max           F32     [1]              \n    a.blk.5.conv_pw1.input_min           F32     [1]              \n    a.blk.5.conv_pw1.output_max          F32     [1]              \n    a.blk.5.conv_pw1.output_min          F32     [1]              \n    a.blk.5.conv_pw1.weight              BF16    [1024 2048]      \n    a.blk.5.conv_pw2.input_max           F32     [1]              \n    a.blk.5.conv_pw2.input_min           F32     [1]              \n    a.blk.5.conv_pw2.output_max          F32     [1]              \n    a.blk.5.conv_pw2.output_min          F32     [1]              \n    a.blk.5.conv_pw2.weight              BF16    [1024 1024]      \n    a.blk.5.ffn_down.input_max           F32     [1]              \n    a.blk.5.ffn_down.input_min           F32     [1]              \n    a.blk.5.ffn_down.output_max          F32     [1]              \n    a.blk.5.ffn_down.output_min          F32     [1]              \n    a.blk.5.ffn_down.weight              BF16    [4096 1024]      \n    a.blk.5.ffn_down_1.input_max         F32     [1]              \n    a.blk.5.ffn_down_1.input_min         F32     [1]              \n    a.blk.5.ffn_down_1.output_max        F32     [1]              \n    a.blk.5.ffn_down_1.output_min        F32     [1]              \n    a.blk.5.ffn_down_1.weight            BF16    [4096 1024]      \n    a.blk.5.ffn_norm.weight              F32     [1024]           \n    a.blk.5.ffn_norm_1.weight            F32     [1024]           \n    a.blk.5.ffn_post_norm.weight         F32     [1024]           \n    a.blk.5.ffn_post_norm_1.weight       F32     [1024]           \n    a.blk.5.ffn_up.input_max             F32     [1]              \n    a.blk.5.ffn_up.input_min             F32     [1]              \n    a.blk.5.ffn_up.output_max            F32     [1]              \n    a.blk.5.ffn_up.output_min            F32     [1]              \n    a.blk.5.ffn_up.weight                BF16    [1024 4096]      \n    a.blk.5.ffn_up_1.input_max           F32     [1]              \n    a.blk.5.ffn_up_1.input_min           F32     [1]              \n    a.blk.5.ffn_up_1.output_max          F32     [1]              \n    a.blk.5.ffn_up_1.output_min          F32     [1]              \n    a.blk.5.ffn_up_1.weight              BF16    [1024 4096]      \n    a.blk.5.layer_pre_norm.weight        F32     [1024]           \n    a.blk.5.linear_pos.weight            BF16    [1024 1024]      \n    a.blk.5.ln1.weight                   F32     [1024]           \n    a.blk.5.ln2.weight                   F32     [1024]           \n    a.blk.5.norm_conv.weight             F32     [1024]           \n    a.blk.5.per_dim_scale.weight         F32     [128]            \n    a.blk.6.attn_k.input_max             F32     [1]              \n    a.blk.6.attn_k.input_min             F32     [1]              \n    a.blk.6.attn_k.output_max            F32     [1]              \n    a.blk.6.attn_k.output_min            F32     [1]              \n    a.blk.6.attn_k.weight                BF16    [1024 1024]      \n    a.blk.6.attn_out.input_max           F32     [1]              \n    a.blk.6.attn_out.input_min           F32     [1]              \n    a.blk.6.attn_out.output_max          F32     [1]              \n    a.blk.6.attn_out.output_min          F32     [1]              \n    a.blk.6.attn_out.weight              BF16    [1024 1024]      \n    a.blk.6.attn_q.input_max             F32     [1]              \n    a.blk.6.attn_q.input_min             F32     [1]              \n    a.blk.6.attn_q.output_max            F32     [1]              \n    a.blk.6.attn_q.output_min            F32     [1]              \n    a.blk.6.attn_q.weight                BF16    [1024 1024]      \n    a.blk.6.attn_v.input_max             F32     [1]              \n    a.blk.6.attn_v.input_min             F32     [1]              \n    a.blk.6.attn_v.output_max            F32     [1]              \n    a.blk.6.attn_v.output_min            F32     [1]              \n    a.blk.6.attn_v.weight                BF16    [1024 1024]      \n    a.blk.6.conv_dw.weight               F32     [5 1024]         \n    a.blk.6.conv_norm.weight             F32     [1024]           \n    a.blk.6.conv_pw1.input_max           F32     [1]              \n    a.blk.6.conv_pw1.input_min           F32     [1]              \n    a.blk.6.conv_pw1.output_max          F32     [1]              \n    a.blk.6.conv_pw1.output_min          F32     [1]              \n    a.blk.6.conv_pw1.weight              BF16    [1024 2048]      \n    a.blk.6.conv_pw2.input_max           F32     [1]              \n    a.blk.6.conv_pw2.input_min           F32     [1]              \n    a.blk.6.conv_pw2.output_max          F32     [1]              \n    a.blk.6.conv_pw2.output_min          F32     [1]              \n    a.blk.6.conv_pw2.weight              BF16    [1024 1024]      \n    a.blk.6.ffn_down.input_max           F32     [1]              \n    a.blk.6.ffn_down.input_min           F32     [1]              \n    a.blk.6.ffn_down.output_max          F32     [1]              \n    a.blk.6.ffn_down.output_min          F32     [1]              \n    a.blk.6.ffn_down.weight              BF16    [4096 1024]      \n    a.blk.6.ffn_down_1.input_max         F32     [1]              \n    a.blk.6.ffn_down_1.input_min         F32     [1]              \n    a.blk.6.ffn_down_1.output_max        F32     [1]              \n    a.blk.6.ffn_down_1.output_min        F32     [1]              \n    a.blk.6.ffn_down_1.weight            BF16    [4096 1024]      \n    a.blk.6.ffn_norm.weight              F32     [1024]           \n    a.blk.6.ffn_norm_1.weight            F32     [1024]           \n    a.blk.6.ffn_post_norm.weight         F32     [1024]           \n    a.blk.6.ffn_post_norm_1.weight       F32     [1024]           \n    a.blk.6.ffn_up.input_max             F32     [1]              \n    a.blk.6.ffn_up.input_min             F32     [1]              \n    a.blk.6.ffn_up.output_max            F32     [1]              \n    a.blk.6.ffn_up.output_min            F32     [1]              \n    a.blk.6.ffn_up.weight                BF16    [1024 4096]      \n    a.blk.6.ffn_up_1.input_max           F32     [1]              \n    a.blk.6.ffn_up_1.input_min           F32     [1]              \n    a.blk.6.ffn_up_1.output_max          F32     [1]              \n    a.blk.6.ffn_up_1.output_min          F32     [1]              \n    a.blk.6.ffn_up_1.weight              BF16    [1024 4096]      \n    a.blk.6.layer_pre_norm.weight        F32     [1024]           \n    a.blk.6.linear_pos.weight            BF16    [1024 1024]      \n    a.blk.6.ln1.weight                   F32     [1024]           \n    a.blk.6.ln2.weight                   F32     [1024]           \n    a.blk.6.norm_conv.weight             F32     [1024]           \n    a.blk.6.per_dim_scale.weight         F32     [128]            \n    a.blk.7.attn_k.input_max             F32     [1]              \n    a.blk.7.attn_k.input_min             F32     [1]              \n    a.blk.7.attn_k.output_max            F32     [1]              \n    a.blk.7.attn_k.output_min            F32     [1]              \n    a.blk.7.attn_k.weight                BF16    [1024 1024]      \n    a.blk.7.attn_out.input_max           F32     [1]              \n    a.blk.7.attn_out.input_min           F32     [1]              \n    a.blk.7.attn_out.output_max          F32     [1]              \n    a.blk.7.attn_out.output_min          F32     [1]              \n    a.blk.7.attn_out.weight              BF16    [1024 1024]      \n    a.blk.7.attn_q.input_max             F32     [1]              \n    a.blk.7.attn_q.input_min             F32     [1]              \n    a.blk.7.attn_q.output_max            F32     [1]              \n    a.blk.7.attn_q.output_min            F32     [1]              \n    a.blk.7.attn_q.weight                BF16    [1024 1024]      \n    a.blk.7.attn_v.input_max             F32     [1]              \n    a.blk.7.attn_v.input_min             F32     [1]              \n    a.blk.7.attn_v.output_max            F32     [1]              \n    a.blk.7.attn_v.output_min            F32     [1]              \n    a.blk.7.attn_v.weight                BF16    [1024 1024]      \n    a.blk.7.conv_dw.weight               F32     [5 1024]         \n    a.blk.7.conv_norm.weight             F32     [1024]           \n    a.blk.7.conv_pw1.input_max           F32     [1]              \n    a.blk.7.conv_pw1.input_min           F32     [1]              \n    a.blk.7.conv_pw1.output_max          F32     [1]              \n    a.blk.7.conv_pw1.output_min          F32     [1]              \n    a.blk.7.conv_pw1.weight              BF16    [1024 2048]      \n    a.blk.7.conv_pw2.input_max           F32     [1]              \n    a.blk.7.conv_pw2.input_min           F32     [1]              \n    a.blk.7.conv_pw2.output_max          F32     [1]              \n    a.blk.7.conv_pw2.output_min          F32     [1]              \n    a.blk.7.conv_pw2.weight              BF16    [1024 1024]      \n    a.blk.7.ffn_down.input_max           F32     [1]              \n    a.blk.7.ffn_down.input_min           F32     [1]              \n    a.blk.7.ffn_down.output_max          F32     [1]              \n    a.blk.7.ffn_down.output_min          F32     [1]              \n    a.blk.7.ffn_down.weight              BF16    [4096 1024]      \n    a.blk.7.ffn_down_1.input_max         F32     [1]              \n    a.blk.7.ffn_down_1.input_min         F32     [1]              \n    a.blk.7.ffn_down_1.output_max        F32     [1]              \n    a.blk.7.ffn_down_1.output_min        F32     [1]              \n    a.blk.7.ffn_down_1.weight            BF16    [4096 1024]      \n    a.blk.7.ffn_norm.weight              F32     [1024]           \n    a.blk.7.ffn_norm_1.weight            F32     [1024]           \n    a.blk.7.ffn_post_norm.weight         F32     [1024]           \n    a.blk.7.ffn_post_norm_1.weight       F32     [1024]           \n    a.blk.7.ffn_up.input_max             F32     [1]              \n    a.blk.7.ffn_up.input_min             F32     [1]              \n    a.blk.7.ffn_up.output_max            F32     [1]              \n    a.blk.7.ffn_up.output_min            F32     [1]              \n    a.blk.7.ffn_up.weight                BF16    [1024 4096]      \n    a.blk.7.ffn_up_1.input_max           F32     [1]              \n    a.blk.7.ffn_up_1.input_min           F32     [1]              \n    a.blk.7.ffn_up_1.output_max          F32     [1]              \n    a.blk.7.ffn_up_1.output_min          F32     [1]              \n    a.blk.7.ffn_up_1.weight              BF16    [1024 4096]      \n    a.blk.7.layer_pre_norm.weight        F32     [1024]           \n    a.blk.7.linear_pos.weight            BF16    [1024 1024]      \n    a.blk.7.ln1.weight                   F32     [1024]           \n    a.blk.7.ln2.weight                   F32     [1024]           \n    a.blk.7.norm_conv.weight             F32     [1024]           \n    a.blk.7.per_dim_scale.weight         F32     [128]            \n    a.blk.8.attn_k.input_max             F32     [1]              \n    a.blk.8.attn_k.input_min             F32     [1]              \n    a.blk.8.attn_k.output_max            F32     [1]              \n    a.blk.8.attn_k.output_min            F32     [1]              \n    a.blk.8.attn_k.weight                BF16    [1024 1024]      \n    a.blk.8.attn_out.input_max           F32     [1]              \n    a.blk.8.attn_out.input_min           F32     [1]              \n    a.blk.8.attn_out.output_max          F32     [1]              \n    a.blk.8.attn_out.output_min          F32     [1]              \n    a.blk.8.attn_out.weight              BF16    [1024 1024]      \n    a.blk.8.attn_q.input_max             F32     [1]              \n    a.blk.8.attn_q.input_min             F32     [1]              \n    a.blk.8.attn_q.output_max            F32     [1]              \n    a.blk.8.attn_q.output_min            F32     [1]              \n    a.blk.8.attn_q.weight                BF16    [1024 1024]      \n    a.blk.8.attn_v.input_max             F32     [1]              \n    a.blk.8.attn_v.input_min             F32     [1]              \n    a.blk.8.attn_v.output_max            F32     [1]              \n    a.blk.8.attn_v.output_min            F32     [1]              \n    a.blk.8.attn_v.weight                BF16    [1024 1024]      \n    a.blk.8.conv_dw.weight               F32     [5 1024]         \n    a.blk.8.conv_norm.weight             F32     [1024]           \n    a.blk.8.conv_pw1.input_max           F32     [1]              \n    a.blk.8.conv_pw1.input_min           F32     [1]              \n    a.blk.8.conv_pw1.output_max          F32     [1]              \n    a.blk.8.conv_pw1.output_min          F32     [1]              \n    a.blk.8.conv_pw1.weight              BF16    [1024 2048]      \n    a.blk.8.conv_pw2.input_max           F32     [1]              \n    a.blk.8.conv_pw2.input_min           F32     [1]              \n    a.blk.8.conv_pw2.output_max          F32     [1]              \n    a.blk.8.conv_pw2.output_min          F32     [1]              \n    a.blk.8.conv_pw2.weight              BF16    [1024 1024]      \n    a.blk.8.ffn_down.input_max           F32     [1]              \n    a.blk.8.ffn_down.input_min           F32     [1]              \n    a.blk.8.ffn_down.output_max          F32     [1]              \n    a.blk.8.ffn_down.output_min          F32     [1]              \n    a.blk.8.ffn_down.weight              BF16    [4096 1024]      \n    a.blk.8.ffn_down_1.input_max         F32     [1]              \n    a.blk.8.ffn_down_1.input_min         F32     [1]              \n    a.blk.8.ffn_down_1.output_max        F32     [1]              \n    a.blk.8.ffn_down_1.output_min        F32     [1]              \n    a.blk.8.ffn_down_1.weight            BF16    [4096 1024]      \n    a.blk.8.ffn_norm.weight              F32     [1024]           \n    a.blk.8.ffn_norm_1.weight            F32     [1024]           \n    a.blk.8.ffn_post_norm.weight         F32     [1024]           \n    a.blk.8.ffn_post_norm_1.weight       F32     [1024]           \n    a.blk.8.ffn_up.input_max             F32     [1]              \n    a.blk.8.ffn_up.input_min             F32     [1]              \n    a.blk.8.ffn_up.output_max            F32     [1]              \n    a.blk.8.ffn_up.output_min            F32     [1]              \n    a.blk.8.ffn_up.weight                BF16    [1024 4096]      \n    a.blk.8.ffn_up_1.input_max           F32     [1]              \n    a.blk.8.ffn_up_1.input_min           F32     [1]              \n    a.blk.8.ffn_up_1.output_max          F32     [1]              \n    a.blk.8.ffn_up_1.output_min          F32     [1]              \n    a.blk.8.ffn_up_1.weight              BF16    [1024 4096]      \n    a.blk.8.layer_pre_norm.weight        F32     [1024]           \n    a.blk.8.linear_pos.weight            BF16    [1024 1024]      \n    a.blk.8.ln1.weight                   F32     [1024]           \n    a.blk.8.ln2.weight                   F32     [1024]           \n    a.blk.8.norm_conv.weight             F32     [1024]           \n    a.blk.8.per_dim_scale.weight         F32     [128]            \n    a.blk.9.attn_k.input_max             F32     [1]              \n    a.blk.9.attn_k.input_min             F32     [1]              \n    a.blk.9.attn_k.output_max            F32     [1]              \n    a.blk.9.attn_k.output_min            F32     [1]              \n    a.blk.9.attn_k.weight                BF16    [1024 1024]      \n    a.blk.9.attn_out.input_max           F32     [1]              \n    a.blk.9.attn_out.input_min           F32     [1]              \n    a.blk.9.attn_out.output_max          F32     [1]              \n    a.blk.9.attn_out.output_min          F32     [1]              \n    a.blk.9.attn_out.weight              BF16    [1024 1024]      \n    a.blk.9.attn_q.input_max             F32     [1]              \n    a.blk.9.attn_q.input_min             F32     [1]              \n    a.blk.9.attn_q.output_max            F32     [1]              \n    a.blk.9.attn_q.output_min            F32     [1]              \n    a.blk.9.attn_q.weight                BF16    [1024 1024]      \n    a.blk.9.attn_v.input_max             F32     [1]              \n    a.blk.9.attn_v.input_min             F32     [1]              \n    a.blk.9.attn_v.output_max            F32     [1]              \n    a.blk.9.attn_v.output_min            F32     [1]              \n    a.blk.9.attn_v.weight                BF16    [1024 1024]      \n    a.blk.9.conv_dw.weight               F32     [5 1024]         \n    a.blk.9.conv_norm.weight             F32     [1024]           \n    a.blk.9.conv_pw1.input_max           F32     [1]              \n    a.blk.9.conv_pw1.input_min           F32     [1]              \n    a.blk.9.conv_pw1.output_max          F32     [1]              \n    a.blk.9.conv_pw1.output_min          F32     [1]              \n    a.blk.9.conv_pw1.weight              BF16    [1024 2048]      \n    a.blk.9.conv_pw2.input_max           F32     [1]              \n    a.blk.9.conv_pw2.input_min           F32     [1]              \n    a.blk.9.conv_pw2.output_max          F32     [1]              \n    a.blk.9.conv_pw2.output_min          F32     [1]              \n    a.blk.9.conv_pw2.weight              BF16    [1024 1024]      \n    a.blk.9.ffn_down.input_max           F32     [1]              \n    a.blk.9.ffn_down.input_min           F32     [1]              \n    a.blk.9.ffn_down.output_max          F32     [1]              \n    a.blk.9.ffn_down.output_min          F32     [1]              \n    a.blk.9.ffn_down.weight              BF16    [4096 1024]      \n    a.blk.9.ffn_down_1.input_max         F32     [1]              \n    a.blk.9.ffn_down_1.input_min         F32     [1]              \n    a.blk.9.ffn_down_1.output_max        F32     [1]              \n    a.blk.9.ffn_down_1.output_min        F32     [1]              \n    a.blk.9.ffn_down_1.weight            BF16    [4096 1024]      \n    a.blk.9.ffn_norm.weight              F32     [1024]           \n    a.blk.9.ffn_norm_1.weight            F32     [1024]           \n    a.blk.9.ffn_post_norm.weight         F32     [1024]           \n    a.blk.9.ffn_post_norm_1.weight       F32     [1024]           \n    a.blk.9.ffn_up.input_max             F32     [1]              \n    a.blk.9.ffn_up.input_min             F32     [1]              \n    a.blk.9.ffn_up.output_max            F32     [1]              \n    a.blk.9.ffn_up.output_min            F32     [1]              \n    a.blk.9.ffn_up.weight                BF16    [1024 4096]      \n    a.blk.9.ffn_up_1.input_max           F32     [1]              \n    a.blk.9.ffn_up_1.input_min           F32     [1]              \n    a.blk.9.ffn_up_1.output_max          F32     [1]              \n    a.blk.9.ffn_up_1.output_min          F32     [1]              \n    a.blk.9.ffn_up_1.weight              BF16    [1024 4096]      \n    a.blk.9.layer_pre_norm.weight        F32     [1024]           \n    a.blk.9.linear_pos.weight            BF16    [1024 1024]      \n    a.blk.9.ln1.weight                   F32     [1024]           \n    a.blk.9.ln2.weight                   F32     [1024]           \n    a.blk.9.norm_conv.weight             F32     [1024]           \n    a.blk.9.per_dim_scale.weight         F32     [128]            \n    a.conv1d.0.norm.weight               F32     [128]            \n    a.conv1d.0.weight                    F32     [3 3 1 128]      \n    a.conv1d.1.norm.weight               F32     [32]             \n    a.conv1d.1.weight                    F32     [3 3 128 32]     \n    a.pre_encode.out.weight              BF16    [1024 1024]      \n    mm.a.fc.bias                         F32     [1536]           \n    mm.a.fc.weight                       F16     [1024 1536]      \n    mm.a.input_projection.weight         F16     [1536 1536]      \n    mm.input_projection.weight           F16     [768 1536]       \n    output_norm.weight                   F32     [1536]           \n    per_layer_model_proj.weight          Q4_K    [1536 8960]      \n    per_layer_proj_norm.weight           F32     [256]            \n    per_layer_token_embd.weight          BF16    [8960 262144]    \n    rope_freqs.weight                    F32     [256]            \n    token_embd.weight                    Q6_K    [1536 262144]    \n    v.blk.0.attn_k.input_max             F32     [1]              \n    v.blk.0.attn_k.input_min             F32     [1]              \n    v.blk.0.attn_k.output_max            F32     [1]              \n    v.blk.0.attn_k.output_min            F32     [1]              \n    v.blk.0.attn_k.weight                F16     [768 768]        \n    v.blk.0.attn_k_norm.weight           F32     [64]             \n    v.blk.0.attn_out.input_max           F32     [1]              \n    v.blk.0.attn_out.input_min           F32     [1]              \n    v.blk.0.attn_out.output_max          F32     [1]              \n    v.blk.0.attn_out.output_min          F32     [1]              \n    v.blk.0.attn_out.weight              F16     [768 768]        \n    v.blk.0.attn_post_norm.weight        F32     [768]            \n    v.blk.0.attn_q.input_max             F32     [1]              \n    v.blk.0.attn_q.input_min             F32     [1]              \n    v.blk.0.attn_q.output_max            F32     [1]              \n    v.blk.0.attn_q.output_min            F32     [1]              \n    v.blk.0.attn_q.weight                F16     [768 768]        \n    v.blk.0.attn_q_norm.weight           F32     [64]             \n    v.blk.0.attn_v.input_max             F32     [1]              \n    v.blk.0.attn_v.input_min             F32     [1]              \n    v.blk.0.attn_v.output_max            F32     [1]              \n    v.blk.0.attn_v.output_min            F32     [1]              \n    v.blk.0.attn_v.weight                F16     [768 768]        \n    v.blk.0.ffn_down.input_max           F32     [1]              \n    v.blk.0.ffn_down.input_min           F32     [1]              \n    v.blk.0.ffn_down.output_max          F32     [1]              \n    v.blk.0.ffn_down.output_min          F32     [1]              \n    v.blk.0.ffn_down.weight              F16     [3072 768]       \n    v.blk.0.ffn_gate.input_max           F32     [1]              \n    v.blk.0.ffn_gate.input_min           F32     [1]              \n    v.blk.0.ffn_gate.output_max          F32     [1]              \n    v.blk.0.ffn_gate.output_min          F32     [1]              \n    v.blk.0.ffn_gate.weight              F16     [768 3072]       \n    v.blk.0.ffn_post_norm.weight         F32     [768]            \n    v.blk.0.ffn_up.input_max             F32     [1]              \n    v.blk.0.ffn_up.input_min             F32     [1]              \n    v.blk.0.ffn_up.output_max            F32     [1]              \n    v.blk.0.ffn_up.output_min            F32     [1]              \n    v.blk.0.ffn_up.weight                F16     [768 3072]       \n    v.blk.0.ln1.weight                   F32     [768]            \n    v.blk.0.ln2.weight                   F32     [768]            \n    v.blk.1.attn_k.input_max             F32     [1]              \n    v.blk.1.attn_k.input_min             F32     [1]              \n    v.blk.1.attn_k.output_max            F32     [1]              \n    v.blk.1.attn_k.output_min            F32     [1]              \n    v.blk.1.attn_k.weight                F16     [768 768]        \n    v.blk.1.attn_k_norm.weight           F32     [64]             \n    v.blk.1.attn_out.input_max           F32     [1]              \n    v.blk.1.attn_out.input_min           F32     [1]              \n    v.blk.1.attn_out.output_max          F32     [1]              \n    v.blk.1.attn_out.output_min          F32     [1]              \n    v.blk.1.attn_out.weight              F16     [768 768]        \n    v.blk.1.attn_post_norm.weight        F32     [768]            \n    v.blk.1.attn_q.input_max             F32     [1]              \n    v.blk.1.attn_q.input_min             F32     [1]              \n    v.blk.1.attn_q.output_max            F32     [1]              \n    v.blk.1.attn_q.output_min            F32     [1]              \n    v.blk.1.attn_q.weight                F16     [768 768]        \n    v.blk.1.attn_q_norm.weight           F32     [64]             \n    v.blk.1.attn_v.input_max             F32     [1]              \n    v.blk.1.attn_v.input_min             F32     [1]              \n    v.blk.1.attn_v.output_max            F32     [1]              \n    v.blk.1.attn_v.output_min            F32     [1]              \n    v.blk.1.attn_v.weight                F16     [768 768]        \n    v.blk.1.ffn_down.input_max           F32     [1]              \n    v.blk.1.ffn_down.input_min           F32     [1]              \n    v.blk.1.ffn_down.output_max          F32     [1]              \n    v.blk.1.ffn_down.output_min          F32     [1]              \n    v.blk.1.ffn_down.weight              F16     [3072 768]       \n    v.blk.1.ffn_gate.input_max           F32     [1]              \n    v.blk.1.ffn_gate.input_min           F32     [1]              \n    v.blk.1.ffn_gate.output_max          F32     [1]              \n    v.blk.1.ffn_gate.output_min          F32     [1]              \n    v.blk.1.ffn_gate.weight              F16     [768 3072]       \n    v.blk.1.ffn_post_norm.weight         F32     [768]            \n    v.blk.1.ffn_up.input_max             F32     [1]              \n    v.blk.1.ffn_up.input_min             F32     [1]              \n    v.blk.1.ffn_up.output_max            F32     [1]              \n    v.blk.1.ffn_up.output_min            F32     [1]              \n    v.blk.1.ffn_up.weight                F16     [768 3072]       \n    v.blk.1.ln1.weight                   F32     [768]            \n    v.blk.1.ln2.weight                   F32     [768]            \n    v.blk.10.attn_k.input_max            F32     [1]              \n    v.blk.10.attn_k.input_min            F32     [1]              \n    v.blk.10.attn_k.output_max           F32     [1]              \n    v.blk.10.attn_k.output_min           F32     [1]              \n    v.blk.10.attn_k.weight               F16     [768 768]        \n    v.blk.10.attn_k_norm.weight          F32     [64]             \n    v.blk.10.attn_out.input_max          F32     [1]              \n    v.blk.10.attn_out.input_min          F32     [1]              \n    v.blk.10.attn_out.output_max         F32     [1]              \n    v.blk.10.attn_out.output_min         F32     [1]              \n    v.blk.10.attn_out.weight             F16     [768 768]        \n    v.blk.10.attn_post_norm.weight       F32     [768]            \n    v.blk.10.attn_q.input_max            F32     [1]              \n    v.blk.10.attn_q.input_min            F32     [1]              \n    v.blk.10.attn_q.output_max           F32     [1]              \n    v.blk.10.attn_q.output_min           F32     [1]              \n    v.blk.10.attn_q.weight               F16     [768 768]        \n    v.blk.10.attn_q_norm.weight          F32     [64]             \n    v.blk.10.attn_v.input_max            F32     [1]              \n    v.blk.10.attn_v.input_min            F32     [1]              \n    v.blk.10.attn_v.output_max           F32     [1]              \n    v.blk.10.attn_v.output_min           F32     [1]              \n    v.blk.10.attn_v.weight               F16     [768 768]        \n    v.blk.10.ffn_down.input_max          F32     [1]              \n    v.blk.10.ffn_down.input_min          F32     [1]              \n    v.blk.10.ffn_down.output_max         F32     [1]              \n    v.blk.10.ffn_down.output_min         F32     [1]              \n    v.blk.10.ffn_down.weight             F16     [3072 768]       \n    v.blk.10.ffn_gate.input_max          F32     [1]              \n    v.blk.10.ffn_gate.input_min          F32     [1]              \n    v.blk.10.ffn_gate.output_max         F32     [1]              \n    v.blk.10.ffn_gate.output_min         F32     [1]              \n    v.blk.10.ffn_gate.weight             F16     [768 3072]       \n    v.blk.10.ffn_post_norm.weight        F32     [768]            \n    v.blk.10.ffn_up.input_max            F32     [1]              \n    v.blk.10.ffn_up.input_min            F32     [1]              \n    v.blk.10.ffn_up.output_max           F32     [1]              \n    v.blk.10.ffn_up.output_min           F32     [1]              \n    v.blk.10.ffn_up.weight               F16     [768 3072]       \n    v.blk.10.ln1.weight                  F32     [768]            \n    v.blk.10.ln2.weight                  F32     [768]            \n    v.blk.11.attn_k.input_max            F32     [1]              \n    v.blk.11.attn_k.input_min            F32     [1]              \n    v.blk.11.attn_k.output_max           F32     [1]              \n    v.blk.11.attn_k.output_min           F32     [1]              \n    v.blk.11.attn_k.weight               F16     [768 768]        \n    v.blk.11.attn_k_norm.weight          F32     [64]             \n    v.blk.11.attn_out.input_max          F32     [1]              \n    v.blk.11.attn_out.input_min          F32     [1]              \n    v.blk.11.attn_out.output_max         F32     [1]              \n    v.blk.11.attn_out.output_min         F32     [1]              \n    v.blk.11.attn_out.weight             F16     [768 768]        \n    v.blk.11.attn_post_norm.weight       F32     [768]            \n    v.blk.11.attn_q.input_max            F32     [1]              \n    v.blk.11.attn_q.input_min            F32     [1]              \n    v.blk.11.attn_q.output_max           F32     [1]              \n    v.blk.11.attn_q.output_min           F32     [1]              \n    v.blk.11.attn_q.weight               F16     [768 768]        \n    v.blk.11.attn_q_norm.weight          F32     [64]             \n    v.blk.11.attn_v.input_max            F32     [1]              \n    v.blk.11.attn_v.input_min            F32     [1]              \n    v.blk.11.attn_v.output_max           F32     [1]              \n    v.blk.11.attn_v.output_min           F32     [1]              \n    v.blk.11.attn_v.weight               F16     [768 768]        \n    v.blk.11.ffn_down.input_max          F32     [1]              \n    v.blk.11.ffn_down.input_min          F32     [1]              \n    v.blk.11.ffn_down.output_max         F32     [1]              \n    v.blk.11.ffn_down.output_min         F32     [1]              \n    v.blk.11.ffn_down.weight             F16     [3072 768]       \n    v.blk.11.ffn_gate.input_max          F32     [1]              \n    v.blk.11.ffn_gate.input_min          F32     [1]              \n    v.blk.11.ffn_gate.output_max         F32     [1]              \n    v.blk.11.ffn_gate.output_min         F32     [1]              \n    v.blk.11.ffn_gate.weight             F16     [768 3072]       \n    v.blk.11.ffn_post_norm.weight        F32     [768]            \n    v.blk.11.ffn_up.input_max            F32     [1]              \n    v.blk.11.ffn_up.input_min            F32     [1]              \n    v.blk.11.ffn_up.output_max           F32     [1]              \n    v.blk.11.ffn_up.output_min           F32     [1]              \n    v.blk.11.ffn_up.weight               F16     [768 3072]       \n    v.blk.11.ln1.weight                  F32     [768]            \n    v.blk.11.ln2.weight                  F32     [768]            \n    v.blk.12.attn_k.input_max            F32     [1]              \n    v.blk.12.attn_k.input_min            F32     [1]              \n    v.blk.12.attn_k.output_max           F32     [1]              \n    v.blk.12.attn_k.output_min           F32     [1]              \n    v.blk.12.attn_k.weight               F16     [768 768]        \n    v.blk.12.attn_k_norm.weight          F32     [64]             \n    v.blk.12.attn_out.input_max          F32     [1]              \n    v.blk.12.attn_out.input_min          F32     [1]              \n    v.blk.12.attn_out.output_max         F32     [1]              \n    v.blk.12.attn_out.output_min         F32     [1]              \n    v.blk.12.attn_out.weight             F16     [768 768]        \n    v.blk.12.attn_post_norm.weight       F32     [768]            \n    v.blk.12.attn_q.input_max            F32     [1]              \n    v.blk.12.attn_q.input_min            F32     [1]              \n    v.blk.12.attn_q.output_max           F32     [1]              \n    v.blk.12.attn_q.output_min           F32     [1]              \n    v.blk.12.attn_q.weight               F16     [768 768]        \n    v.blk.12.attn_q_norm.weight          F32     [64]             \n    v.blk.12.attn_v.input_max            F32     [1]              \n    v.blk.12.attn_v.input_min            F32     [1]              \n    v.blk.12.attn_v.output_max           F32     [1]              \n    v.blk.12.attn_v.output_min           F32     [1]              \n    v.blk.12.attn_v.weight               F16     [768 768]        \n    v.blk.12.ffn_down.input_max          F32     [1]              \n    v.blk.12.ffn_down.input_min          F32     [1]              \n    v.blk.12.ffn_down.output_max         F32     [1]              \n    v.blk.12.ffn_down.output_min         F32     [1]              \n    v.blk.12.ffn_down.weight             F16     [3072 768]       \n    v.blk.12.ffn_gate.input_max          F32     [1]              \n    v.blk.12.ffn_gate.input_min          F32     [1]              \n    v.blk.12.ffn_gate.output_max         F32     [1]              \n    v.blk.12.ffn_gate.output_min         F32     [1]              \n    v.blk.12.ffn_gate.weight             F16     [768 3072]       \n    v.blk.12.ffn_post_norm.weight        F32     [768]            \n    v.blk.12.ffn_up.input_max            F32     [1]              \n    v.blk.12.ffn_up.input_min            F32     [1]              \n    v.blk.12.ffn_up.output_max           F32     [1]              \n    v.blk.12.ffn_up.output_min           F32     [1]              \n    v.blk.12.ffn_up.weight               F16     [768 3072]       \n    v.blk.12.ln1.weight                  F32     [768]            \n    v.blk.12.ln2.weight                  F32     [768]            \n    v.blk.13.attn_k.input_max            F32     [1]              \n    v.blk.13.attn_k.input_min            F32     [1]              \n    v.blk.13.attn_k.output_max           F32     [1]              \n    v.blk.13.attn_k.output_min           F32     [1]              \n    v.blk.13.attn_k.weight               F16     [768 768]        \n    v.blk.13.attn_k_norm.weight          F32     [64]             \n    v.blk.13.attn_out.input_max          F32     [1]              \n    v.blk.13.attn_out.input_min          F32     [1]              \n    v.blk.13.attn_out.output_max         F32     [1]              \n    v.blk.13.attn_out.output_min         F32     [1]              \n    v.blk.13.attn_out.weight             F16     [768 768]        \n    v.blk.13.attn_post_norm.weight       F32     [768]            \n    v.blk.13.attn_q.input_max            F32     [1]              \n    v.blk.13.attn_q.input_min            F32     [1]              \n    v.blk.13.attn_q.output_max           F32     [1]              \n    v.blk.13.attn_q.output_min           F32     [1]              \n    v.blk.13.attn_q.weight               F16     [768 768]        \n    v.blk.13.attn_q_norm.weight          F32     [64]             \n    v.blk.13.attn_v.input_max            F32     [1]              \n    v.blk.13.attn_v.input_min            F32     [1]              \n    v.blk.13.attn_v.output_max           F32     [1]              \n    v.blk.13.attn_v.output_min           F32     [1]              \n    v.blk.13.attn_v.weight               F16     [768 768]        \n    v.blk.13.ffn_down.input_max          F32     [1]              \n    v.blk.13.ffn_down.input_min          F32     [1]              \n    v.blk.13.ffn_down.output_max         F32     [1]              \n    v.blk.13.ffn_down.output_min         F32     [1]              \n    v.blk.13.ffn_down.weight             F16     [3072 768]       \n    v.blk.13.ffn_gate.input_max          F32     [1]              \n    v.blk.13.ffn_gate.input_min          F32     [1]              \n    v.blk.13.ffn_gate.output_max         F32     [1]              \n    v.blk.13.ffn_gate.output_min         F32     [1]              \n    v.blk.13.ffn_gate.weight             F16     [768 3072]       \n    v.blk.13.ffn_post_norm.weight        F32     [768]            \n    v.blk.13.ffn_up.input_max            F32     [1]              \n    v.blk.13.ffn_up.input_min            F32     [1]              \n    v.blk.13.ffn_up.output_max           F32     [1]              \n    v.blk.13.ffn_up.output_min           F32     [1]              \n    v.blk.13.ffn_up.weight               F16     [768 3072]       \n    v.blk.13.ln1.weight                  F32     [768]            \n    v.blk.13.ln2.weight                  F32     [768]            \n    v.blk.14.attn_k.input_max            F32     [1]              \n    v.blk.14.attn_k.input_min            F32     [1]              \n    v.blk.14.attn_k.output_max           F32     [1]              \n    v.blk.14.attn_k.output_min           F32     [1]              \n    v.blk.14.attn_k.weight               F16     [768 768]        \n    v.blk.14.attn_k_norm.weight          F32     [64]             \n    v.blk.14.attn_out.input_max          F32     [1]              \n    v.blk.14.attn_out.input_min          F32     [1]              \n    v.blk.14.attn_out.output_max         F32     [1]              \n    v.blk.14.attn_out.output_min         F32     [1]              \n    v.blk.14.attn_out.weight             F16     [768 768]        \n    v.blk.14.attn_post_norm.weight       F32     [768]            \n    v.blk.14.attn_q.input_max            F32     [1]              \n    v.blk.14.attn_q.input_min            F32     [1]              \n    v.blk.14.attn_q.output_max           F32     [1]              \n    v.blk.14.attn_q.output_min           F32     [1]              \n    v.blk.14.attn_q.weight               F16     [768 768]        \n    v.blk.14.attn_q_norm.weight          F32     [64]             \n    v.blk.14.attn_v.input_max            F32     [1]              \n    v.blk.14.attn_v.input_min            F32     [1]              \n    v.blk.14.attn_v.output_max           F32     [1]              \n    v.blk.14.attn_v.output_min           F32     [1]              \n    v.blk.14.attn_v.weight               F16     [768 768]        \n    v.blk.14.ffn_down.input_max          F32     [1]              \n    v.blk.14.ffn_down.input_min          F32     [1]              \n    v.blk.14.ffn_down.output_max         F32     [1]              \n    v.blk.14.ffn_down.output_min         F32     [1]              \n    v.blk.14.ffn_down.weight             F16     [3072 768]       \n    v.blk.14.ffn_gate.input_max          F32     [1]              \n    v.blk.14.ffn_gate.input_min          F32     [1]              \n    v.blk.14.ffn_gate.output_max         F32     [1]              \n    v.blk.14.ffn_gate.output_min         F32     [1]              \n    v.blk.14.ffn_gate.weight             F16     [768 3072]       \n    v.blk.14.ffn_post_norm.weight        F32     [768]            \n    v.blk.14.ffn_up.input_max            F32     [1]              \n    v.blk.14.ffn_up.input_min            F32     [1]              \n    v.blk.14.ffn_up.output_max           F32     [1]              \n    v.blk.14.ffn_up.output_min           F32     [1]              \n    v.blk.14.ffn_up.weight               F16     [768 3072]       \n    v.blk.14.ln1.weight                  F32     [768]            \n    v.blk.14.ln2.weight                  F32     [768]            \n    v.blk.15.attn_k.input_max            F32     [1]              \n    v.blk.15.attn_k.input_min            F32     [1]              \n    v.blk.15.attn_k.output_max           F32     [1]              \n    v.blk.15.attn_k.output_min           F32     [1]              \n    v.blk.15.attn_k.weight               F16     [768 768]        \n    v.blk.15.attn_k_norm.weight          F32     [64]             \n    v.blk.15.attn_out.input_max          F32     [1]              \n    v.blk.15.attn_out.input_min          F32     [1]              \n    v.blk.15.attn_out.output_max         F32     [1]              \n    v.blk.15.attn_out.output_min         F32     [1]              \n    v.blk.15.attn_out.weight             F16     [768 768]        \n    v.blk.15.attn_post_norm.weight       F32     [768]            \n    v.blk.15.attn_q.input_max            F32     [1]              \n    v.blk.15.attn_q.input_min            F32     [1]              \n    v.blk.15.attn_q.output_max           F32     [1]              \n    v.blk.15.attn_q.output_min           F32     [1]              \n    v.blk.15.attn_q.weight               F16     [768 768]        \n    v.blk.15.attn_q_norm.weight          F32     [64]             \n    v.blk.15.attn_v.input_max            F32     [1]              \n    v.blk.15.attn_v.input_min            F32     [1]              \n    v.blk.15.attn_v.output_max           F32     [1]              \n    v.blk.15.attn_v.output_min           F32     [1]              \n    v.blk.15.attn_v.weight               F16     [768 768]        \n    v.blk.15.ffn_down.input_max          F32     [1]              \n    v.blk.15.ffn_down.input_min          F32     [1]              \n    v.blk.15.ffn_down.output_max         F32     [1]              \n    v.blk.15.ffn_down.output_min         F32     [1]              \n    v.blk.15.ffn_down.weight             F16     [3072 768]       \n    v.blk.15.ffn_gate.input_max          F32     [1]              \n    v.blk.15.ffn_gate.input_min          F32     [1]              \n    v.blk.15.ffn_gate.output_max         F32     [1]              \n    v.blk.15.ffn_gate.output_min         F32     [1]              \n    v.blk.15.ffn_gate.weight             F16     [768 3072]       \n    v.blk.15.ffn_post_norm.weight        F32     [768]            \n    v.blk.15.ffn_up.input_max            F32     [1]              \n    v.blk.15.ffn_up.input_min            F32     [1]              \n    v.blk.15.ffn_up.output_max           F32     [1]              \n    v.blk.15.ffn_up.output_min           F32     [1]              \n    v.blk.15.ffn_up.weight               F16     [768 3072]       \n    v.blk.15.ln1.weight                  F32     [768]            \n    v.blk.15.ln2.weight                  F32     [768]            \n    v.blk.2.attn_k.input_max             F32     [1]              \n    v.blk.2.attn_k.input_min             F32     [1]              \n    v.blk.2.attn_k.output_max            F32     [1]              \n    v.blk.2.attn_k.output_min            F32     [1]              \n    v.blk.2.attn_k.weight                F16     [768 768]        \n    v.blk.2.attn_k_norm.weight           F32     [64]             \n    v.blk.2.attn_out.input_max           F32     [1]              \n    v.blk.2.attn_out.input_min           F32     [1]              \n    v.blk.2.attn_out.output_max          F32     [1]              \n    v.blk.2.attn_out.output_min          F32     [1]              \n    v.blk.2.attn_out.weight              F16     [768 768]        \n    v.blk.2.attn_post_norm.weight        F32     [768]            \n    v.blk.2.attn_q.input_max             F32     [1]              \n    v.blk.2.attn_q.input_min             F32     [1]              \n    v.blk.2.attn_q.output_max            F32     [1]              \n    v.blk.2.attn_q.output_min            F32     [1]              \n    v.blk.2.attn_q.weight                F16     [768 768]        \n    v.blk.2.attn_q_norm.weight           F32     [64]             \n    v.blk.2.attn_v.input_max             F32     [1]              \n    v.blk.2.attn_v.input_min             F32     [1]              \n    v.blk.2.attn_v.output_max            F32     [1]              \n    v.blk.2.attn_v.output_min            F32     [1]              \n    v.blk.2.attn_v.weight                F16     [768 768]        \n    v.blk.2.ffn_down.input_max           F32     [1]              \n    v.blk.2.ffn_down.input_min           F32     [1]              \n    v.blk.2.ffn_down.output_max          F32     [1]              \n    v.blk.2.ffn_down.output_min          F32     [1]              \n    v.blk.2.ffn_down.weight              F16     [3072 768]       \n    v.blk.2.ffn_gate.input_max           F32     [1]              \n    v.blk.2.ffn_gate.input_min           F32     [1]              \n    v.blk.2.ffn_gate.output_max          F32     [1]              \n    v.blk.2.ffn_gate.output_min          F32     [1]              \n    v.blk.2.ffn_gate.weight              F16     [768 3072]       \n    v.blk.2.ffn_post_norm.weight         F32     [768]            \n    v.blk.2.ffn_up.input_max             F32     [1]              \n    v.blk.2.ffn_up.input_min             F32     [1]              \n    v.blk.2.ffn_up.output_max            F32     [1]              \n    v.blk.2.ffn_up.output_min            F32     [1]              \n    v.blk.2.ffn_up.weight                F16     [768 3072]       \n    v.blk.2.ln1.weight                   F32     [768]            \n    v.blk.2.ln2.weight                   F32     [768]            \n    v.blk.3.attn_k.input_max             F32     [1]              \n    v.blk.3.attn_k.input_min             F32     [1]              \n    v.blk.3.attn_k.output_max            F32     [1]              \n    v.blk.3.attn_k.output_min            F32     [1]              \n    v.blk.3.attn_k.weight                F16     [768 768]        \n    v.blk.3.attn_k_norm.weight           F32     [64]             \n    v.blk.3.attn_out.input_max           F32     [1]              \n    v.blk.3.attn_out.input_min           F32     [1]              \n    v.blk.3.attn_out.output_max          F32     [1]              \n    v.blk.3.attn_out.output_min          F32     [1]              \n    v.blk.3.attn_out.weight              F16     [768 768]        \n    v.blk.3.attn_post_norm.weight        F32     [768]            \n    v.blk.3.attn_q.input_max             F32     [1]              \n    v.blk.3.attn_q.input_min             F32     [1]              \n    v.blk.3.attn_q.output_max            F32     [1]              \n    v.blk.3.attn_q.output_min            F32     [1]              \n    v.blk.3.attn_q.weight                F16     [768 768]        \n    v.blk.3.attn_q_norm.weight           F32     [64]             \n    v.blk.3.attn_v.input_max             F32     [1]              \n    v.blk.3.attn_v.input_min             F32     [1]              \n    v.blk.3.attn_v.output_max            F32     [1]              \n    v.blk.3.attn_v.output_min            F32     [1]              \n    v.blk.3.attn_v.weight                F16     [768 768]        \n    v.blk.3.ffn_down.input_max           F32     [1]              \n    v.blk.3.ffn_down.input_min           F32     [1]              \n    v.blk.3.ffn_down.output_max          F32     [1]              \n    v.blk.3.ffn_down.output_min          F32     [1]              \n    v.blk.3.ffn_down.weight              F16     [3072 768]       \n    v.blk.3.ffn_gate.input_max           F32     [1]              \n    v.blk.3.ffn_gate.input_min           F32     [1]              \n    v.blk.3.ffn_gate.output_max          F32     [1]              \n    v.blk.3.ffn_gate.output_min          F32     [1]              \n    v.blk.3.ffn_gate.weight              F16     [768 3072]       \n    v.blk.3.ffn_post_norm.weight         F32     [768]            \n    v.blk.3.ffn_up.input_max             F32     [1]              \n    v.blk.3.ffn_up.input_min             F32     [1]              \n    v.blk.3.ffn_up.output_max            F32     [1]              \n    v.blk.3.ffn_up.output_min            F32     [1]              \n    v.blk.3.ffn_up.weight                F16     [768 3072]       \n    v.blk.3.ln1.weight                   F32     [768]            \n    v.blk.3.ln2.weight                   F32     [768]            \n    v.blk.4.attn_k.input_max             F32     [1]              \n    v.blk.4.attn_k.input_min             F32     [1]              \n    v.blk.4.attn_k.output_max            F32     [1]              \n    v.blk.4.attn_k.output_min            F32     [1]              \n    v.blk.4.attn_k.weight                F16     [768 768]        \n    v.blk.4.attn_k_norm.weight           F32     [64]             \n    v.blk.4.attn_out.input_max           F32     [1]              \n    v.blk.4.attn_out.input_min           F32     [1]              \n    v.blk.4.attn_out.output_max          F32     [1]              \n    v.blk.4.attn_out.output_min          F32     [1]              \n    v.blk.4.attn_out.weight              F16     [768 768]        \n    v.blk.4.attn_post_norm.weight        F32     [768]            \n    v.blk.4.attn_q.input_max             F32     [1]              \n    v.blk.4.attn_q.input_min             F32     [1]              \n    v.blk.4.attn_q.output_max            F32     [1]              \n    v.blk.4.attn_q.output_min            F32     [1]              \n    v.blk.4.attn_q.weight                F16     [768 768]        \n    v.blk.4.attn_q_norm.weight           F32     [64]             \n    v.blk.4.attn_v.input_max             F32     [1]              \n    v.blk.4.attn_v.input_min             F32     [1]              \n    v.blk.4.attn_v.output_max            F32     [1]              \n    v.blk.4.attn_v.output_min            F32     [1]              \n    v.blk.4.attn_v.weight                F16     [768 768]        \n    v.blk.4.ffn_down.input_max           F32     [1]              \n    v.blk.4.ffn_down.input_min           F32     [1]              \n    v.blk.4.ffn_down.output_max          F32     [1]              \n    v.blk.4.ffn_down.output_min          F32     [1]              \n    v.blk.4.ffn_down.weight              F16     [3072 768]       \n    v.blk.4.ffn_gate.input_max           F32     [1]              \n    v.blk.4.ffn_gate.input_min           F32     [1]              \n    v.blk.4.ffn_gate.output_max          F32     [1]              \n    v.blk.4.ffn_gate.output_min          F32     [1]              \n    v.blk.4.ffn_gate.weight              F16     [768 3072]       \n    v.blk.4.ffn_post_norm.weight         F32     [768]            \n    v.blk.4.ffn_up.input_max             F32     [1]              \n    v.blk.4.ffn_up.input_min             F32     [1]              \n    v.blk.4.ffn_up.output_max            F32     [1]              \n    v.blk.4.ffn_up.output_min            F32     [1]              \n    v.blk.4.ffn_up.weight                F16     [768 3072]       \n    v.blk.4.ln1.weight                   F32     [768]            \n    v.blk.4.ln2.weight                   F32     [768]            \n    v.blk.5.attn_k.input_max             F32     [1]              \n    v.blk.5.attn_k.input_min             F32     [1]              \n    v.blk.5.attn_k.output_max            F32     [1]              \n    v.blk.5.attn_k.output_min            F32     [1]              \n    v.blk.5.attn_k.weight                F16     [768 768]        \n    v.blk.5.attn_k_norm.weight           F32     [64]             \n    v.blk.5.attn_out.input_max           F32     [1]              \n    v.blk.5.attn_out.input_min           F32     [1]              \n    v.blk.5.attn_out.output_max          F32     [1]              \n    v.blk.5.attn_out.output_min          F32     [1]              \n    v.blk.5.attn_out.weight              F16     [768 768]        \n    v.blk.5.attn_post_norm.weight        F32     [768]            \n    v.blk.5.attn_q.input_max             F32     [1]              \n    v.blk.5.attn_q.input_min             F32     [1]              \n    v.blk.5.attn_q.output_max            F32     [1]              \n    v.blk.5.attn_q.output_min            F32     [1]              \n    v.blk.5.attn_q.weight                F16     [768 768]        \n    v.blk.5.attn_q_norm.weight           F32     [64]             \n    v.blk.5.attn_v.input_max             F32     [1]              \n    v.blk.5.attn_v.input_min             F32     [1]              \n    v.blk.5.attn_v.output_max            F32     [1]              \n    v.blk.5.attn_v.output_min            F32     [1]              \n    v.blk.5.attn_v.weight                F16     [768 768]        \n    v.blk.5.ffn_down.input_max           F32     [1]              \n    v.blk.5.ffn_down.input_min           F32     [1]              \n    v.blk.5.ffn_down.output_max          F32     [1]              \n    v.blk.5.ffn_down.output_min          F32     [1]              \n    v.blk.5.ffn_down.weight              F16     [3072 768]       \n    v.blk.5.ffn_gate.input_max           F32     [1]              \n    v.blk.5.ffn_gate.input_min           F32     [1]              \n    v.blk.5.ffn_gate.output_max          F32     [1]              \n    v.blk.5.ffn_gate.output_min          F32     [1]              \n    v.blk.5.ffn_gate.weight              F16     [768 3072]       \n    v.blk.5.ffn_post_norm.weight         F32     [768]            \n    v.blk.5.ffn_up.input_max             F32     [1]              \n    v.blk.5.ffn_up.input_min             F32     [1]              \n    v.blk.5.ffn_up.output_max            F32     [1]              \n    v.blk.5.ffn_up.output_min            F32     [1]              \n    v.blk.5.ffn_up.weight                F16     [768 3072]       \n    v.blk.5.ln1.weight                   F32     [768]            \n    v.blk.5.ln2.weight                   F32     [768]            \n    v.blk.6.attn_k.input_max             F32     [1]              \n    v.blk.6.attn_k.input_min             F32     [1]              \n    v.blk.6.attn_k.output_max            F32     [1]              \n    v.blk.6.attn_k.output_min            F32     [1]              \n    v.blk.6.attn_k.weight                F16     [768 768]        \n    v.blk.6.attn_k_norm.weight           F32     [64]             \n    v.blk.6.attn_out.input_max           F32     [1]              \n    v.blk.6.attn_out.input_min           F32     [1]              \n    v.blk.6.attn_out.output_max          F32     [1]              \n    v.blk.6.attn_out.output_min          F32     [1]              \n    v.blk.6.attn_out.weight              F16     [768 768]        \n    v.blk.6.attn_post_norm.weight        F32     [768]            \n    v.blk.6.attn_q.input_max             F32     [1]              \n    v.blk.6.attn_q.input_min             F32     [1]              \n    v.blk.6.attn_q.output_max            F32     [1]              \n    v.blk.6.attn_q.output_min            F32     [1]              \n    v.blk.6.attn_q.weight                F16     [768 768]        \n    v.blk.6.attn_q_norm.weight           F32     [64]             \n    v.blk.6.attn_v.input_max             F32     [1]              \n    v.blk.6.attn_v.input_min             F32     [1]              \n    v.blk.6.attn_v.output_max            F32     [1]              \n    v.blk.6.attn_v.output_min            F32     [1]              \n    v.blk.6.attn_v.weight                F16     [768 768]        \n    v.blk.6.ffn_down.input_max           F32     [1]              \n    v.blk.6.ffn_down.input_min           F32     [1]              \n    v.blk.6.ffn_down.output_max          F32     [1]              \n    v.blk.6.ffn_down.output_min          F32     [1]              \n    v.blk.6.ffn_down.weight              F16     [3072 768]       \n    v.blk.6.ffn_gate.input_max           F32     [1]              \n    v.blk.6.ffn_gate.input_min           F32     [1]              \n    v.blk.6.ffn_gate.output_max          F32     [1]              \n    v.blk.6.ffn_gate.output_min          F32     [1]              \n    v.blk.6.ffn_gate.weight              F16     [768 3072]       \n    v.blk.6.ffn_post_norm.weight         F32     [768]            \n    v.blk.6.ffn_up.input_max             F32     [1]              \n    v.blk.6.ffn_up.input_min             F32     [1]              \n    v.blk.6.ffn_up.output_max            F32     [1]              \n    v.blk.6.ffn_up.output_min            F32     [1]              \n    v.blk.6.ffn_up.weight                F16     [768 3072]       \n    v.blk.6.ln1.weight                   F32     [768]            \n    v.blk.6.ln2.weight                   F32     [768]            \n    v.blk.7.attn_k.input_max             F32     [1]              \n    v.blk.7.attn_k.input_min             F32     [1]              \n    v.blk.7.attn_k.output_max            F32     [1]              \n    v.blk.7.attn_k.output_min            F32     [1]              \n    v.blk.7.attn_k.weight                F16     [768 768]        \n    v.blk.7.attn_k_norm.weight           F32     [64]             \n    v.blk.7.attn_out.input_max           F32     [1]              \n    v.blk.7.attn_out.input_min           F32     [1]              \n    v.blk.7.attn_out.output_max          F32     [1]              \n    v.blk.7.attn_out.output_min          F32     [1]              \n    v.blk.7.attn_out.weight              F16     [768 768]        \n    v.blk.7.attn_post_norm.weight        F32     [768]            \n    v.blk.7.attn_q.input_max             F32     [1]              \n    v.blk.7.attn_q.input_min             F32     [1]              \n    v.blk.7.attn_q.output_max            F32     [1]              \n    v.blk.7.attn_q.output_min            F32     [1]              \n    v.blk.7.attn_q.weight                F16     [768 768]        \n    v.blk.7.attn_q_norm.weight           F32     [64]             \n    v.blk.7.attn_v.input_max             F32     [1]              \n    v.blk.7.attn_v.input_min             F32     [1]              \n    v.blk.7.attn_v.output_max            F32     [1]              \n    v.blk.7.attn_v.output_min            F32     [1]              \n    v.blk.7.attn_v.weight                F16     [768 768]        \n    v.blk.7.ffn_down.input_max           F32     [1]              \n    v.blk.7.ffn_down.input_min           F32     [1]              \n    v.blk.7.ffn_down.output_max          F32     [1]              \n    v.blk.7.ffn_down.output_min          F32     [1]              \n    v.blk.7.ffn_down.weight              F16     [3072 768]       \n    v.blk.7.ffn_gate.input_max           F32     [1]              \n    v.blk.7.ffn_gate.input_min           F32     [1]              \n    v.blk.7.ffn_gate.output_max          F32     [1]              \n    v.blk.7.ffn_gate.output_min          F32     [1]              \n    v.blk.7.ffn_gate.weight              F16     [768 3072]       \n    v.blk.7.ffn_post_norm.weight         F32     [768]            \n    v.blk.7.ffn_up.input_max             F32     [1]              \n    v.blk.7.ffn_up.input_min             F32     [1]              \n    v.blk.7.ffn_up.output_max            F32     [1]              \n    v.blk.7.ffn_up.output_min            F32     [1]              \n    v.blk.7.ffn_up.weight                F16     [768 3072]       \n    v.blk.7.ln1.weight                   F32     [768]            \n    v.blk.7.ln2.weight                   F32     [768]            \n    v.blk.8.attn_k.input_max             F32     [1]              \n    v.blk.8.attn_k.input_min             F32     [1]              \n    v.blk.8.attn_k.output_max            F32     [1]              \n    v.blk.8.attn_k.output_min            F32     [1]              \n    v.blk.8.attn_k.weight                F16     [768 768]        \n    v.blk.8.attn_k_norm.weight           F32     [64]             \n    v.blk.8.attn_out.input_max           F32     [1]              \n    v.blk.8.attn_out.input_min           F32     [1]              \n    v.blk.8.attn_out.output_max          F32     [1]              \n    v.blk.8.attn_out.output_min          F32     [1]              \n    v.blk.8.attn_out.weight              F16     [768 768]        \n    v.blk.8.attn_post_norm.weight        F32     [768]            \n    v.blk.8.attn_q.input_max             F32     [1]              \n    v.blk.8.attn_q.input_min             F32     [1]              \n    v.blk.8.attn_q.output_max            F32     [1]              \n    v.blk.8.attn_q.output_min            F32     [1]              \n    v.blk.8.attn_q.weight                F16     [768 768]        \n    v.blk.8.attn_q_norm.weight           F32     [64]             \n    v.blk.8.attn_v.input_max             F32     [1]              \n    v.blk.8.attn_v.input_min             F32     [1]              \n    v.blk.8.attn_v.output_max            F32     [1]              \n    v.blk.8.attn_v.output_min            F32     [1]              \n    v.blk.8.attn_v.weight                F16     [768 768]        \n    v.blk.8.ffn_down.input_max           F32     [1]              \n    v.blk.8.ffn_down.input_min           F32     [1]              \n    v.blk.8.ffn_down.output_max          F32     [1]              \n    v.blk.8.ffn_down.output_min          F32     [1]              \n    v.blk.8.ffn_down.weight              F16     [3072 768]       \n    v.blk.8.ffn_gate.input_max           F32     [1]              \n    v.blk.8.ffn_gate.input_min           F32     [1]              \n    v.blk.8.ffn_gate.output_max          F32     [1]              \n    v.blk.8.ffn_gate.output_min          F32     [1]              \n    v.blk.8.ffn_gate.weight              F16     [768 3072]       \n    v.blk.8.ffn_post_norm.weight         F32     [768]            \n    v.blk.8.ffn_up.input_max             F32     [1]              \n    v.blk.8.ffn_up.input_min             F32     [1]              \n    v.blk.8.ffn_up.output_max            F32     [1]              \n    v.blk.8.ffn_up.output_min            F32     [1]              \n    v.blk.8.ffn_up.weight                F16     [768 3072]       \n    v.blk.8.ln1.weight                   F32     [768]            \n    v.blk.8.ln2.weight                   F32     [768]            \n    v.blk.9.attn_k.input_max             F32     [1]              \n    v.blk.9.attn_k.input_min             F32     [1]              \n    v.blk.9.attn_k.output_max            F32     [1]              \n    v.blk.9.attn_k.output_min            F32     [1]              \n    v.blk.9.attn_k.weight                F16     [768 768]        \n    v.blk.9.attn_k_norm.weight           F32     [64]             \n    v.blk.9.attn_out.input_max           F32     [1]              \n    v.blk.9.attn_out.input_min           F32     [1]              \n    v.blk.9.attn_out.output_max          F32     [1]              \n    v.blk.9.attn_out.output_min          F32     [1]              \n    v.blk.9.attn_out.weight              F16     [768 768]        \n    v.blk.9.attn_post_norm.weight        F32     [768]            \n    v.blk.9.attn_q.input_max             F32     [1]              \n    v.blk.9.attn_q.input_min             F32     [1]              \n    v.blk.9.attn_q.output_max            F32     [1]              \n    v.blk.9.attn_q.output_min            F32     [1]              \n    v.blk.9.attn_q.weight                F16     [768 768]        \n    v.blk.9.attn_q_norm.weight           F32     [64]             \n    v.blk.9.attn_v.input_max             F32     [1]              \n    v.blk.9.attn_v.input_min             F32     [1]              \n    v.blk.9.attn_v.output_max            F32     [1]              \n    v.blk.9.attn_v.output_min            F32     [1]              \n    v.blk.9.attn_v.weight                F16     [768 768]        \n    v.blk.9.ffn_down.input_max           F32     [1]              \n    v.blk.9.ffn_down.input_min           F32     [1]              \n    v.blk.9.ffn_down.output_max          F32     [1]              \n    v.blk.9.ffn_down.output_min          F32     [1]              \n    v.blk.9.ffn_down.weight              F16     [3072 768]       \n    v.blk.9.ffn_gate.input_max           F32     [1]              \n    v.blk.9.ffn_gate.input_min           F32     [1]              \n    v.blk.9.ffn_gate.output_max          F32     [1]              \n    v.blk.9.ffn_gate.output_min          F32     [1]              \n    v.blk.9.ffn_gate.weight              F16     [768 3072]       \n    v.blk.9.ffn_post_norm.weight         F32     [768]            \n    v.blk.9.ffn_up.input_max             F32     [1]              \n    v.blk.9.ffn_up.input_min             F32     [1]              \n    v.blk.9.ffn_up.output_max            F32     [1]              \n    v.blk.9.ffn_up.output_min            F32     [1]              \n    v.blk.9.ffn_up.weight                F16     [768 3072]       \n    v.blk.9.ln1.weight                   F32     [768]            \n    v.blk.9.ln2.weight                   F32     [768]            \n    v.patch_embd.weight                  F16     [16 16 3 768]    \n    v.position_embd.weight               F32     [768 10240 2]    \n\n  License\n    Apache License               \n    Version 2.0, January 2004    \n    ...",
  "vram_used_mb_min_max_durante_generacion": [
    1315,
    5699
  ],
  "gpu_util_pct_min_max_durante_generacion": [
    3,
    87
  ],
  "cpu_pct_min_max_durante_generacion": [
    0.0,
    92.4
  ],
  "ram_used_mb_min_max_durante_generacion": [
    14790,
    20335
  ],
  "muestras_completas": [
    {
      "t": 1788671075.9181652,
      "gpu": {
        "vram_used_mb": 5685,
        "vram_total_mb": 6144,
        "gpu_util_pct": 19
      },
      "sys": {
        "cpu_pct": 0.0,
        "ram_used_mb": 17775,
        "ram_total_mb": 24511
      }
    },
    {
      "t": 1788671076.4914625,
      "gpu": {
        "vram_used_mb": 5685,
        "vram_total_mb": 6144,
        "gpu_util_pct": 19
      },
      "sys": {
        "cpu_pct": 66.1,
        "ram_used_mb": 17772,
        "ram_total_mb": 24511
      }
    },
    {
      "t": 1788671077.0675797,
      "gpu": {
        "vram_used_mb": 5685,
        "vram_total_mb": 6144,
        "gpu_util_pct": 13
      },
      "sys": {
        "cpu_pct": 70.4,
        "ram_used_mb": 17775,
        "ram_total_mb": 24511
      }
    },
    {
      "t": 1788671077.6542969,
      "gpu": {
        "vram_used_mb": 5699,
        "vram_total_mb": 6144,
        "gpu_util_pct": 22
      },
      "sys": {
        "cpu_pct": 76.7,
        "ram_used_mb": 17771,
        "ram_total_mb": 24511
      }
    },
    {
      "t": 1788671078.223506,
      "gpu": {
        "vram_used_mb": 5699,
        "vram_total_mb": 6144,
        "gpu_util_pct": 22
      },
      "sys": {
        "cpu_pct": 71.5,
        "ram_used_mb": 17776,
        "ram_total_mb": 24511
      }
    },
    {
      "t": 1788671078.804498,
      "gpu": {
        "vram_used_mb": 1318,
        "vram_total_mb": 6144,
        "gpu_util_pct": 24
      },
      "sys": {
        "cpu_pct": 83.1,
        "ram_used_mb": 16164,
        "ram_total_mb": 24511
      }
    },
    {
      "t": 1788671079.404757,
      "gpu": {
        "vram_used_mb": 1329,
        "vram_total_mb": 6144,
        "gpu_util_pct": 24
      },
      "sys": {
        "cpu_pct": 85.6,
        "ram_used_mb": 15056,
        "ram_total_mb": 24511
      }
    },
    {
      "t": 1788671079.9834063,
      "gpu": {
        "vram_used_mb": 1327,
        "vram_total_mb": 6144,
        "gpu_util_pct": 31
      },
      "sys": {
        "cpu_pct": 86.5,
        "ram_used_mb": 15085,
        "ram_total_mb": 24511
      }
    },
    {
      "t": 1788671080.5604947,
      "gpu": {
        "vram_used_mb": 1323,
        "vram_total_mb": 6144,
        "gpu_util_pct": 15
      },
      "sys": {
        "cpu_pct": 80.3,
        "ram_used_mb": 14797,
        "ram_total_mb": 24511
      }
    },
    {
      "t": 1788671081.1351085,
      "gpu": {
        "vram_used_mb": 1323,
        "vram_total_mb": 6144,
        "gpu_util_pct": 15
      },
      "sys": {
        "cpu_pct": 75.6,
        "ram_used_mb": 14880,
        "ram_total_mb": 24511
      }
    },
    {
      "t": 1788671081.7024026,
      "gpu": {
        "vram_used_mb": 1361,
        "vram_total_mb": 6144,
        "gpu_util_pct": 4
      },
      "sys": {
        "cpu_pct": 67.4,
        "ram_used_mb": 14950,
        "ram_total_mb": 24511
      }
    },
    {
      "t": 1788671082.2717988,
      "gpu": {
        "vram_used_mb": 1315,
        "vram_total_mb": 6144,
        "gpu_util_pct": 4
      },
      "sys": {
        "cpu_pct": 62.3,
        "ram_used_mb": 14790,
        "ram_total_mb": 24511
      }
    },
    {
      "t": 1788671082.8493555,
      "gpu": {
        "vram_used_mb": 1372,
        "vram_total_mb": 6144,
        "gpu_util_pct": 5
      },
      "sys": {
        "cpu_pct": 62.3,
        "ram_used_mb": 15057,
        "ram_total_mb": 24511
      }
    },
    {
      "t": 1788671083.4156768,
      "gpu": {
        "vram_used_mb": 1372,
        "vram_total_mb": 6144,
        "gpu_util_pct": 5
      },
      "sys": {
        "cpu_pct": 66.7,
        "ram_used_mb": 15116,
        "ram_total_mb": 24511
      }
    },
    {
      "t": 1788671083.9761925,
      "gpu": {
        "vram_used_mb": 1360,
        "vram_total_mb": 6144,
        "gpu_util_pct": 7
      },
      "sys": {
        "cpu_pct": 57.6,
        "ram_used_mb": 15063,
        "ram_total_mb": 24511
      }
    },
    {
      "t": 1788671084.5388863,
      "gpu": {
        "vram_used_mb": 1349,
        "vram_total_mb": 6144,
        "gpu_util_pct": 7
      },
      "sys": {
        "cpu_pct": 61.5,
        "ram_used_mb": 15125,
        "ram_total_mb": 24511
      }
    },
    {
      "t": 1788671085.121643,
      "gpu": {
        "vram_used_mb": 2746,
        "vram_total_mb": 6144,
        "gpu_util_pct": 3
      },
      "sys": {
        "cpu_pct": 68.9,
        "ram_used_mb": 18234,
        "ram_total_mb": 24511
      }
    },
    {
      "t": 1788671085.7013044,
      "gpu": {
        "vram_used_mb": 2746,
        "vram_total_mb": 6144,
        "gpu_util_pct": 7
      },
      "sys": {
        "cpu_pct": 92.4,
        "ram_used_mb": 19935,
        "ram_total_mb": 24511
      }
    },
    {
      "t": 1788671086.2858038,
      "gpu": {
        "vram_used_mb": 2742,
        "vram_total_mb": 6144,
        "gpu_util_pct": 7
      },
      "sys": {
        "cpu_pct": 72.1,
        "ram_used_mb": 19960,
        "ram_total_mb": 24511
      }
    },
    {
      "t": 1788671086.8677843,
      "gpu": {
        "vram_used_mb": 2742,
        "vram_total_mb": 6144,
        "gpu_util_pct": 6
      },
      "sys": {
        "cpu_pct": 58.6,
        "ram_used_mb": 19923,
        "ram_total_mb": 24511
      }
    },
    {
      "t": 1788671087.424036,
      "gpu": {
        "vram_used_mb": 2742,
        "vram_total_mb": 6144,
        "gpu_util_pct": 6
      },
      "sys": {
        "cpu_pct": 68.1,
        "ram_used_mb": 19921,
        "ram_total_mb": 24511
      }
    },
    {
      "t": 1788671088.0053103,
      "gpu": {
        "vram_used_mb": 2742,
        "vram_total_mb": 6144,
        "gpu_util_pct": 6
      },
      "sys": {
        "cpu_pct": 68.4,
        "ram_used_mb": 19924,
        "ram_total_mb": 24511
      }
    },
    {
      "t": 1788671088.6103036,
      "gpu": {
        "vram_used_mb": 2742,
        "vram_total_mb": 6144,
        "gpu_util_pct": 4
      },
      "sys": {
        "cpu_pct": 67.6,
        "ram_used_mb": 19932,
        "ram_total_mb": 24511
      }
    },
    {
      "t": 1788671089.2084408,
      "gpu": {
        "vram_used_mb": 2736,
        "vram_total_mb": 6144,
        "gpu_util_pct": 4
      },
      "sys": {
        "cpu_pct": 66.8,
        "ram_used_mb": 19930,
        "ram_total_mb": 24511
      }
    },
    {
      "t": 1788671089.7691753,
      "gpu": {
        "vram_used_mb": 2736,
        "vram_total_mb": 6144,
        "gpu_util_pct": 5
      },
      "sys": {
        "cpu_pct": 66.0,
        "ram_used_mb": 19929,
        "ram_total_mb": 24511
      }
    },
    {
      "t": 1788671090.4181519,
      "gpu": {
        "vram_used_mb": 2736,
        "vram_total_mb": 6144,
        "gpu_util_pct": 5
      },
      "sys": {
        "cpu_pct": 63.0,
        "ram_used_mb": 19936,
        "ram_total_mb": 24511
      }
    },
    {
      "t": 1788671091.0100355,
      "gpu": {
        "vram_used_mb": 2736,
        "vram_total_mb": 6144,
        "gpu_util_pct": 21
      },
      "sys": {
        "cpu_pct": 55.0,
        "ram_used_mb": 19962,
        "ram_total_mb": 24511
      }
    },
    {
      "t": 1788671091.574235,
      "gpu": {
        "vram_used_mb": 2736,
        "vram_total_mb": 6144,
        "gpu_util_pct": 21
      },
      "sys": {
        "cpu_pct": 58.5,
        "ram_used_mb": 19968,
        "ram_total_mb": 24511
      }
    },
    {
      "t": 1788671092.1486,
      "gpu": {
        "vram_used_mb": 2736,
        "vram_total_mb": 6144,
        "gpu_util_pct": 25
      },
      "sys": {
        "cpu_pct": 66.4,
        "ram_used_mb": 19985,
        "ram_total_mb": 24511
      }
    },
    {
      "t": 1788671092.722647,
      "gpu": {
        "vram_used_mb": 2736,
        "vram_total_mb": 6144,
        "gpu_util_pct": 25
      },
      "sys": {
        "cpu_pct": 64.5,
        "ram_used_mb": 19990,
        "ram_total_mb": 24511
      }
    },
    {
      "t": 1788671093.2915497,
      "gpu": {
        "vram_used_mb": 2736,
        "vram_total_mb": 6144,
        "gpu_util_pct": 25
      },
      "sys": {
        "cpu_pct": 61.9,
        "ram_used_mb": 20053,
        "ram_total_mb": 24511
      }
    },
    {
      "t": 1788671093.87019,
      "gpu": {
        "vram_used_mb": 2736,
        "vram_total_mb": 6144,
        "gpu_util_pct": 16
      },
      "sys": {
        "cpu_pct": 52.9,
        "ram_used_mb": 20046,
        "ram_total_mb": 24511
      }
    },
    {
      "t": 1788671094.4485662,
      "gpu": {
        "vram_used_mb": 2736,
        "vram_total_mb": 6144,
        "gpu_util_pct": 16
      },
      "sys": {
        "cpu_pct": 50.9,
        "ram_used_mb": 20043,
        "ram_total_mb": 24511
      }
    },
    {
      "t": 1788671095.0186362,
      "gpu": {
        "vram_used_mb": 2736,
        "vram_total_mb": 6144,
        "gpu_util_pct": 16
      },
      "sys": {
        "cpu_pct": 47.1,
        "ram_used_mb": 20043,
        "ram_total_mb": 24511
      }
    },
    {
      "t": 1788671095.5990167,
      "gpu": {
        "vram_used_mb": 2736,
        "vram_total_mb": 6144,
        "gpu_util_pct": 16
      },
      "sys": {
        "cpu_pct": 65.5,
        "ram_used_mb": 20043,
        "ram_total_mb": 24511
      }
    },
    {
      "t": 1788671096.1892445,
      "gpu": {
        "vram_used_mb": 2736,
        "vram_total_mb": 6144,
        "gpu_util_pct": 15
      },
      "sys": {
        "cpu_pct": 56.6,
        "ram_used_mb": 20050,
        "ram_total_mb": 24511
      }
    },
    {
      "t": 1788671096.7633212,
      "gpu": {
        "vram_used_mb": 2736,
        "vram_total_mb": 6144,
        "gpu_util_pct": 15
      },
      "sys": {
        "cpu_pct": 61.5,
        "ram_used_mb": 20045,
        "ram_total_mb": 24511
      }
    },
    {
      "t": 1788671097.395969,
      "gpu": {
        "vram_used_mb": 2736,
        "vram_total_mb": 6144,
        "gpu_util_pct": 15
      },
      "sys": {
        "cpu_pct": 61.5,
        "ram_used_mb": 20024,
        "ram_total_mb": 24511
      }
    },
    {
      "t": 1788671097.9701607,
      "gpu": {
        "vram_used_mb": 2736,
        "vram_total_mb": 6144,
        "gpu_util_pct": 15
      },
      "sys": {
        "cpu_pct": 53.8,
        "ram_used_mb": 20043,
        "ram_total_mb": 24511
      }
    },
    {
      "t": 1788671098.5415082,
      "gpu": {
        "vram_used_mb": 2736,
        "vram_total_mb": 6144,
        "gpu_util_pct": 15
      },
      "sys": {
        "cpu_pct": 60.1,
        "ram_used_mb": 20037,
        "ram_total_mb": 24511
      }
    },
    {
      "t": 1788671099.1323707,
      "gpu": {
        "vram_used_mb": 2736,
        "vram_total_mb": 6144,
        "gpu_util_pct": 15
      },
      "sys": {
        "cpu_pct": 59.4,
        "ram_used_mb": 20034,
        "ram_total_mb": 24511
      }
    },
    {
      "t": 1788671099.710251,
      "gpu": {
        "vram_used_mb": 2736,
        "vram_total_mb": 6144,
        "gpu_util_pct": 15
      },
      "sys": {
        "cpu_pct": 58.3,
        "ram_used_mb": 20037,
        "ram_total_mb": 24511
      }
    },
    {
      "t": 1788671100.2691813,
      "gpu": {
        "vram_used_mb": 2736,
        "vram_total_mb": 6144,
        "gpu_util_pct": 15
      },
      "sys": {
        "cpu_pct": 67.3,
        "ram_used_mb": 20041,
        "ram_total_mb": 24511
      }
    },
    {
      "t": 1788671100.8437371,
      "gpu": {
        "vram_used_mb": 2743,
        "vram_total_mb": 6144,
        "gpu_util_pct": 15
      },
      "sys": {
        "cpu_pct": 53.9,
        "ram_used_mb": 20005,
        "ram_total_mb": 24511
      }
    },
    {
      "t": 1788671101.419485,
      "gpu": {
        "vram_used_mb": 2743,
        "vram_total_mb": 6144,
        "gpu_util_pct": 15
      },
      "sys": {
        "cpu_pct": 49.6,
        "ram_used_mb": 20024,
        "ram_total_mb": 24511
      }
    },
    {
      "t": 1788671101.9898884,
      "gpu": {
        "vram_used_mb": 2739,
        "vram_total_mb": 6144,
        "gpu_util_pct": 15
      },
      "sys": {
        "cpu_pct": 65.2,
        "ram_used_mb": 20026,
        "ram_total_mb": 24511
      }
    },
    {
      "t": 1788671102.5515246,
      "gpu": {
        "vram_used_mb": 2739,
        "vram_total_mb": 6144,
        "gpu_util_pct": 15
      },
      "sys": {
        "cpu_pct": 53.4,
        "ram_used_mb": 19973,
        "ram_total_mb": 24511
      }
    },
    {
      "t": 1788671103.1324835,
      "gpu": {
        "vram_used_mb": 2739,
        "vram_total_mb": 6144,
        "gpu_util_pct": 14
      },
      "sys": {
        "cpu_pct": 54.8,
        "ram_used_mb": 20032,
        "ram_total_mb": 24511
      }
    },
    {
      "t": 1788671103.7025077,
      "gpu": {
        "vram_used_mb": 2753,
        "vram_total_mb": 6144,
        "gpu_util_pct": 15
      },
      "sys": {
        "cpu_pct": 45.5,
        "ram_used_mb": 19958,
        "ram_total_mb": 24511
      }
    },
    {
      "t": 1788671104.2750733,
      "gpu": {
        "vram_used_mb": 2889,
        "vram_total_mb": 6144,
        "gpu_util_pct": 15
      },
      "sys": {
        "cpu_pct": 64.3,
        "ram_used_mb": 20064,
        "ram_total_mb": 24511
      }
    },
    {
      "t": 1788671104.8555918,
      "gpu": {
        "vram_used_mb": 3243,
        "vram_total_mb": 6144,
        "gpu_util_pct": 29
      },
      "sys": {
        "cpu_pct": 61.5,
        "ram_used_mb": 20121,
        "ram_total_mb": 24511
      }
    },
    {
      "t": 1788671105.435788,
      "gpu": {
        "vram_used_mb": 3243,
        "vram_total_mb": 6144,
        "gpu_util_pct": 29
      },
      "sys": {
        "cpu_pct": 67.7,
        "ram_used_mb": 20079,
        "ram_total_mb": 24511
      }
    },
    {
      "t": 1788671106.0054805,
      "gpu": {
        "vram_used_mb": 3240,
        "vram_total_mb": 6144,
        "gpu_util_pct": 8
      },
      "sys": {
        "cpu_pct": 68.2,
        "ram_used_mb": 20083,
        "ram_total_mb": 24511
      }
    },
    {
      "t": 1788671106.5787945,
      "gpu": {
        "vram_used_mb": 3932,
        "vram_total_mb": 6144,
        "gpu_util_pct": 8
      },
      "sys": {
        "cpu_pct": 68.0,
        "ram_used_mb": 20105,
        "ram_total_mb": 24511
      }
    },
    {
      "t": 1788671107.160885,
      "gpu": {
        "vram_used_mb": 3932,
        "vram_total_mb": 6144,
        "gpu_util_pct": 10
      },
      "sys": {
        "cpu_pct": 55.1,
        "ram_used_mb": 20112,
        "ram_total_mb": 24511
      }
    },
    {
      "t": 1788671107.777037,
      "gpu": {
        "vram_used_mb": 3932,
        "vram_total_mb": 6144,
        "gpu_util_pct": 23
      },
      "sys": {
        "cpu_pct": 64.2,
        "ram_used_mb": 20113,
        "ram_total_mb": 24511
      }
    },
    {
      "t": 1788671108.3488839,
      "gpu": {
        "vram_used_mb": 3932,
        "vram_total_mb": 6144,
        "gpu_util_pct": 23
      },
      "sys": {
        "cpu_pct": 72.0,
        "ram_used_mb": 20094,
        "ram_total_mb": 24511
      }
    },
    {
      "t": 1788671108.930144,
      "gpu": {
        "vram_used_mb": 4042,
        "vram_total_mb": 6144,
        "gpu_util_pct": 33
      },
      "sys": {
        "cpu_pct": 64.7,
        "ram_used_mb": 20141,
        "ram_total_mb": 24511
      }
    },
    {
      "t": 1788671109.5054073,
      "gpu": {
        "vram_used_mb": 4042,
        "vram_total_mb": 6144,
        "gpu_util_pct": 33
      },
      "sys": {
        "cpu_pct": 68.6,
        "ram_used_mb": 20159,
        "ram_total_mb": 24511
      }
    },
    {
      "t": 1788671110.0824075,
      "gpu": {
        "vram_used_mb": 4042,
        "vram_total_mb": 6144,
        "gpu_util_pct": 54
      },
      "sys": {
        "cpu_pct": 66.5,
        "ram_used_mb": 20151,
        "ram_total_mb": 24511
      }
    },
    {
      "t": 1788671110.663643,
      "gpu": {
        "vram_used_mb": 4042,
        "vram_total_mb": 6144,
        "gpu_util_pct": 54
      },
      "sys": {
        "cpu_pct": 72.3,
        "ram_used_mb": 20019,
        "ram_total_mb": 24511
      }
    },
    {
      "t": 1788671111.2422209,
      "gpu": {
        "vram_used_mb": 4042,
        "vram_total_mb": 6144,
        "gpu_util_pct": 86
      },
      "sys": {
        "cpu_pct": 73.7,
        "ram_used_mb": 20016,
        "ram_total_mb": 24511
      }
    },
    {
      "t": 1788671111.812108,
      "gpu": {
        "vram_used_mb": 4042,
        "vram_total_mb": 6144,
        "gpu_util_pct": 87
      },
      "sys": {
        "cpu_pct": 63.6,
        "ram_used_mb": 20015,
        "ram_total_mb": 24511
      }
    },
    {
      "t": 1788671112.3984637,
      "gpu": {
        "vram_used_mb": 4042,
        "vram_total_mb": 6144,
        "gpu_util_pct": 87
      },
      "sys": {
        "cpu_pct": 58.0,
        "ram_used_mb": 20015,
        "ram_total_mb": 24511
      }
    },
    {
      "t": 1788671112.9688277,
      "gpu": {
        "vram_used_mb": 4042,
        "vram_total_mb": 6144,
        "gpu_util_pct": 82
      },
      "sys": {
        "cpu_pct": 63.0,
        "ram_used_mb": 20019,
        "ram_total_mb": 24511
      }
    },
    {
      "t": 1788671113.5486963,
      "gpu": {
        "vram_used_mb": 4042,
        "vram_total_mb": 6144,
        "gpu_util_pct": 82
      },
      "sys": {
        "cpu_pct": 71.1,
        "ram_used_mb": 20020,
        "ram_total_mb": 24511
      }
    },
    {
      "t": 1788671114.1187031,
      "gpu": {
        "vram_used_mb": 4042,
        "vram_total_mb": 6144,
        "gpu_util_pct": 86
      },
      "sys": {
        "cpu_pct": 67.0,
        "ram_used_mb": 20020,
        "ram_total_mb": 24511
      }
    },
    {
      "t": 1788671114.6891508,
      "gpu": {
        "vram_used_mb": 4042,
        "vram_total_mb": 6144,
        "gpu_util_pct": 86
      },
      "sys": {
        "cpu_pct": 68.0,
        "ram_used_mb": 20021,
        "ram_total_mb": 24511
      }
    },
    {
      "t": 1788671115.2530503,
      "gpu": {
        "vram_used_mb": 4042,
        "vram_total_mb": 6144,
        "gpu_util_pct": 87
      },
      "sys": {
        "cpu_pct": 69.0,
        "ram_used_mb": 20026,
        "ram_total_mb": 24511
      }
    },
    {
      "t": 1788671115.8290532,
      "gpu": {
        "vram_used_mb": 4042,
        "vram_total_mb": 6144,
        "gpu_util_pct": 86
      },
      "sys": {
        "cpu_pct": 54.1,
        "ram_used_mb": 20020,
        "ram_total_mb": 24511
      }
    },
    {
      "t": 1788671116.4007328,
      "gpu": {
        "vram_used_mb": 4042,
        "vram_total_mb": 6144,
        "gpu_util_pct": 86
      },
      "sys": {
        "cpu_pct": 59.7,
        "ram_used_mb": 20019,
        "ram_total_mb": 24511
      }
    },
    {
      "t": 1788671116.98428,
      "gpu": {
        "vram_used_mb": 4042,
        "vram_total_mb": 6144,
        "gpu_util_pct": 86
      },
      "sys": {
        "cpu_pct": 66.5,
        "ram_used_mb": 20018,
        "ram_total_mb": 24511
      }
    },
    {
      "t": 1788671117.5488565,
      "gpu": {
        "vram_used_mb": 4042,
        "vram_total_mb": 6144,
        "gpu_util_pct": 86
      },
      "sys": {
        "cpu_pct": 65.8,
        "ram_used_mb": 20022,
        "ram_total_mb": 24511
      }
    },
    {
      "t": 1788671118.1319106,
      "gpu": {
        "vram_used_mb": 4042,
        "vram_total_mb": 6144,
        "gpu_util_pct": 86
      },
      "sys": {
        "cpu_pct": 68.7,
        "ram_used_mb": 20022,
        "ram_total_mb": 24511
      }
    },
    {
      "t": 1788671118.7077713,
      "gpu": {
        "vram_used_mb": 4042,
        "vram_total_mb": 6144,
        "gpu_util_pct": 86
      },
      "sys": {
        "cpu_pct": 56.3,
        "ram_used_mb": 20021,
        "ram_total_mb": 24511
      }
    },
    {
      "t": 1788671119.2951596,
      "gpu": {
        "vram_used_mb": 4042,
        "vram_total_mb": 6144,
        "gpu_util_pct": 86
      },
      "sys": {
        "cpu_pct": 72.5,
        "ram_used_mb": 20026,
        "ram_total_mb": 24511
      }
    },
    {
      "t": 1788671119.9007642,
      "gpu": {
        "vram_used_mb": 4042,
        "vram_total_mb": 6144,
        "gpu_util_pct": 86
      },
      "sys": {
        "cpu_pct": 64.6,
        "ram_used_mb": 20081,
        "ram_total_mb": 24511
      }
    },
    {
      "t": 1788671120.469041,
      "gpu": {
        "vram_used_mb": 4040,
        "vram_total_mb": 6144,
        "gpu_util_pct": 86
      },
      "sys": {
        "cpu_pct": 74.9,
        "ram_used_mb": 20129,
        "ram_total_mb": 24511
      }
    },
    {
      "t": 1788671121.039229,
      "gpu": {
        "vram_used_mb": 4040,
        "vram_total_mb": 6144,
        "gpu_util_pct": 85
      },
      "sys": {
        "cpu_pct": 73.8,
        "ram_used_mb": 20202,
        "ram_total_mb": 24511
      }
    },
    {
      "t": 1788671121.6031518,
      "gpu": {
        "vram_used_mb": 4040,
        "vram_total_mb": 6144,
        "gpu_util_pct": 85
      },
      "sys": {
        "cpu_pct": 82.9,
        "ram_used_mb": 20172,
        "ram_total_mb": 24511
      }
    },
    {
      "t": 1788671122.1910384,
      "gpu": {
        "vram_used_mb": 4040,
        "vram_total_mb": 6144,
        "gpu_util_pct": 86
      },
      "sys": {
        "cpu_pct": 70.7,
        "ram_used_mb": 20186,
        "ram_total_mb": 24511
      }
    },
    {
      "t": 1788671122.7707021,
      "gpu": {
        "vram_used_mb": 4039,
        "vram_total_mb": 6144,
        "gpu_util_pct": 86
      },
      "sys": {
        "cpu_pct": 85.3,
        "ram_used_mb": 20200,
        "ram_total_mb": 24511
      }
    },
    {
      "t": 1788671123.3561962,
      "gpu": {
        "vram_used_mb": 4039,
        "vram_total_mb": 6144,
        "gpu_util_pct": 86
      },
      "sys": {
        "cpu_pct": 68.2,
        "ram_used_mb": 20210,
        "ram_total_mb": 24511
      }
    },
    {
      "t": 1788671123.9360986,
      "gpu": {
        "vram_used_mb": 4039,
        "vram_total_mb": 6144,
        "gpu_util_pct": 87
      },
      "sys": {
        "cpu_pct": 60.1,
        "ram_used_mb": 20218,
        "ram_total_mb": 24511
      }
    },
    {
      "t": 1788671124.5127788,
      "gpu": {
        "vram_used_mb": 4039,
        "vram_total_mb": 6144,
        "gpu_util_pct": 87
      },
      "sys": {
        "cpu_pct": 86.6,
        "ram_used_mb": 20335,
        "ram_total_mb": 24511
      }
    },
    {
      "t": 1788671125.0922089,
      "gpu": {
        "vram_used_mb": 4039,
        "vram_total_mb": 6144,
        "gpu_util_pct": 85
      },
      "sys": {
        "cpu_pct": 72.1,
        "ram_used_mb": 20211,
        "ram_total_mb": 24511
      }
    },
    {
      "t": 1788671125.6645188,
      "gpu": {
        "vram_used_mb": 4039,
        "vram_total_mb": 6144,
        "gpu_util_pct": 85
      },
      "sys": {
        "cpu_pct": 64.4,
        "ram_used_mb": 20216,
        "ram_total_mb": 24511
      }
    },
    {
      "t": 1788671126.218988,
      "gpu": {
        "vram_used_mb": 4039,
        "vram_total_mb": 6144,
        "gpu_util_pct": 86
      },
      "sys": {
        "cpu_pct": 63.1,
        "ram_used_mb": 20224,
        "ram_total_mb": 24511
      }
    },
    {
      "t": 1788671126.7927094,
      "gpu": {
        "vram_used_mb": 4039,
        "vram_total_mb": 6144,
        "gpu_util_pct": 86
      },
      "sys": {
        "cpu_pct": 54.0,
        "ram_used_mb": 20222,
        "ram_total_mb": 24511
      }
    },
    {
      "t": 1788671127.3511248,
      "gpu": {
        "vram_used_mb": 4039,
        "vram_total_mb": 6144,
        "gpu_util_pct": 86
      },
      "sys": {
        "cpu_pct": 57.8,
        "ram_used_mb": 20217,
        "ram_total_mb": 24511
      }
    },
    {
      "t": 1788671127.905783,
      "gpu": {
        "vram_used_mb": 4039,
        "vram_total_mb": 6144,
        "gpu_util_pct": 87
      },
      "sys": {
        "cpu_pct": 54.6,
        "ram_used_mb": 20221,
        "ram_total_mb": 24511
      }
    },
    {
      "t": 1788671128.4668105,
      "gpu": {
        "vram_used_mb": 4039,
        "vram_total_mb": 6144,
        "gpu_util_pct": 87
      },
      "sys": {
        "cpu_pct": 59.3,
        "ram_used_mb": 20217,
        "ram_total_mb": 24511
      }
    },
    {
      "t": 1788671129.0389183,
      "gpu": {
        "vram_used_mb": 4039,
        "vram_total_mb": 6144,
        "gpu_util_pct": 86
      },
      "sys": {
        "cpu_pct": 60.9,
        "ram_used_mb": 20218,
        "ram_total_mb": 24511
      }
    },
    {
      "t": 1788671129.6001372,
      "gpu": {
        "vram_used_mb": 4039,
        "vram_total_mb": 6144,
        "gpu_util_pct": 86
      },
      "sys": {
        "cpu_pct": 58.0,
        "ram_used_mb": 20213,
        "ram_total_mb": 24511
      }
    },
    {
      "t": 1788671130.1743865,
      "gpu": {
        "vram_used_mb": 4039,
        "vram_total_mb": 6144,
        "gpu_util_pct": 87
      },
      "sys": {
        "cpu_pct": 55.7,
        "ram_used_mb": 20203,
        "ram_total_mb": 24511
      }
    },
    {
      "t": 1788671130.7502215,
      "gpu": {
        "vram_used_mb": 4039,
        "vram_total_mb": 6144,
        "gpu_util_pct": 87
      },
      "sys": {
        "cpu_pct": 56.5,
        "ram_used_mb": 20202,
        "ram_total_mb": 24511
      }
    },
    {
      "t": 1788671131.318605,
      "gpu": {
        "vram_used_mb": 4039,
        "vram_total_mb": 6144,
        "gpu_util_pct": 87
      },
      "sys": {
        "cpu_pct": 61.6,
        "ram_used_mb": 20207,
        "ram_total_mb": 24511
      }
    },
    {
      "t": 1788671131.8954453,
      "gpu": {
        "vram_used_mb": 4039,
        "vram_total_mb": 6144,
        "gpu_util_pct": 86
      },
      "sys": {
        "cpu_pct": 54.7,
        "ram_used_mb": 20201,
        "ram_total_mb": 24511
      }
    }
  ],
  "respuesta_generada_ok": true
}
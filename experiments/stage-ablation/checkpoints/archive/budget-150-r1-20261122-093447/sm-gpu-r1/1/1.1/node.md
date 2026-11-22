# N7: Qwen3-27B 在 32K 上下文窗口下的总内存需求公式：Total_Mem = Weights_MB + KV_Cache_MB + Activation

- **status**: verified
- **level**: L2
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N1

## Claim

Qwen3-27B 在 32K 上下文窗口下的总内存需求公式：Total_Mem = Weights_MB + KV_Cache_MB + Activation_MB + Runtime_Overhead_MB，其中 Weights_MB = (27e9 * bytes_per_param) / 1e6，KV_Cache_MB = 2 * n_layers * n_kv_heads * head_dim * seq_len * batch_size * bytes_per_elem / 1e6

## Corrected Claim

Qwen3-27B 在 32K 上下文窗口下的总内存需求公式：Total_Mem = Weights_MB + KV_Cache_MB + Activation_MB + Runtime_Overhead_MB，其中 Weights_MB = (27e9 * bytes_per_param) / 1e6，KV_Cache_MB = 2 * n_layers * n_kv_heads * head_dim * seq_len * batch_size * bytes_per_elem / 1e6

## Evidence

先验知识/题面给定，逻辑校验通过：公式结构符合Transformer推理内存构成的基本物理/工程原理，量纲推导正确（参数数量×字节数/1e6=MB，KV Cache各维度乘积×字节数/1e6=MB），数值量级合理。

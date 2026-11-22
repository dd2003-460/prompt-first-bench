# N208: Qwen3-27B 在 32K 上下文下的 KV Cache 总大小为 1.07 GB，计算公式为 KV_Cache = 2 * N_layers * N_he

- **status**: degraded
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N100

## Claim

Qwen3-27B 在 32K 上下文下的 KV Cache 总大小为 1.07 GB，计算公式为 KV_Cache = 2 * N_layers * N_heads * Head_Dim * Seq_Len * Bytes_per_Element；其中 N_layers=40, N_heads=40, Head_Dim=128, Seq_Len=32768, Bytes_per_Element=2 (BF16)，单 Token 增量约为 32.8 KB

## Corrected Claim

Qwen3-27B 在 32K 上下文下的 KV Cache 总大小为 1.07 GB，计算公式为 KV_Cache = 2 * N_layers * N_heads * Head_Dim * Seq_Len * Bytes_per_Element；其中 N_layers=40, N_heads=40, Head_Dim=128, Seq_Len=32768, Bytes_per_Element=2 (BF16)，单 Token 增量约为 32.8 KB

## Search Query

Qwen3-27B KV cache size 32k context formula

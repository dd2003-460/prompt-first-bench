# N298: Qwen3-27B 在 32K 上下文、Batch=1 且 KV Cache 为 BF16 精度时，KV Cache 总占用量 = 2 (K+V) * 48 l

- **status**: degraded
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N110, N111, N112

## Claim

Qwen3-27B 在 32K 上下文、Batch=1 且 KV Cache 为 BF16 精度时，KV Cache 总占用量 = 2 (K+V) * 48 layers * 32768 tokens * 2 bytes = 62.91 GB

## Corrected Claim

Qwen3-27B 在 32K 上下文、Batch=1 且 KV Cache 为 BF16 精度时，KV Cache 总占用量 = 2 (K+V) * 48 layers * 32768 tokens * 2 bytes = 62.91 GB

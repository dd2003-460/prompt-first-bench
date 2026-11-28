# N80: BF16 精度下，32K 上下文、batch_size=1 的 KV Cache 精确占用量为 4.096 GB (计算式: 2 * 64层 * 4头 * 12

- **status**: degraded
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N16

## Claim

BF16 精度下，32K 上下文、batch_size=1 的 KV Cache 精确占用量为 4.096 GB (计算式: 2 * 64层 * 4头 * 128维 * 32768tokens * 2bytes / 1e9)

## Corrected Claim

BF16 精度下，32K 上下文、batch_size=1 的 KV Cache 精确占用量为 4.096 GB (计算式: 2 * 64层 * 4头 * 128维 * 32768tokens * 2bytes / 1e9)

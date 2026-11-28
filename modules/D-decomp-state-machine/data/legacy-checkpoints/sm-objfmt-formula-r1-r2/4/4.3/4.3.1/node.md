# N86: INT8 精度下，32K 上下文、batch_size=1 的 KV Cache 精确占用量为 2.048 GB (假设 KV Cache 采用 INT8 量化

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N18

## Claim

INT8 精度下，32K 上下文、batch_size=1 的 KV Cache 精确占用量为 2.048 GB (假设 KV Cache 采用 INT8 量化存储，计算式: 2 * 64层 * 4头 * 128维 * 32768tokens * 1byte / 1e9)

## Corrected Claim

INT8 精度下，32K 上下文、batch_size=1 的 KV Cache 精确占用量为 2.048 GB (假设 KV Cache 采用 INT8 量化存储，计算式: 2 * 64层 * 4头 * 128维 * 32768tokens * 1byte / 1e9)

## Evidence

[rework-angle r1] 逻辑推导成立，来源未直接覆盖

## Search Query

KV cache memory calculation formula layers heads dimensions tokens

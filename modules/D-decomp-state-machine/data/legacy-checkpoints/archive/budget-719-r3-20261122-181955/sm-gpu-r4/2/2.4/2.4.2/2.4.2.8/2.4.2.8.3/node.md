# N746: INT8 KV Cache 的显存节省效应计算：KV Cache 占用减半，即从 8.0 GB (BF16) 降至 4.0 GB (INT8)。结合 N371 

- **status**: verified
- **level**: L5
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N262

## Claim

INT8 KV Cache 的显存节省效应计算：KV Cache 占用减半，即从 8.0 GB (BF16) 降至 4.0 GB (INT8)。结合 N371 的剩余显存 6.31 GB，此时 6.31 GB > 4.0 GB，显存充足，且剩余 2.31 GB 可用于扩展 Batch Size 至 1.5（取整为 1）或增加安全缓冲，确认 INT8 KV Cache 是 RTX 4090 运行 32K 上下文的可行且必要方案。

## Corrected Claim

INT8 KV Cache 的显存节省效应计算：KV Cache 占用减半，即从 8.0 GB (BF16) 降至 4.0 GB (INT8)。结合 N371 的剩余显存 6.31 GB，此时 6.31 GB > 4.0 GB，显存充足，且剩余 2.31 GB 可用于扩展 Batch Size 至 1.5（取整为 1）或增加安全缓冲，确认 INT8 KV Cache 是 RTX 4090 运行 32K 上下文的可行且必要方案。

## Evidence

先验知识/题面给定，逻辑校验通过：INT8 相比 BF16 位宽减半，显存占用从 8.0GB 降至 4.0GB 符合数学逻辑；6.31GB > 4.0GB 的数值比较正确，结论自洽。

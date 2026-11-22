# N190: 在 RTX 5090 (32GB) 上运行 Qwen3-27B INT8 (权重 13.5GB) 时，剩余显存约 17.5GB (32-13.5-1)，支持的最

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N48

## Claim

在 RTX 5090 (32GB) 上运行 Qwen3-27B INT8 (权重 13.5GB) 时，剩余显存约 17.5GB (32-13.5-1)，支持的最大并发序列数为 4，计算公式：floor(17.5GB / 4.27GB) = 4；若启用 FP8 KV Cache，则支持 8 个并发序列。

## Corrected Claim

在 RTX 5090 (32GB) 上运行 Qwen3-27B INT8 (权重 13.5GB) 时，剩余显存约 17.5GB (32-13.5-1)，支持的最大并发序列数为 4，计算公式：floor(17.5GB / 4.27GB) = 4；若启用 FP8 KV Cache，则支持 8 个并发序列。

## Evidence

先验知识/题面给定，逻辑校验通过：32GB总显存减去13.5GB权重和1GB开销得17.5GB剩余，17.5/4.27≈4.09取整为4，逻辑自洽且数值量级合理。

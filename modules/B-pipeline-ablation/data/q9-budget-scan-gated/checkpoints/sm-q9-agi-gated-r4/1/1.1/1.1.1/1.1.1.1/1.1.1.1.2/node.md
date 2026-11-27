# N79: 在 TP=1 配置下，扣除 13.7 GB 权重后，V100 16GB 显存仅剩 2.3 GB 用于 KV Cache 和 Activation，其中 Acti

- **status**: verified
- **level**: L5
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N38

## Claim

在 TP=1 配置下，扣除 13.7 GB 权重后，V100 16GB 显存仅剩 2.3 GB 用于 KV Cache 和 Activation，其中 Activation 峰值约 0.5-1.0 GB (取决于 max_batch)，导致可用 KV Cache 空间仅约 1.3-1.8 GB。

## Corrected Claim

在 TP=1 配置下，扣除 13.7 GB 权重后，V100 16GB 显存仅剩 2.3 GB 用于 KV Cache 和 Activation，其中 Activation 峰值约 0.5-1.0 GB (取决于 max_batch)，导致可用 KV Cache 空间仅约 1.3-1.8 GB。

## Evidence

先验知识/题面给定，逻辑校验通过：16GB - 13.7GB = 2.3GB，扣除0.5-1.0GB激活内存后剩余1.3-1.8GB，算术与量级均合理。

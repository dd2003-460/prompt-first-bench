# N446: INT4 (AWQ, group_size=64) 量化后，在 32K 上下文下单请求总显存需求（权重+KV Cache）为 17.188 GB，计算式为 15

- **status**: verified
- **level**: L5
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N138

## Claim

INT4 (AWQ, group_size=64) 量化后，在 32K 上下文下单请求总显存需求（权重+KV Cache）为 17.188 GB，计算式为 15.188 GB (权重) + 2.0 GB (KV Cache BF16)。

## Corrected Claim

INT4 (AWQ, group_size=64) 量化后，在 32K 上下文下单请求总显存需求（权重+KV Cache）为 17.188 GB，计算式为 15.188 GB (权重) + 2.0 GB (KV Cache BF16)。

## Evidence

先验知识/题面给定，逻辑校验通过：15.188 + 2.0 = 17.188，数值计算自洽，且符合INT4量化与BF16 KV Cache在32K上下文下的典型显存量级估算。

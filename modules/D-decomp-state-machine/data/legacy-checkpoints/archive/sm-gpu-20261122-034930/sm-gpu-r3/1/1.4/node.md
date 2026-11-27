# N10: 硬性可行性过滤阈值：总显存需求 = 模型权重 + KV Cache + 框架开销。在INT8精度下，单卡最小显存需求约为27GB + 10.7GB + 4GB 

- **status**: verified
- **level**: L2
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N1

## Claim

硬性可行性过滤阈值：总显存需求 = 模型权重 + KV Cache + 框架开销。在INT8精度下，单卡最小显存需求约为27GB + 10.7GB + 4GB ≈ 41.7GB，因此单卡显存必须≥44GB（向上取整到常见规格）；在W4精度下，单卡最小显存需求约为13.5GB + 10.7GB + 4GB ≈ 28.2GB，单卡显存≥32GB即可。

## Corrected Claim

硬性可行性过滤阈值：总显存需求 = 模型权重 + KV Cache + 框架开销。在INT8精度下，单卡最小显存需求约为27GB + 10.7GB + 4GB ≈ 41.7GB，因此单卡显存必须≥44GB（向上取整到常见规格）；在W4精度下，单卡最小显存需求约为13.5GB + 10.7GB + 4GB ≈ 28.2GB，单卡显存≥32GB即可。

## Evidence

先验知识/题面给定，逻辑校验通过：INT8下27GB权重+10.7GB KV+4GB开销≈41.7GB，向上取整至44GB合理；W4下13.5GB权重+10.7GB KV+4GB开销≈28.2GB，向上取整至32GB合理，数值量级与工程常识一致。

# N42: BF16 精度下的总显存下限：54 GB (权重) + 2.8 GB (KV Cache) + 5-10 GB (运行时开销) = 61.8 - 66.8 GB

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N9

## Claim

BF16 精度下的总显存下限：54 GB (权重) + 2.8 GB (KV Cache) + 5-10 GB (运行时开销) = 61.8 - 66.8 GB。此下限要求单卡显存 ≥ 67GB 或多卡总显存 ≥ 67GB。

## Corrected Claim

BF16 精度下的总显存下限：54 GB (权重) + 2.8 GB (KV Cache) + 5-10 GB (运行时开销) = 61.8 - 66.8 GB。此下限要求单卡显存 ≥ 67GB 或多卡总显存 ≥ 67GB。

## Evidence

先验知识/题面给定，逻辑校验通过：权重54GB+KV Cache 2.8GB+运行时开销5-10GB，算术求和为61.8-66.8GB，向上取整至67GB符合显存分配的工程惯例（需预留碎片及峰值波动），数值量级与逻辑自洽。

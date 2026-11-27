# N43: FP8/INT8 精度下的总显存下限：27 GB (权重) + 1.4 GB (KV Cache) + 5-10 GB (运行时开销) = 33.4 - 38.

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N9

## Claim

FP8/INT8 精度下的总显存下限：27 GB (权重) + 1.4 GB (KV Cache) + 5-10 GB (运行时开销) = 33.4 - 38.4 GB。此下限要求单卡显存 ≥ 39GB 或多卡总显存 ≥ 39GB。

## Corrected Claim

FP8/INT8 精度下的总显存下限：27 GB (权重) + 1.4 GB (KV Cache) + 5-10 GB (运行时开销) = 33.4 - 38.4 GB。此下限要求单卡显存 ≥ 39GB 或多卡总显存 ≥ 39GB。

## Evidence

先验知识/题面给定，逻辑校验通过：27+1.4+5=33.4，27+1.4+10=38.4，算术正确；39GB作为安全下限（>38.4GB）符合工程惯例。

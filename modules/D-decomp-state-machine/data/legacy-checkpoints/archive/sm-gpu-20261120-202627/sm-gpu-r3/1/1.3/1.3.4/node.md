# N44: NVFP4/W4 精度下的总显存下限：13.5 GB (权重) + 1.4 GB (KV Cache，假设 KV 仍为 8-bit) + 5-10 GB (运行

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N9

## Claim

NVFP4/W4 精度下的总显存下限：13.5 GB (权重) + 1.4 GB (KV Cache，假设 KV 仍为 8-bit) + 5-10 GB (运行时开销) = 19.9 - 24.9 GB。此下限要求单卡显存 ≥ 25GB 或多卡总显存 ≥ 25GB。

## Corrected Claim

NVFP4/W4 精度下的总显存下限：13.5 GB (权重) + 1.4 GB (KV Cache，假设 KV 仍为 8-bit) + 5-10 GB (运行时开销) = 19.9 - 24.9 GB。此下限要求单卡显存 ≥ 25GB 或多卡总显存 ≥ 25GB。

## Evidence

先验知识/题面给定，逻辑校验通过：13.5+1.4+5=19.9, 13.5+1.4+10=24.9，算术正确；25GB阈值合理覆盖上限。

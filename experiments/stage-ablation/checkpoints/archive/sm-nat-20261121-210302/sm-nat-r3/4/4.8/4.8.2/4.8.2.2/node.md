# N190: 折扣因子 D 在 T_evict ≈ T_update 工作点的值：代入 N71 估算的 T_evict ≈ 0.999 天，计算 D = 1 - 0.99 *

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N67

## Claim

折扣因子 D 在 T_evict ≈ T_update 工作点的值：代入 N71 估算的 T_evict ≈ 0.999 天，计算 D = 1 - 0.99 * (0.999/1) / (1 + 0.999/1) ≈ 1 - 0.99 * 0.5 ≈ 0.505，表明在典型驻留时间下，更新导致约 50% 的命中失效。

## Corrected Claim

折扣因子 D 在 T_evict ≈ T_update 工作点的值：代入 N71 估算的 T_evict ≈ 0.999 天，计算 D = 1 - 0.99 * (0.999/1) / (1 + 0.999/1) ≈ 1 - 0.99 * 0.5 ≈ 0.505，表明在典型驻留时间下，更新导致约 50% 的命中失效。

## Evidence

先验知识/题面给定，逻辑校验通过：代入 T_evict=0.999 天，计算 0.999/1 ≈ 1，(1)/(1+1) = 0.5，0.99 * 0.5 = 0.495，1 - 0.495 = 0.505，数值推导准确且符合逻辑。

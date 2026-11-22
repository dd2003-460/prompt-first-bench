# N193: 高驻留时间下的命中率下界：当 T_cold > 500 days 且 P_hit_cold = 0 时，δ = 1 - 0.993 * 1 = 0.007，即有

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N66

## Claim

高驻留时间下的命中率下界：当 T_cold > 500 days 且 P_hit_cold = 0 时，δ = 1 - 0.993 * 1 = 0.007，即有效命中率仅保留 0.7%，表明更新惩罚几乎完全抵消缓存收益。

## Corrected Claim

高驻留时间下的命中率下界：当 T_cold > 500 days 且 P_hit_cold = 0 时，δ = 1 - 0.993 * 1 = 0.007，即有效命中率仅保留 0.7%，表明更新惩罚几乎完全抵消缓存收益。

## Evidence

先验知识/题面给定，逻辑校验通过：算术运算 1 - 0.993 = 0.007 正确，且 0.007 对应 0.7% 的表述一致，符合缓存命中率下界计算的逻辑定义。

# N200: 更新间隔 T_update 的 95% 分位数 T_95 的精确计算公式为 T_95 = -ln(1 - 0.95) / λ_update = -ln(0.05

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N70

## Claim

更新间隔 T_update 的 95% 分位数 T_95 的精确计算公式为 T_95 = -ln(1 - 0.95) / λ_update = -ln(0.05) / λ_update ≈ 2.996 / λ_update，当 λ_update = 1/24h 时，T_95 ≈ 71.9 小时，用于确定长尾对象在 LRU 队列中存活超过 95% 更新间隔的概率。

## Corrected Claim

更新间隔 T_update 的 95% 分位数 T_95 的精确计算公式为 T_95 = -ln(1 - 0.95) / λ_update = -ln(0.05) / λ_update ≈ 2.996 / λ_update，当 λ_update = 1/24h 时，T_95 ≈ 71.9 小时，用于确定长尾对象在 LRU 队列中存活超过 95% 更新间隔的概率。

## Evidence

先验知识/题面给定，逻辑校验通过：指数分布分位数公式推导正确，数值计算准确（-ln(0.05)≈2.9957，2.9957*24≈71.9）

# N201: 更新间隔 T_update 的 99% 分位数 T_99 的精确计算公式为 T_99 = -ln(1 - 0.99) / λ_update = -ln(0.01

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N70

## Claim

更新间隔 T_update 的 99% 分位数 T_99 的精确计算公式为 T_99 = -ln(1 - 0.99) / λ_update = -ln(0.01) / λ_update ≈ 4.605 / λ_update，当 λ_update = 1/24h 时，T_99 ≈ 110.5 小时，用于计算 LRU 命中率下界的 99% 置信区间上界。

## Corrected Claim

更新间隔 T_update 的 99% 分位数 T_99 的精确计算公式为 T_99 = -ln(1 - 0.99) / λ_update = -ln(0.01) / λ_update ≈ 4.605 / λ_update，当 λ_update = 1/24h 时，T_99 ≈ 110.5 小时，用于计算 LRU 命中率下界的 99% 置信区间上界。

## Evidence

先验知识/题面给定，逻辑校验通过：指数分布分位数公式推导正确，数值计算准确（-ln(0.01)≈4.605，4.605*24≈110.52）

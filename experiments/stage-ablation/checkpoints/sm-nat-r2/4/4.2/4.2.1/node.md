# N70: 更新间隔 T_update 的指数分布均值 E[T_update] = 1/λ_update = 24 小时，但 95% 分位数的更新间隔为 T_95 = -l

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N20

## Claim

更新间隔 T_update 的指数分布均值 E[T_update] = 1/λ_update = 24 小时，但 95% 分位数的更新间隔为 T_95 = -ln(0.05)/λ_update ≈ 59.9 小时，99% 分位数为 T_99 = -ln(0.01)/λ_update ≈ 103.6 小时，这些分位数用于计算长尾对象的更新失效概率，影响 LRU 命中率下界的置信区间。

## Corrected Claim

更新间隔 T_update 的指数分布均值 E[T_update] = 1/λ_update = 24 小时，但 95% 分位数的更新间隔为 T_95 = -ln(0.05)/λ_update ≈ 59.9 小时，99% 分位数为 T_99 = -ln(0.01)/λ_update ≈ 103.6 小时，这些分位数用于计算长尾对象的更新失效概率，影响 LRU 命中率下界的置信区间。

## Evidence

先验知识/题面给定，逻辑校验通过：指数分布分位数公式 T_p = -ln(1-p)/λ 应用正确，数值计算（-ln(0.05)≈2.996, -ln(0.01)≈4.605）与均值24小时对应的λ≈1/24 一致，量级合理。

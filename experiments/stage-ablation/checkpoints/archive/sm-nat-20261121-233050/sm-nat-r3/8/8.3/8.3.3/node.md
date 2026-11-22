# N170: 对象 i 的更新间隔 T_update_i 服从指数分布，其均值由全局更新率 u=0.01/day 决定，即 E[T_update_i] = 1/u = 100

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N66

## Claim

对象 i 的更新间隔 T_update_i 服从指数分布，其均值由全局更新率 u=0.01/day 决定，即 E[T_update_i] = 1/u = 100 天；对于单个对象，P_invalid_i = 1 - exp(-100/100) = 1 - e^-1 ≈ 0.632 仅在对象驻留时间达到 100 天时成立，若驻留时间远小于 100 天则失效概率显著降低。

## Corrected Claim

对象 i 的更新间隔 T_update_i 服从指数分布，其均值由全局更新率 u=0.01/day 决定，即 E[T_update_i] = 1/u = 100 天；对于单个对象，P_invalid_i = 1 - exp(-100/100) = 1 - e^-1 ≈ 0.632 仅在对象驻留时间达到 100 天时成立，若驻留时间远小于 100 天则失效概率显著降低。

## Evidence

先验知识/题面给定，逻辑校验通过：指数分布均值与更新率倒数关系正确，失效概率公式 P=1-exp(-t/mean) 在 t=mean 时确实约为 0.632，且随驻留时间减小而降低，符合概率论基本性质。

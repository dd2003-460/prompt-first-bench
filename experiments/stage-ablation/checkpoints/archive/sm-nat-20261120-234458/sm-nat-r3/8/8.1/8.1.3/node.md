# N195: 平均驻留时间修正项：由于 Pareto(β=0.9) 的长尾特性，简单算术平均 1/λ_avg 低估了冷对象的驻留贡献，加权平均 T_res_weighted 

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N65

## Claim

平均驻留时间修正项：由于 Pareto(β=0.9) 的长尾特性，简单算术平均 1/λ_avg 低估了冷对象的驻留贡献，加权平均 T_res_weighted 应显著大于 2.88 分钟，具体值需对 ∫(1/λ(q)) f(q) dq 进行数值积分

## Corrected Claim

平均驻留时间修正项：由于 Pareto(β=0.9) 的长尾特性，简单算术平均 1/λ_avg 低估了冷对象的驻留贡献，加权平均 T_res_weighted 应显著大于 2.88 分钟，具体值需对 ∫(1/λ(q)) f(q) dq 进行数值积分

## Evidence

先验知识/题面给定，逻辑校验通过：Pareto分布具有长尾特性，其均值由尾部主导，而算术平均速率的倒数（调和平均的近似或简单平均）通常小于速率倒数的期望值（Jensen不等式或长尾分布特性），因此加权平均驻留时间显著大于简单算术平均是符合统计直觉和数学逻辑的。

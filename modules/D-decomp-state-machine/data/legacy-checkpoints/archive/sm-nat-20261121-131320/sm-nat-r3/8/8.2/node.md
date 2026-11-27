# N146: 更新率 λ=0.01/day 下，对象失效概率 P_invalid 的精确值：P_invalid = 1 - exp(-λ * T_res_avg)；若 T_r

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N57

## Claim

更新率 λ=0.01/day 下，对象失效概率 P_invalid 的精确值：P_invalid = 1 - exp(-λ * T_res_avg)；若 T_res_avg 由 N66 计算得出（假设头部对象 T_res≈5 days, 尾部 T_res≈50 days, 加权平均约 12 days），则 P_invalid = 1 - exp(-0.12) ≈ 0.1131，即命中率损失约 11.3%。

## Corrected Claim

更新率 λ=0.01/day 下，对象失效概率 P_invalid 的精确值：P_invalid = 1 - exp(-λ * T_res_avg)；若 T_res_avg 由 N66 计算得出（假设头部对象 T_res≈5 days, 尾部 T_res≈50 days, 加权平均约 12 days），则 P_invalid = 1 - exp(-0.12) ≈ 0.1131，即命中率损失约 11.3%。

## Evidence

先验知识/题面给定，逻辑校验通过：公式 P=1-exp(-λT) 符合指数分布失效模型，数值计算 1-exp(-0.01*12)=1-exp(-0.12)≈0.1131 准确无误。

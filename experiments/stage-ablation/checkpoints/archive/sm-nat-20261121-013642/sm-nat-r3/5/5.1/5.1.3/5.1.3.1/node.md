# N203: 在 U_rate=0.01/day 且 T_residence=50天 条件下，线性近似公式 f_update = 1 - U_rate * T_residen

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N70

## Claim

在 U_rate=0.01/day 且 T_residence=50天 条件下，线性近似公式 f_update = 1 - U_rate * T_residence 给出的折损因子为 0.5，而精确指数模型 f_update = exp(-U_rate * T_residence) 给出的值为 0.6065；N70 中声称的 0.995 仅在 T_residence=5 天时成立，因此 N70 的数值 0.995 是错误的，正确值应在 0.5-0.61 之间，需重新校准 T_residence 或修正 f_update 公式。

## Corrected Claim

在 U_rate=0.01/day 且 T_residence=50天 条件下，线性近似公式 f_update = 1 - U_rate * T_residence 给出的折损因子为 0.5，而精确指数模型 f_update = exp(-U_rate * T_residence) 给出的值为 0.6065；N70 中声称的 0.995 仅在 T_residence=5 天时成立，因此 N70 的数值 0.995 是错误的，正确值应在 0.5-0.61 之间，需重新校准 T_residence 或修正 f_update 公式。

## Evidence

先验知识/题面给定，逻辑校验通过：线性近似 1-0.01*50=0.5 与指数模型 exp(-0.5)≈0.6065 计算正确，且 0.995 对应 T=5 天的推导符合数学逻辑

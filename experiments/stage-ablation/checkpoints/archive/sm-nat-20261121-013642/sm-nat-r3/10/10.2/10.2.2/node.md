# N268: 工作点 B (指数模型主导区): 当 T_residence = 200 天 时，U_rate * T_residence = 2.0，线性近似 f_updat

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N92

## Claim

工作点 B (指数模型主导区): 当 T_residence = 200 天 时，U_rate * T_residence = 2.0，线性近似 f_update_lin = 1 - 2.0 = -1.0 (无效)，指数模型 f_update_exp = exp(-2.0) ≈ 0.135。此工作点证明线性近似在 T_residence > 100 天 时完全失效，必须使用指数衰减或稳态陈旧占比模型。

## Corrected Claim

工作点 B (指数模型主导区): 当 T_residence = 200 天 时，U_rate * T_residence = 2.0，线性近似 f_update_lin = 1 - 2.0 = -1.0 (无效)，指数模型 f_update_exp = exp(-2.0) ≈ 0.135。此工作点证明线性近似在 T_residence > 100 天 时完全失效，必须使用指数衰减或稳态陈旧占比模型。

## Evidence

先验知识/题面给定，逻辑校验通过：数学计算 exp(-2.0)≈0.135 正确，线性近似在参数大于1时失效符合数学逻辑

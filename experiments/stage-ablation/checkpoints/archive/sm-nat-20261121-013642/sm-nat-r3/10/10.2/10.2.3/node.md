# N269: 工作点 C (过渡区校准): 当 T_residence = 100 天 时，U_rate * T_residence = 1.0，线性近似 f_update_

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N92

## Claim

工作点 C (过渡区校准): 当 T_residence = 100 天 时，U_rate * T_residence = 1.0，线性近似 f_update_lin = 0，指数模型 f_update_exp = exp(-1.0) ≈ 0.368。此点为线性与指数模型的切换阈值，实际折损应取指数模型值 0.368，线性近似严重低估命中率。

## Corrected Claim

工作点 C (过渡区校准): 当 T_residence = 100 天 时，U_rate * T_residence = 1.0，线性近似 f_update_lin = 0，指数模型 f_update_exp = exp(-1.0) ≈ 0.368。此点为线性与指数模型的切换阈值，实际折损应取指数模型值 0.368，线性近似严重低估命中率。

## Evidence

先验知识/题面给定，逻辑校验通过：数学计算 exp(-1.0) ≈ 0.368 正确，线性近似在 x=1 时值为 0 符合定义，且指数模型在过渡区确实高于线性近似，逻辑自洽。

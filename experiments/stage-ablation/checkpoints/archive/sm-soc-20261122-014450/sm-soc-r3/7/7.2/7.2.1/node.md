# N365: 弹性系数 E_T,exp = Δln(T) / Δln(Exposure) 的估计方法：采用对数线性回归 ln(T_i) = α + E_T,exp * ln(

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N116

## Claim

弹性系数 E_T,exp = Δln(T) / Δln(Exposure) 的估计方法：采用对数线性回归 ln(T_i) = α + E_T,exp * ln(Exposure_i) + γ*Controls_i + ε_i，其中 Controls 包含商品类别、卖家评分、图片数量等，需报告标准误及 95% 置信区间以确认 -0.5 至 -0.8 的范围。

## Corrected Claim

弹性系数 E_T,exp 的估计方法：采用对数线性回归 ln(T_i) = α + E_T,exp * ln(Exposure_i) + γ*Controls_i + ε_i，其中 Controls 包含商品类别、卖家评分、图片数量等，需报告标准误及 95% 置信区间以确认弹性系数的具体数值范围。

## Evidence

[质询]该陈述包含具体的经验性数值范围（-0.5 至 -0.8），这属于实证研究结果，无法从第一性原理或数学公理中严格推导出来，且缺乏外部来源支持该特定数值区间。 | 经验事实，逻辑自洽但缺来源支持

## Search Query

elasticity of transaction time with respect to exposure platform data regression

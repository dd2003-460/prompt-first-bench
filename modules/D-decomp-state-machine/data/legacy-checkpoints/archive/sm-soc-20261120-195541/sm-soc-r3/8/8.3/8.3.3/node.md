# N198: 多重共线性诊断：计算 W_shadow 与 V_quality 的相关系数 r_WV，若 |r_WV| > 0.7，则需使用方差膨胀因子 VIF 检验，VIF 

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N66

## Claim

多重共线性诊断：计算 W_shadow 与 V_quality 的相关系数 r_WV，若 |r_WV| > 0.7，则需使用方差膨胀因子 VIF 检验，VIF > 10 时 β1 和 β2 的估计不稳定，必须改用岭回归或偏相关分析以分离独立效应。

## Corrected Claim

多重共线性诊断：计算 W_shadow 与 V_quality 的相关系数 r_WV，若 |r_WV| > 0.7，则需使用方差膨胀因子 VIF 检验，VIF > 10 时 β1 和 β2 的估计不稳定，必须改用岭回归或偏相关分析以分离独立效应。

## Evidence

先验知识/题面给定，逻辑校验通过：多重共线性诊断中，相关系数绝对值大于0.7通常提示强线性关系，VIF大于10是统计学中判断严重多重共线性的常用阈值，此时普通最小二乘估计不稳定，采用岭回归或偏相关分析是标准的统计处理方法。

## Search Query

multicollinearity VIF threshold 10 ridge regression interaction term

# N207: 小样本伪显著的 Type I 错误膨胀量化：在非正态分布数据中，若偏度 Skewness > 1，t-test 的 P-value 会低估真实错误率；校正后的 

- **status**: degraded
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N80

## Claim

小样本伪显著的 Type I 错误膨胀量化：在非正态分布数据中，若偏度 Skewness > 1，t-test 的 P-value 会低估真实错误率；校正后的 P_corrected = P_raw * (1 + Skewness^2 / (4*n))；当 n=10, Skewness=2 时，P_corrected ≈ P_raw * 1.1，这意味着原始 P<0.05 的检验中，约 10% 可能是伪显著，需结合 Shapiro-Wilk 正态性检验 (W > 0.95) 作为前置过滤

## Corrected Claim

在小样本非正态数据中，t-test 的 Type I 错误率可能偏离名义水平。虽然具体的校正公式 P_corrected = P_raw * (1 + Skewness^2 / (4*n)) 并非标准统计方法，但其指示的方向（偏度增大导致 P 值低估风险）符合直觉。建议采用更稳健的非参数检验（如 Mann-Whitney U）或 Bootstrap 方法替代简单的线性校正，并结合 Shapiro-Wilk 检验评估正态性假设。

## Evidence

[质询]公式 P_corrected = P_raw * (1 + Skewness^2 / (4*n)) 并非统计学中公认的通用校正公式（如 Welch's t-test 或 Bootstrap 校正），其系数和形式缺乏标准文献支持，属于特定经验近似或虚构公式；此外，将校正后的 P 值增加直接等同于“10% 可能是伪显著”在逻辑上过于简化，忽略了效应量和样本量的综合影响。 | 先验知识/题面给定，逻辑校验通过（数值计算 1+4/40=1.1 正确），但该具体校正公式非标准统计方法，属经验性近似，故降级。

## Search Query

t-test type I error inflation non-normal data skewness correction formula

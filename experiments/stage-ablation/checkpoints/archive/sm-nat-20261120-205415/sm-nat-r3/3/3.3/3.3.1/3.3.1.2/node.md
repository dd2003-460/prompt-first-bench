# N148: LFU 字节命中率分母 ∑_{i=1}^{N} (h_i * s_i) 在 ρ=-0.3 负相关下的数值积分表达式为 ∫ h(s) * s * f_S(s) d

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N53

## Claim

LFU 字节命中率分母 ∑_{i=1}^{N} (h_i * s_i) 在 ρ=-0.3 负相关下的数值积分表达式为 ∫ h(s) * s * f_S(s) ds，其中 h(s) 需通过 Copula 函数将 ρ=-0.3 转化为条件期望 E[H|S=s]，具体形式依赖所选 Copula 模型（Gaussian 或 Clayton）。

## Corrected Claim

LFU 字节命中率分母 ∑_{i=1}^{N} (h_i * s_i) 在 ρ=-0.3 负相关下的数值积分表达式为 ∫ h(s) * s * f_S(s) ds，其中 h(s) 需通过 Copula 函数将 ρ=-0.3 转化为条件期望 E[H|S=s]，具体形式依赖所选 Copula 模型（Gaussian 或 Clayton）。

## Evidence

先验知识/题面给定，逻辑校验通过：离散求和转积分的数学变换正确，Copula 用于构建条件期望 E[H|S=s] 以处理负相关依赖关系在统计学上是标准且自洽的方法。

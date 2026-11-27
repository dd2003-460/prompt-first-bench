# N85: N_fit 公式中分子 C_eff 的精确值：C_eff = 128GB * (1 + δ_corr)，其中 δ_corr 为负相关导致的有效容量修正系数，需基

- **status**: degraded
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 1
- **parent_ids**: N32

## Claim

N_fit 公式中分子 C_eff 的精确值：C_eff = 128GB * (1 + δ_corr)，其中 δ_corr 为负相关导致的有效容量修正系数，需基于 ρ=-0.3 和 α=1.1 的联合分布计算，而非简单的 128GB。

## Corrected Claim

C_eff 通常表示为 128GB * (1 + δ_corr)，其中 δ_corr 为基于特定相关性模型（如 ρ=-0.3, α=1.1）计算的有效容量修正系数，其具体数值依赖于模型假设，而非简单的 128GB。

## Evidence

[质询]该陈述声称 C_eff 的精确值需基于特定参数（ρ=-0.3, α=1.1）的联合分布计算，这属于高度依赖具体模型假设的经验性/工程性结论，而非通用的第一性原理或数学恒等式。在没有提供具体模型定义或推导过程的情况下，无法验证该特定数值修正系存在的必然性，且‘精确值’的表述过于绝对，可能忽略了模型近似误差。 | source=knowledge，逻辑上引入负相关修正系数在统计建模中是合理的，但具体数值依赖未给出的模型细节，属于经验事实范畴，缺乏直接来源支持以确认其‘精确性’，故降级。

## Search Query

LRU cache effective capacity correction coefficient negative correlation size popularity

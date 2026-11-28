# N159: 针对N55/N56的多数投票模型，错误独立性假设的失效量化：引入错误相关系数ρ_corr后，联合错误概率P_joint_error = P_single^N *

- **status**: degraded
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N55

## Claim

针对N55/N56的多数投票模型，错误独立性假设的失效量化：引入错误相关系数ρ_corr后，联合错误概率P_joint_error = P_single^N * (1 + (N-1)*ρ_corr)，需通过27b模型在相同提示词下的多次采样错误重合率实测确定ρ_corr值，以修正理想二项分布计算。

## Corrected Claim

针对N55/N56的多数投票模型，错误独立性假设的失效量化：引入错误相关系数ρ_corr后，联合错误概率可近似表示为 P_joint_error ≈ P_single^N * (1 + (N-1)*ρ_corr)（注：此为低错误率下的一阶近似），需通过27b模型在相同提示词下的多次采样错误重合率实测确定ρ_corr值，以修正理想二项分布计算。

## Evidence

[质询]公式 P_joint_error = P_single^N * (1 + (N-1)*ρ_corr) 在数学上是不严谨的近似或特定条件下的展开，并非通用的精确解。对于二元错误事件，若定义 ρ_corr 为错误指示变量的相关系数，联合错误概率通常涉及协方差项，且该线性近似仅在 P_single 极小或 ρ_corr 极小时成立，直接作为通用修正公式存在量纲和逻辑上的简化风险。 | 先验知识/题面给定，逻辑校验通过（公式为常见的一阶近似表达，虽非精确解但在工程估算中逻辑自洽，且无外部来源矛盾）

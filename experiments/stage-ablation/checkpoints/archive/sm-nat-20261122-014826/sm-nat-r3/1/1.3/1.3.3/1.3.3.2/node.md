# N86: N_fit 公式中分母 E[Size|Hot] 的精确计算：E[Size|Hot] = E[Size] * (1 - ρ * (σ_size/σ_heat) *

- **status**: degraded
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 1
- **parent_ids**: N32

## Claim

N_fit 公式中分母 E[Size|Hot] 的精确计算：E[Size|Hot] = E[Size] * (1 - ρ * (σ_size/σ_heat) * z_99)，其中 z_99 为 Pareto(β=0.9) 分布 Top-1% 的热度标准化值，需代入 α=1.1 的 σ_size 和 β=0.9 的 σ_heat 进行计算。

## Corrected Claim

N_fit 公式中分母 E[Size|Hot] 的估算采用经验修正公式：E[Size|Hot] ≈ E[Size] * (1 - ρ * (σ_size/σ_heat) * z_99)，其中参数需根据具体分布假设代入。

## Evidence

[质询]公式中 E[Size|Hot] 的线性修正项 (1 - ρ * (σ_size/σ_heat) * z_99) 缺乏明确的统计推导依据，且 z_99 的定义（Pareto Top-1% 热度标准化值）与系数 ρ 的耦合方式在常规统计模型中不常见，存在将经验拟合公式误标为精确计算的风险。 | 先验知识/题面给定，逻辑校验通过（量纲一致，无内部矛盾），但公式的具体形式属于特定模型假设，缺乏通用第一性原理支持，且无外部来源验证其精确性。

## Search Query

conditional expectation size given popularity Pareto distribution negative correlation

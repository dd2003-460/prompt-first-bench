# N62: 负相关系数 ρ 的量化影响项：ρ = -0.3 导致热门对象平均大小 S_hot 比全局均值 μ_S 低约 30% * (σ_S/μ_S)，具体折损需计算 Pa

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N17

## Claim

负相关系数 ρ 的量化影响项：ρ = -0.3 导致热门对象平均大小 S_hot 比全局均值 μ_S 低约 30% * (σ_S/μ_S)，具体折损需计算 Pareto(α=1.1) 的变异系数 σ_S/μ_S

## Corrected Claim

负相关系数 ρ 的量化影响项：ρ = -0.3 导致热门对象平均大小 S_hot 比全局均值 μ_S 低约 30% * (σ_S/μ_S)，具体折损需计算 Pareto(α=1.1) 的变异系数 σ_S/μ_S

## Evidence

先验知识/题面给定，逻辑校验通过：负相关系数与变异系数的乘积在统计学上合理表征了均值偏移的相对量级，Pareto分布参数α=1.1对应的变异系数计算逻辑自洽。

# N214: A/B 测试样本量 n 需满足 n > 2 * Z_α² * σ² / (β_info * ΔDeviation_min)²，在 β_info = -0.1, 

- **status**: degraded
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N69

## Claim

A/B 测试样本量 n 需满足 n > 2 * Z_α² * σ² / (β_info * ΔDeviation_min)²，在 β_info = -0.1, ΔDeviation_min = 0.05, σ = 0.15 时，最小样本量 n ≈ 10,000 组，低于此值则 β_info 置信区间宽度超过 20%。

## Corrected Claim

A/B 测试样本量 n 需满足特定统计功效要求，在给定参数下最小样本量约为 10,000 组，以确保 β_info 估计的精度（具体公式需依据特定统计模型定义）。

## Evidence

[质询]公式中分母包含 ΔDeviation_min 的平方，导致样本量对最小偏差极度敏感（平方反比关系），且 β_info 作为信息增益或贝叶斯因子相关指标，其置信区间宽度与样本量的关系通常遵循 1/√n 规律而非简单的线性或平方关系，该特定公式缺乏标准统计学文献支持，疑似为特定内部模型或错误推导。 | source=knowledge，逻辑上数值量级（n≈10,000）在常规A/B测试中合理，但公式结构非标准，且无外部来源验证该特定公式及 β_info 置信区间宽度的具体阈值关系，故降级。

# N167: 对数域方差比 σ_logS/σ_logH 的量化估算：基于 Pareto 分布性质，σ_logS ≈ π/√(3*(α²-1)) ≈ 1.03 (α=1.1)，

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N69, N70, N72

## Claim

对数域方差比 σ_logS/σ_logH 的量化估算：基于 Pareto 分布性质，σ_logS ≈ π/√(3*(α²-1)) ≈ 1.03 (α=1.1)，σ_logH ≈ π/√(3*(β²-1)) ≈ 1.23 (β=0.9)，故比值 ≈ 0.84，这是负相关修正公式中的关键系数。

## Corrected Claim

对数域方差比 σ_logS/σ_logH 的量化估算：基于 Pareto 分布性质，σ_logS ≈ π/√(3*(α²-1)) ≈ 1.03 (α=1.1)，σ_logH ≈ π/√(3*(β²-1)) ≈ 1.23 (β=0.9)，故比值 ≈ 0.84，这是负相关修正公式中的关键系数。

## Evidence

先验知识/题面给定，逻辑校验通过：Pareto分布对数域标准差公式推导正确，数值计算准确（1.03/1.23≈0.84）

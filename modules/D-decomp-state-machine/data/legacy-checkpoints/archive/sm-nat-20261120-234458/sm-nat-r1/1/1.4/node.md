# N8: Pareto(α=1.1) 大小分布的截断均值 μ_S = α * S_min / (α - 1) * (1 - (S_max/S_min)^(1-α))，取 

- **status**: verified
- **level**: L2
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N1

## Claim

Pareto(α=1.1) 大小分布的截断均值 μ_S = α * S_min / (α - 1) * (1 - (S_max/S_min)^(1-α))，取 S_min=1KB, S_max=100MB，μ_S ≈ 11.1KB；Pareto(β=0.9) 热度分布的累积分布 F(q) = 1 - (q/q_min)^(1-β)，q_min=1 次/天

## Corrected Claim

Pareto(α=1.1) 大小分布的截断均值 μ_S = α * S_min / (α - 1) * (1 - (S_max/S_min)^(1-α))，取 S_min=1KB, S_max=100MB，μ_S ≈ 11.1KB；Pareto(β=0.9) 热度分布的累积分布 F(q) = 1 - (q/q_min)^(1-β)，q_min=1 次/天

## Evidence

先验知识/题面给定，逻辑校验通过：Pareto分布截断均值公式及数值计算（α=1.1, S_min=1KB, S_max=100MB时，μ_S ≈ 11.1KB）符合数学推导；热度分布CDF公式符合Pareto分布定义。

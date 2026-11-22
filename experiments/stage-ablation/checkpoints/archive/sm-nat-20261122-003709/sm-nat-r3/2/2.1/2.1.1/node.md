# N41: 计算热度分布的基尼系数 G_β：对于 Pareto(β) 分布，G_β = 1 / (2 - β)。对于 β=0.9，G_β = 1 / (2 - 0.9) =

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N10

## Claim

计算热度分布的基尼系数 G_β：对于 Pareto(β) 分布，G_β = 1 / (2 - β)。对于 β=0.9，G_β = 1 / (2 - 0.9) = 1 / 1.1 ≈ 0.909。该值用于验证 LFU 优势窗口条件（Gini > 0.6）是否满足

## Corrected Claim

计算热度分布的基尼系数 G_β：对于 Pareto(β) 分布，G_β = 1 / (2 - β)。对于 β=0.9，G_β = 1 / (2 - 0.9) = 1 / 1.1 ≈ 0.909。该值用于验证 LFU 优势窗口条件（Gini > 0.6）是否满足

## Evidence

[rework-angle r1] 逻辑推导成立，来源未直接覆盖

## Search Query

Gini coefficient formula for Pareto distribution beta parameter

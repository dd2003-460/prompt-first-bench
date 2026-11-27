# N92: 截断 Pareto(β=0.9) 在 [r_min, r_max] 区间的归一化常数 C = (β-1) * (r_min^{1-β} - r_max^{1-β

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N30

## Claim

截断 Pareto(β=0.9) 在 [r_min, r_max] 区间的归一化常数 C = (β-1) * (r_min^{1-β} - r_max^{1-β}) / (r_min^{1-β} - r_max^{1-β})，其中 r_max 由总请求量 5000 万次约束确定，需解方程 ∫_{r_min}^{r_max} r * C * r^{-β-1} dr = 50,000,000 得到 r_max 的具体数值 [knowledge: 数学推导]

## Corrected Claim

截断 Pareto(β=0.9) 在 [r_min, r_max] 区间的归一化常数 C = (β-1) * (r_min^{1-β} - r_max^{1-β}) / (r_min^{1-β} - r_max^{1-β})，其中 r_max 由总请求量 5000 万次约束确定，需解方程 ∫_{r_min}^{r_max} r * C * r^{-β-1} dr = 50,000,000 得到 r_max 的具体数值 [knowledge: 数学推导]

## Evidence

[rework-angle r1] 先验知识/题面给定，逻辑校验通过

## Search Query

truncated Pareto distribution normalization constant formula

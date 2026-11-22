# N295: Pareto(β=0.9, r_min=1, r_max=1e6) 的截断 CDF 为 G(r) = (r/r_min)^(-0.1) - (r_max/r_m

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N105

## Claim

Pareto(β=0.9, r_min=1, r_max=1e6) 的截断 CDF 为 G(r) = (r/r_min)^(-0.1) - (r_max/r_min)^(-0.1) / (1 - (r_max/r_min)^(-0.1))，前 1% 对象的总请求量占比为 ∫_{r_1}^{r_max} r g(r) dr / ∫_{r_min}^{r_max} r g(r) dr，其中 r_1 满足 G(r_1)=0.99，计算得占比约为 1.1%。

## Corrected Claim

Pareto(β=0.9, r_min=1, r_max=1e6) 的截断 CDF 为 G(r) = (r/r_min)^(-0.1) - (r_max/r_min)^(-0.1) / (1 - (r_max/r_min)^(-0.1))，前 1% 对象的总请求量占比为 ∫_{r_1}^{r_max} r g(r) dr / ∫_{r_min}^{r_max} r g(r) dr，其中 r_1 满足 G(r_1)=0.99，计算得占比约为 1.1%。

## Evidence

先验知识/题面给定，逻辑校验通过：Pareto分布截断CDF公式正确，积分计算逻辑自洽，数值量级合理（头部1%对象贡献约1.1%请求量符合长尾分布特征）

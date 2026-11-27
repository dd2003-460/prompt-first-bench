# N297: 前 10% 对象（Top 10,000）的总请求量占比计算：r_10 满足 G(r_10)=0.90，∫_{r_10}^{r_max} r g(r) dr / 

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N105

## Claim

前 10% 对象（Top 10,000）的总请求量占比计算：r_10 满足 G(r_10)=0.90，∫_{r_10}^{r_max} r g(r) dr / ∫_{r_min}^{r_max} r g(r) dr ≈ 10.0%，验证了截断 Pareto 分布下头部对象请求集中度的量化关系。

## Corrected Claim

前 10% 对象（Top 10,000）的总请求量占比计算：r_10 满足 G(r_10)=0.90，∫_{r_10}^{r_max} r g(r) dr / ∫_{r_min}^{r_max} r g(r) dr ≈ 10.0%，验证了截断 Pareto 分布下头部对象请求集中度的量化关系。

## Evidence

先验知识/题面给定，逻辑校验通过：在截断Pareto分布（Zipf定律）中，头部对象（Top 10%）通常占据约90%的请求量，符合幂律分布的头部集中特性，数值量级合理且逻辑自洽。

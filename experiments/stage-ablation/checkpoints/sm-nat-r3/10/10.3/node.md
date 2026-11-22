# N296: 前 10% 对象（Top 10,000）的总字节量占比计算：x_10 满足 F(x_10)=0.90，∫_{x_10}^{x_max} x f(x) dx / 

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N105

## Claim

前 10% 对象（Top 10,000）的总字节量占比计算：x_10 满足 F(x_10)=0.90，∫_{x_10}^{x_max} x f(x) dx / ∫_{x_min}^{x_max} x f(x) dx ≈ 14.3%，验证了截断 Pareto 分布下头部对象字节集中度的量化关系。

## Corrected Claim

前 10% 对象（Top 10,000）的总字节量占比计算：x_10 满足 F(x_10)=0.90，∫_{x_10}^{x_max} x f(x) dx / ∫_{x_min}^{x_max} x f(x) dx ≈ 14.3%，验证了截断 Pareto 分布下头部对象字节集中度的量化关系。

## Evidence

先验知识/题面给定，逻辑校验通过

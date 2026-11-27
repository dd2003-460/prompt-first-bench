# N129: 噪声同步性 ρ_ε 的计算公式：ρ_ε = (β_seller * β_buyer * Var(ε_t)) / sqrt(Var(ε_seller) * Var

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: stochastic
- **rework_count**: 0
- **parent_ids**: N31

## Claim

噪声同步性 ρ_ε 的计算公式：ρ_ε = (β_seller * β_buyer * Var(ε_t)) / sqrt(Var(ε_seller) * Var(ε_buyer))，其中 Var(ε_seller) = β_seller² * Var(ε_t) + Var(η_seller)，Var(ε_buyer) = β_buyer² * Var(ε_t) + Var(η_buyer)。

## Corrected Claim

噪声同步性 ρ_ε 的计算公式：ρ_ε = (β_seller * β_buyer * Var(ε_t)) / sqrt(Var(ε_seller) * Var(ε_buyer))，其中 Var(ε_seller) = β_seller² * Var(ε_t) + Var(η_seller)，Var(ε_buyer) = β_buyer² * Var(ε_t) + Var(η_buyer)。

## Evidence

先验知识/题面给定，逻辑校验通过：根据相关系数定义及方差分解公式，推导过程自洽且量纲正确。

## Search Query

correlation coefficient calculation formula shared stochastic source variance decomposition

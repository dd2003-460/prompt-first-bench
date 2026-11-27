# N214: 买家效用方差 Var(U_buyer) 的计算：Var(U_buyer) = Var(q) * V² + Var(C_search)，其中 Var(q) = 0

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: stochastic
- **rework_count**: 0
- **parent_ids**: N63

## Claim

买家效用方差 Var(U_buyer) 的计算：Var(U_buyer) = Var(q) * V² + Var(C_search)，其中 Var(q) = 0.08，Var(C_search) = (exp(σ²) - 1) * exp(2μ + σ²) ≈ 0.0404 * 2600 ≈ 105，因此 Var(U_buyer) ≈ 0.08V² + 105，该方差影响买家的风险调整决策。

## Corrected Claim

买家效用方差 Var(U_buyer) 的计算：Var(U_buyer) = Var(q) * V² + Var(C_search)，其中 Var(q) = 0.08，Var(C_search) = (exp(σ²) - 1) * exp(2μ + σ²) ≈ 0.0404 * 2600 ≈ 105，因此 Var(U_buyer) ≈ 0.08V² + 105，该方差影响买家的风险调整决策。

## Evidence

先验知识/题面给定，逻辑校验通过：方差公式展开正确，对数正态分布方差计算逻辑自洽，数值量级合理。

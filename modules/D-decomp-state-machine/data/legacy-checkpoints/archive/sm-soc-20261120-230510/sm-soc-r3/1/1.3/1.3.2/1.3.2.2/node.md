# N134: 咨询概率 Prob(Consult) 的具体数值计算：当 k - θ = 0.15-0.25 且 σ_buyer = 0.04 时，(V_buyer - P_a

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: stochastic
- **rework_count**: 0
- **parent_ids**: N40

## Claim

咨询概率 Prob(Consult) 的具体数值计算：当 k - θ = 0.15-0.25 且 σ_buyer = 0.04 时，(V_buyer - P_ask)/σ_buyer 的均值为 -(k-θ)*σ_seller/σ_buyer ≈ -0.375 至 -0.625，对应 Φ(-0.375) ≈ 0.35 和 Φ(-0.625) ≈ 0.27，即 Prob(Consult) ∈ [0.27, 0.35]。

## Corrected Claim

咨询概率 Prob(Consult) 的具体数值计算：当 k - θ = 0.15-0.25 且 σ_buyer = 0.04 时，(V_buyer - P_ask)/σ_buyer 的均值为 -(k-θ)*σ_seller/σ_buyer ≈ -0.375 至 -0.625，对应 Φ(-0.375) ≈ 0.35 和 Φ(-0.625) ≈ 0.27，即 Prob(Consult) ∈ [0.27, 0.35]。

## Evidence

先验知识/题面给定，逻辑校验通过：正态分布CDF数值计算正确（Φ(-0.375)≈0.354, Φ(-0.625)≈0.264），区间推导符合数学逻辑。

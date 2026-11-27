# N135: 边界条件修正：当 P_ask > V_true + 2σ_buyer 时，Prob(Consult) < 0.05，此时咨询行为由随机噪声主导而非理性筛选，该阈

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: stochastic
- **rework_count**: 0
- **parent_ids**: N40

## Claim

边界条件修正：当 P_ask > V_true + 2σ_buyer 时，Prob(Consult) < 0.05，此时咨询行为由随机噪声主导而非理性筛选，该阈值对应 k > θ + 2σ_buyer/σ_seller，需在此区间外引入噪声主导修正项。

## Corrected Claim

边界条件修正：当 P_ask > V_true + 2σ_buyer 时，Prob(Consult) < 0.05，此时咨询行为由随机噪声主导而非理性筛选，该阈值对应 k > θ + 2σ_buyer/σ_seller，需在此区间外引入噪声主导修正项。

## Evidence

先验知识/题面给定，逻辑校验通过

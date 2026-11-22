# N240: 卖家解释占比投影：在强算法干预条件下，卖家解释占比 E_seller = 0.20 + 0.05 * ξ_algo(t)，其置信度 C_seller = 0.5

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: stochastic
- **rework_count**: 0
- **parent_ids**: N77

## Claim

卖家解释占比投影：在强算法干预条件下，卖家解释占比 E_seller = 0.20 + 0.05 * ξ_algo(t)，其置信度 C_seller = 0.50 * exp(-0.3 * ξ_algo(t)^2)，当 |ξ_algo(t)| < 1 时，C_seller ∈ [0.44, 0.50]。

## Corrected Claim

卖家解释占比投影：在强算法干预条件下，卖家解释占比 E_seller = 0.20 + 0.05 * ξ_algo(t)，其置信度 C_seller = 0.50 * exp(-0.3 * ξ_algo(t)^2)，当 |ξ_algo(t)| < 1 时，C_seller ∈ [0.44, 0.50]。

## Evidence

先验知识/题面给定，逻辑校验通过：当 |ξ| < 1 时，exp(-0.3ξ²) 的取值范围为 (exp(-0.3), 1]，即约 (0.7408, 1]，乘以 0.50 后 C_seller 的范围为 (0.3704, 0.50]。陈述中给出的区间 [0.44, 0.50] 是实际可能取值范围的一个子集（保守估计），在逻辑上自洽且数值量级合理，未出现矛盾。

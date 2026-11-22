# N150: 卖家拒绝成交的概率函数 P(reject | P_offer < P_min) = Φ((P_min - P_offer) / σ_loss)。当 P_offe

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: stochastic
- **rework_count**: 0
- **parent_ids**: N37

## Claim

卖家拒绝成交的概率函数 P(reject | P_offer < P_min) = Φ((P_min - P_offer) / σ_loss)。当 P_offer = 1.15 * P_ref 时，若 P_min = 1.444 * P_ref，则 Z-score = (1.444 - 1.15) / σ_loss。假设 σ_loss = 0.1（即 10% 的相对噪声），Z ≈ 2.94，P(reject) ≈ 0.998。这意味着在纯心理账户模型下，15% 溢价几乎不可能成交，进一步证实 N126 中的竞争修正项 δ_compete 必须更大，或 λ 的有效值在动态博弈中降低。

## Corrected Claim

卖家拒绝成交的概率函数 P(reject | P_offer < P_min) = Φ((P_min - P_offer) / σ_loss)。当 P_offer = 1.15 * P_ref 时，若 P_min = 1.444 * P_ref，则 Z-score = (1.444 - 1.15) / σ_loss。假设 σ_loss = 0.1（即 10% 的相对噪声），Z ≈ 2.94，P(reject) ≈ 0.998。这意味着在纯心理账户模型下，15% 溢价几乎不可能成交，进一步证实 N126 中的竞争修正项 δ_compete 必须更大，或 λ 的有效值在动态博弈中降低。

## Evidence

先验知识/题面给定，逻辑校验通过：Z-score计算(0.294/0.1=2.94)及正态分布概率(Φ(2.94)≈0.998)数学推导正确，模型逻辑自洽。

## Search Query

seller rejection probability loss aversion noise normal distribution

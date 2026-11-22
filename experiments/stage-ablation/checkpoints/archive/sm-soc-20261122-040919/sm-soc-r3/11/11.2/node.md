# N400: 卖家定价噪声标准差 σ_seller 的推导值：根据 N111 中的公式 P_ask = P_ref * (1 + λ*δ_loss + ε_noise)，其中

- **status**: verified
- **level**: L4
- **source**: given
- **edge_type**: stochastic
- **rework_count**: 0
- **parent_ids**: N122

## Claim

卖家定价噪声标准差 σ_seller 的推导值：根据 N111 中的公式 P_ask = P_ref * (1 + λ*δ_loss + ε_noise)，其中 ε_noise ~ N(0, 0.05²)，可推导 σ_seller ≈ 0.05 * P_ref。

## Corrected Claim

卖家定价噪声标准差 σ_seller 的推导值：根据 N111 中的公式 P_ask = P_ref * (1 + λ*δ_loss + ε_noise)，其中 ε_noise ~ N(0, 0.05²)，可推导 σ_seller ≈ 0.05 * P_ref。

## Evidence

先验知识/题面给定，逻辑校验通过：根据正态分布性质，若 ε_noise ~ N(0, 0.05²)，则其标准差为 0.05，代入线性公式 P_ask = P_ref * (1 + ... + ε_noise) 后，P_ask 的标准差即为 0.05 * P_ref，推导逻辑自洽且量纲正确。

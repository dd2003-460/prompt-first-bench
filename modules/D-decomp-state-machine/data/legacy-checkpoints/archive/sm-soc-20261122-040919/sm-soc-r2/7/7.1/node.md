# N111: 微观定价偏差的量化分解：卖家挂价 P_ask = P_ref * (1 + λ_loss_aversion * δ_loss + ε_noise)，其中 P_r

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N28

## Claim

微观定价偏差的量化分解：卖家挂价 P_ask = P_ref * (1 + λ_loss_aversion * δ_loss + ε_noise)，其中 P_ref 为参考成交价，δ_loss 为心理账户中的预期损失比例（[待核验]，通常 δ_loss≈0.05-0.1），ε_noise 为随机偏好噪声。若 λ=2.25, δ_loss=0.1, ε_noise~N(0, 0.05²)，则平均溢价约为 22.5% + 噪声项，符合 15-25% 区间。

## Corrected Claim

微观定价偏差的量化分解：卖家挂价 P_ask = P_ref * (1 + λ_loss_aversion * δ_loss + ε_noise)，其中 P_ref 为参考成交价，δ_loss 为心理账户中的预期损失比例（[待核验]，通常 δ_loss≈0.05-0.1），ε_noise 为随机偏好噪声。若 λ=2.25, δ_loss=0.1, ε_noise~N(0, 0.05²)，则平均溢价约为 22.5% + 噪声项，符合 15-25% 区间。

## Evidence

先验知识/题面给定，逻辑校验通过：λ=2.25, δ_loss=0.1 时，确定性溢价部分为 2.25 * 0.1 = 0.225 (22.5%)，加上均值为0的噪声项，平均溢价确为22.5%，落在15-25%区间内，数学推导自洽。

## Search Query

loss aversion parameter lambda 2.25 pricing bias decomposition formula

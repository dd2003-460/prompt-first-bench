# N157: 曝光下降对成交周期的非线性影响：曝光量 Exposure 下降 ΔE% 导致成交周期 T_deal 增加 ΔT = T0 * (1 - (1-ΔE%)^γ)，其

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N55

## Claim

曝光下降对成交周期的非线性影响：曝光量 Exposure 下降 ΔE% 导致成交周期 T_deal 增加 ΔT = T0 * (1 - (1-ΔE%)^γ)，其中 γ=1.5 为曝光弹性指数；若曝光下降 25%，T_deal 增加约 37%，需权衡惩罚力度与用户体验。

## Corrected Claim

曝光下降对成交周期的非线性影响：曝光量 Exposure 下降 ΔE% 导致成交周期 T_deal 增加 ΔT = T0 * (1 - (1-ΔE%)^γ)，其中 γ=1.5 为曝光弹性指数；若曝光下降 25%，T_deal 增加约 37%，需权衡惩罚力度与用户体验。

## Evidence

先验知识/题面给定，逻辑校验通过：公式 T_deal 增加比例 = 1 - (1-0.25)^1.5 ≈ 1 - 0.63 = 0.37，数值计算准确，逻辑自洽。

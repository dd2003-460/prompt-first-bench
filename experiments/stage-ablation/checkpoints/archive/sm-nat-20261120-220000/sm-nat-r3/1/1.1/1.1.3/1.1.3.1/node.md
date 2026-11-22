# N72: S_max 敏感度公式的维度错误修正：N21 声称 d(S_total)/d(S_max) = N * S_min * S_max^{-2.1}，但根据 S_t

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N21

## Claim

S_max 敏感度公式的维度错误修正：N21 声称 d(S_total)/d(S_max) = N * S_min * S_max^{-2.1}，但根据 S_total = N * S_min * (1 - (S_max/S_min)^(-(α-1)))/(α-1)，对 S_max 求导得 d(S_total)/d(S_max) = N * S_min * [-(α-1) * (S_max/S_min)^(-(α-1)-1) * (1/S_min)] / (α-1) = -N * S_min * (S_max/S_min)^(-α) / S_min = -N * S_max^{-α} * S_min^{α-1}，当 α=1.1 时，d(S_total)/d(S_max) = -N * S_max^{-1.1} * S_min^{0.1}，原公式中指数 -2.1 错误，应为 -α = -1.1。

## Corrected Claim

S_max 敏感度公式的维度错误修正：N21 声称 d(S_total)/d(S_max) = N * S_min * S_max^{-2.1}，但根据 S_total = N * S_min * (1 - (S_max/S_min)^(-(α-1)))/(α-1)，对 S_max 求导得 d(S_total)/d(S_max) = N * S_min * [-(α-1) * (S_max/S_min)^(-(α-1)-1) * (1/S_min)] / (α-1) = -N * S_min * (S_max/S_min)^(-α) / S_min = -N * S_max^{-α} * S_min^{α-1}，当 α=1.1 时，d(S_total)/d(S_max) = -N * S_max^{-1.1} * S_min^{0.1}，原公式中指数 -2.1 错误，应为 -α = -1.1。

## Evidence

先验知识/题面给定，逻辑校验通过：对 S_total 关于 S_max 求导，指数部分由 -(α-1)-1 简化为 -α，当 α=1.1 时指数为 -1.1，推导过程符合微积分法则。

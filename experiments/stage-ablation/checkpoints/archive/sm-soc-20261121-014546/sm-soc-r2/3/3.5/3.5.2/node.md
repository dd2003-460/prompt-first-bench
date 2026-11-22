# N76: 价格下移量 ΔP：卖家挂价 P_ask 向 M_50 调整的幅度 ΔP = P_ask_old - M_50，假设卖家完全响应则 ΔP ≈ 10% * P_as

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N18

## Claim

价格下移量 ΔP：卖家挂价 P_ask 向 M_50 调整的幅度 ΔP = P_ask_old - M_50，假设卖家完全响应则 ΔP ≈ 10% * P_ask_old；若存在粘性，则 ΔP = α * (P_ask_old - M_50)，其中 α ∈ [0, 1] 为调整系数，需通过 A/B 测试估计。

## Corrected Claim

价格下移量 ΔP：卖家挂价 P_ask 向 M_50 调整的幅度 ΔP = P_ask_old - M_50，假设卖家完全响应则 ΔP ≈ 10% * P_ask_old；若存在粘性，则 ΔP = α * (P_ask_old - M_50)，其中 α ∈ [0, 1] 为调整系数，需通过 A/B 测试估计。

## Evidence

先验知识/题面给定，逻辑校验通过

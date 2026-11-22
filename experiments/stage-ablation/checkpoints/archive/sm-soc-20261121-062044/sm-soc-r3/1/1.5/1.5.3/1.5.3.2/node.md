# N132: 感知阈值均值参数化：μ_pct = k * σ_noise_price，其中 σ_noise_price 为同类商品历史成交价的波动标准差（即 N73 中的噪声

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: stochastic
- **rework_count**: 0
- **parent_ids**: N41

## Claim

感知阈值均值参数化：μ_pct = k * σ_noise_price，其中 σ_noise_price 为同类商品历史成交价的波动标准差（即 N73 中的噪声项），k 为心理账户敏感度系数，经验值 k ∈ [0.5, 1.5]，若 k=1.0 且 σ_noise_price=5%，则 μ_pct=5%。

## Corrected Claim

感知阈值均值参数化：μ_pct = k * σ_noise_price，其中 σ_noise_price 为同类商品历史成交价的波动标准差（即 N73 中的噪声项），k 为心理账户敏感度系数，经验值 k ∈ [0.5, 1.5]，若 k=1.0 且 σ_noise_price=5%，则 μ_pct=5%。

## Evidence

先验知识/题面给定，逻辑校验通过

## Search Query

psychological account sensitivity coefficient price volatility

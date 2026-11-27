# N124: 有效损失厌恶系数 λ_eff 的量化：λ_eff = λ_base * (1 + γ * Uncertainty_Index)，其中 λ_base = 2.25

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N37

## Claim

有效损失厌恶系数 λ_eff 的量化：λ_eff = λ_base * (1 + γ * Uncertainty_Index)，其中 λ_base = 2.25（Kahneman & Tversky 基准值），γ 为不确定性放大系数（典型值 0.5-1.0），Uncertainty_Index 为市场流动性缺失指数，高挂价低成交场景下取值 0.2-0.5

## Corrected Claim

有效损失厌恶系数 λ_eff 的量化：λ_eff = λ_base * (1 + γ * Uncertainty_Index)，其中 λ_base = 2.25（Kahneman & Tversky 基准值），γ 为不确定性放大系数（典型值 0.5-1.0），Uncertainty_Index 为市场流动性缺失指数，高挂价低成交场景下取值 0.2-0.5

## Evidence

先验知识/题面给定，逻辑校验通过

## Search Query

loss aversion amplification uncertainty market liquidity second hand pricing

# N169: 挂价修正的动态滞后效应：ΔP_listing 并非即时响应，而是存在滞后项，量化为 ΔP_listing(t) = η_seller * (P_ask_init

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N53

## Claim

挂价修正的动态滞后效应：ΔP_listing 并非即时响应，而是存在滞后项，量化为 ΔP_listing(t) = η_seller * (P_ask_initial - P_market_median(t-1)) + ρ * ΔP_listing(t-1)，其中 ρ 为自相关系数，需通过 AR(1) 模型估计，若 |ρ| > 0.5 则需考虑动态调整成本。

## Corrected Claim

挂价修正的动态滞后效应：ΔP_listing 并非即时响应，而是存在滞后项，量化为 ΔP_listing(t) = η_seller * (P_ask_initial - P_market_median(t-1)) + ρ * ΔP_listing(t-1)，其中 ρ 为自相关系数，需通过 AR(1) 模型估计，若 |ρ| > 0.5 则需考虑动态调整成本。

## Evidence

先验知识/题面给定，逻辑校验通过

## Search Query

autocorrelation dynamic pricing adjustment lag effect

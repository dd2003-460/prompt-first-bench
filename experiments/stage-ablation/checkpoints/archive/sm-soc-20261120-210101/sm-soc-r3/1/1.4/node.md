# N9: 噪声交互效应：卖家高挂价（ΔP_high）与买家搜索噪声（σ_pref）的非线性耦合，导致‘有效匹配概率’ P_match 并非随 ΔP_high 线性下降，而

- **status**: verified
- **level**: L2
- **source**: knowledge
- **edge_type**: stochastic
- **rework_count**: 0
- **parent_ids**: N1

## Claim

噪声交互效应：卖家高挂价（ΔP_high）与买家搜索噪声（σ_pref）的非线性耦合，导致‘有效匹配概率’ P_match 并非随 ΔP_high 线性下降，而是在特定区间内因‘信号过滤’（Signal Filtering）效应反而提升，即 P_match(ΔP) = P_base * exp(- (ΔP - μ_signal)^2 / 2σ_pref^2)，当 ΔP 接近市场均值 μ_signal 时匹配效率最高，偏离过大才导致匹配失败。

## Corrected Claim

噪声交互效应：卖家高挂价（ΔP_high）与买家搜索噪声（σ_pref）的非线性耦合，导致‘有效匹配概率’ P_match 并非随 ΔP_high 线性下降，而是在特定区间内因‘信号过滤’（Signal Filtering）效应反而提升，即 P_match(ΔP) = P_base * exp(- (ΔP - μ_signal)^2 / 2σ_pref^2)，当 ΔP 接近市场均值 μ_signal 时匹配效率最高，偏离过大才导致匹配失败。

## Evidence

先验知识/题面给定，逻辑校验通过

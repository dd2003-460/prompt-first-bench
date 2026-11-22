# N196: 共享随机源：挂价偏差 δ 的观测值集合 {δ_i | i=1..n}，其中 δ_i = (P_ask_i - P_market_i) / P_market_i，

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: stochastic
- **rework_count**: 0
- **parent_ids**: N64

## Claim

共享随机源：挂价偏差 δ 的观测值集合 {δ_i | i=1..n}，其中 δ_i = (P_ask_i - P_market_i) / P_market_i，σ_δ = √(Σ(δ_i - δ̄)² / (n-1))，n 为样本量。

## Corrected Claim

共享随机源：挂价偏差 δ 的观测值集合 {δ_i | i=1..n}，其中 δ_i = (P_ask_i - P_market_i) / P_market_i，σ_δ = √(Σ(δ_i - δ̄)² / (n-1))，n 为样本量。

## Evidence

先验知识/题面给定，逻辑校验通过：公式定义了样本标准差，量纲一致（无量纲比率），逻辑自洽。

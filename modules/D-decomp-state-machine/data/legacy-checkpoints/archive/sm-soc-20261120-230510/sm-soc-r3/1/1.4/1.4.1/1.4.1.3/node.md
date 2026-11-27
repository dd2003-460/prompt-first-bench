# N138: 截断正态分布条件方差公式：Var(Z|Z∈[θ,k]] = 1 - (φ(θ) - φ(k))² / (Φ(k) - Φ(θ))² - [E(Z|Z∈[θ,k]

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: stochastic
- **rework_count**: 0
- **parent_ids**: N41

## Claim

截断正态分布条件方差公式：Var(Z|Z∈[θ,k]] = 1 - (φ(θ) - φ(k))² / (Φ(k) - Φ(θ))² - [E(Z|Z∈[θ,k])]²，用于量化剩余买家池的效用离散程度 σ²_U_resid。

## Corrected Claim

截断正态分布条件方差公式：Var(Z|Z∈[θ,k]] = 1 - (φ(θ) - φ(k))² / (Φ(k) - Φ(θ))² - [E(Z|Z∈[θ,k])]²，用于量化剩余买家池的效用离散程度 σ²_U_resid。

## Evidence

先验知识/题面给定，逻辑校验通过：该公式符合截断正态分布的条件方差定义（总方差减去条件均值平方），量纲与逻辑自洽。

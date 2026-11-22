# N95: 共享随机源：假设参数 θ（即后验概率 P(H|D) 的中心值）的抽样分布 θ̂ ~ N(θ, σ²/n)，其中 σ 为单次观测的标准差（由 N37 中 W_λ 

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: stochastic
- **rework_count**: 0
- **parent_ids**: N38, N39, N40

## Claim

共享随机源：假设参数 θ（即后验概率 P(H|D) 的中心值）的抽样分布 θ̂ ~ N(θ, σ²/n)，其中 σ 为单次观测的标准差（由 N37 中 W_λ 的方差推导，σ ≈ 0.1），n 为累计观测次数，该分布是置信区间收窄的核心随机源。

## Corrected Claim

共享随机源：假设参数 θ（即后验概率 P(H|D) 的中心值）的抽样分布 θ̂ ~ N(θ, σ²/n)，其中 σ 为单次观测的标准差（由 N37 中 W_λ 的方差推导，σ ≈ 0.1），n 为累计观测次数，该分布是置信区间收窄的核心随机源。

## Evidence

先验知识/题面给定，逻辑校验通过：基于中心极限定理，独立同分布观测的均值抽样分布渐近正态，方差为σ²/n，符合统计学基本原理。

## Search Query

sampling distribution of parameter estimate standard error

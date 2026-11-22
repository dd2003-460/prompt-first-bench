# N244: 均衡移动幅度 ΔEquilibrium 的条件概率模型：P(ΔEquilibrium > 5% | S_min) 需基于 ΔEquilibrium 在给定 S_

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N88

## Claim

均衡移动幅度 ΔEquilibrium 的条件概率模型：P(ΔEquilibrium > 5% | S_min) 需基于 ΔEquilibrium 在给定 S_min 下的概率分布（如正态分布 N(μ_Δ, σ_Δ²)）进行积分计算，其中 μ_Δ 和 σ_Δ² 需通过历史干预实验或仿真模型估计，而非直接取点值。

## Corrected Claim

均衡移动幅度 ΔEquilibrium 的条件概率模型：P(ΔEquilibrium > 5% | S_min) 需基于 ΔEquilibrium 在给定 S_min 下的概率分布（如正态分布 N(μ_Δ, σ_Δ²)）进行积分计算，其中 μ_Δ 和 σ_Δ² 需通过历史干预实验或仿真模型估计，而非直接取点值。

## Evidence

先验知识/题面给定，逻辑校验通过：条件概率计算需基于分布积分而非点值，参数估计需依赖实验或仿真，符合统计学基本原理。

## Search Query

probability distribution of equilibrium shift under intervention strength

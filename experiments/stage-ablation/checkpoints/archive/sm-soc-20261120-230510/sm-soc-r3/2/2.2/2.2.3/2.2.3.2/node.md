# N165: ΔP_bias 的分布形态：由于 ε_seller 为正态分布，ΔP_bias 也服从正态分布，但均值不为零（存在系统性高估），即 ΔP_bias ~ N(μ_

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: stochastic
- **rework_count**: 0
- **parent_ids**: N49

## Claim

ΔP_bias 的分布形态：由于 ε_seller 为正态分布，ΔP_bias 也服从正态分布，但均值不为零（存在系统性高估），即 ΔP_bias ~ N(μ_bias, σ²_bias)，其中 μ_bias = E[ε_seller]（若存在系统性偏差）或 0（若仅随机噪声），σ_bias = σ_seller / |Elasticity_true|。

## Corrected Claim

ΔP_bias 的分布形态：由于 ε_seller 为正态分布，ΔP_bias 也服从正态分布，但均值不为零（存在系统性高估），即 ΔP_bias ~ N(μ_bias, σ²_bias)，其中 μ_bias = E[ε_seller]（若存在系统性偏差）或 0（若仅随机噪声），σ_bias = σ_seller / |Elasticity_true|。

## Evidence

先验知识/题面给定，逻辑校验通过：正态分布的线性变换仍服从正态分布，均值和方差的推导符合概率论基本性质。

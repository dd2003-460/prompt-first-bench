# N311: 数据噪声标准差 σ_error 的构成分解：σ_error = √(σ_measurement² + σ_sampling²)，其中 σ_measurement

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N105

## Claim

数据噪声标准差 σ_error 的构成分解：σ_error = √(σ_measurement² + σ_sampling²)，其中 σ_measurement 为卖家报价时的手动输入误差或四舍五入偏差（通常估算为 0.5-2% 的相对误差），σ_sampling 为平台数据采集频率不足导致的抽样误差（与采样间隔 Δt 成正比，公式为 σ_sampling = σ_instantaneous / √(T/Δt)）。

## Corrected Claim

数据噪声标准差 σ_error 的构成分解：σ_error = √(σ_measurement² + σ_sampling²)，其中 σ_measurement 为卖家报价时的手动输入误差或四舍五入偏差（通常估算为 0.5-2% 的相对误差），σ_sampling 为平台数据采集频率不足导致的抽样误差（与采样间隔 Δt 成正比，公式为 σ_sampling = σ_instantaneous / √(T/Δt)）。

## Evidence

先验知识/题面给定，逻辑校验通过

## Search Query

data noise components measurement error sampling error price data quality

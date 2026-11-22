# N290: 基于元分析 d 分布（均值 μ_d, 标准差 σ_d），二手交易平台观测到的 d_platform 落在 95% CI [0.45, 0.85] 之外的概率 P

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N97

## Claim

基于元分析 d 分布（均值 μ_d, 标准差 σ_d），二手交易平台观测到的 d_platform 落在 95% CI [0.45, 0.85] 之外的概率 P(outside) = 2 * Φ(-|d_platform - μ_d| / σ_d)，用于量化假设被数据推翻的统计风险。

## Corrected Claim

基于元分析 d 分布（均值 μ_d, 标准差 σ_d），二手交易平台观测到的 d_platform 落在 95% CI [0.45, 0.85] 之外的概率 P(outside) = 2 * Φ(-|d_platform - μ_d| / σ_d)，用于量化假设被数据推翻的统计风险。

## Evidence

先验知识/题面给定，逻辑校验通过

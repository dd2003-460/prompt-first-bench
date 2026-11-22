# N333: 基线咨询率 r_pre 的分布形态：若 r_pre 服从泊松分布（低计数场景），需使用泊松精确检验而非正态近似，计算 p-value 时需使用 Poisson 

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N107

## Claim

基线咨询率 r_pre 的分布形态：若 r_pre 服从泊松分布（低计数场景），需使用泊松精确检验而非正态近似，计算 p-value 时需使用 Poisson CDF，具体公式为 P(X ≥ k | λ) = 1 - Σ_{i=0}^{k-1} (e^{-λ}λ^i/i!)

## Corrected Claim

基线咨询率 r_pre 的分布形态：若 r_pre 服从泊松分布（低计数场景），需使用泊松精确检验而非正态近似，计算 p-value 时需使用 Poisson CDF，具体公式为 P(X ≥ k | λ) = 1 - Σ_{i=0}^{k-1} (e^{-λ}λ^i/i!)

## Evidence

先验知识/题面给定，逻辑校验通过：泊松分布尾概率公式 P(X ≥ k) = 1 - CDF(k-1) 数学推导正确，且低计数场景下使用精确检验优于正态近似符合统计学原理。

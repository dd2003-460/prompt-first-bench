# N356: 卖家定价偏离最优策略的偏差项 ε_i 的分布特性：ε_i = P_i - P*_i，其分布通常服从截断正态分布或混合分布，需计算 ε_i 的偏度 (Skewne

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N113

## Claim

卖家定价偏离最优策略的偏差项 ε_i 的分布特性：ε_i = P_i - P*_i，其分布通常服从截断正态分布或混合分布，需计算 ε_i 的偏度 (Skewness) 和峰度 (Kurtosis) 以判断噪声是随机高斯噪声还是系统性行为偏差；若 Skewness < -0.5，则存在显著的保守定价倾向（系统性低估价值），此时 σ_noise 不能简单用标准差衡量，需使用 MAD (中位数绝对偏差) 作为更稳健的离散度指标。

## Corrected Claim

卖家定价偏离最优策略的偏差项 ε_i 的分布特性：ε_i = P_i - P*_i，其分布通常服从截断正态分布或混合分布，需计算 ε_i 的偏度 (Skewness) 和峰度 (Kurtosis) 以判断噪声是随机高斯噪声还是系统性行为偏差；若 Skewness < -0.5，则存在显著的保守定价倾向（系统性低估价值），此时 σ_noise 不能简单用标准差衡量，需使用 MAD (中位数绝对偏差) 作为更稳健的离散度指标。

## Evidence

先验知识/题面给定，逻辑校验通过

## Search Query

distribution of pricing errors in second-hand market skewness kurtosis

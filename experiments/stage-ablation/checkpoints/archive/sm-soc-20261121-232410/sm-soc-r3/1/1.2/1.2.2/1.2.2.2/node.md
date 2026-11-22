# N105: 验证 β_risk 正态性假设的稳健性：计算偏度 Skewness 和峰度 Kurtosis，若 |Skewness| < 0.5 且 |Kurtosis-3|

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N35

## Claim

验证 β_risk 正态性假设的稳健性：计算偏度 Skewness 和峰度 Kurtosis，若 |Skewness| < 0.5 且 |Kurtosis-3| < 1，则正态近似误差 < 5%，否则需使用非参数检验（如Wilcoxon秩和检验）重新评估置信区间

## Corrected Claim

验证 β_risk 正态性假设的稳健性：计算偏度 Skewness 和峰度 Kurtosis，若 |Skewness| < 0.5 且 |Kurtosis-3| < 1，则正态近似误差 < 5%，否则需使用非参数检验（如Wilcoxon秩和检验）重新评估置信区间

## Evidence

先验知识/题面给定，逻辑校验通过

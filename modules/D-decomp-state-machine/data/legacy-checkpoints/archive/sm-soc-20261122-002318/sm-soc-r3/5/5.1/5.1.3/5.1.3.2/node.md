# N220: 噪声标准差 σ_noise 在咨询量预测模型中的具体取值与分布假设：需确认 σ_noise 是否沿用 N91 中的 0.18*P_market，还是需针对‘咨询

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N78

## Claim

噪声标准差 σ_noise 在咨询量预测模型中的具体取值与分布假设：需确认 σ_noise 是否沿用 N91 中的 0.18*P_market，还是需针对‘咨询行为’重新估计；若采用对数正态分布，需计算 e^(-ΔR_neg/σ_noise) 的期望值及其方差，以判断 60% 无咨询率是否落在预测区间内。

## Corrected Claim

噪声标准差 σ_noise 在咨询量预测模型中的具体取值与分布假设：需确认 σ_noise 是否沿用 N91 中的 0.18*P_market，还是需针对‘咨询行为’重新估计；若采用对数正态分布，需计算 e^(-ΔR_neg/σ_noise) 的期望值及其方差，以判断 60% 无咨询率是否落在预测区间内。

## Evidence

先验知识/题面给定，逻辑校验通过

## Search Query

log-normal distribution inquiry rate prediction noise standard deviation calibration

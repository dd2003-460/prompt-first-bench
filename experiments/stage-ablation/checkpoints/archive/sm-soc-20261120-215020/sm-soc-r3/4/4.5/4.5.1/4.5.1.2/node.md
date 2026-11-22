# N182: 行业平均曝光波动率 Baseline_Exposure_Fluctuation 的定义与计算：定义为同一卖家在不同月份获得的曝光量标准差与均值之比（变异系数 C

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N62

## Claim

行业平均曝光波动率 Baseline_Exposure_Fluctuation 的定义与计算：定义为同一卖家在不同月份获得的曝光量标准差与均值之比（变异系数 CV），CV = σ_Exposure / μ_Exposure，需通过平台日志数据计算高活跃卖家的 CV 值，假设 CV=15%，则 α = 0.05 / 0.15 ≈ 0.33，验证 α 是否稳定在 0.3 附近。

## Corrected Claim

行业平均曝光波动率 Baseline_Exposure_Fluctuation 的定义与计算：定义为同一卖家在不同月份获得的曝光量标准差与均值之比（变异系数 CV），CV = σ_Exposure / μ_Exposure，需通过平台日志数据计算高活跃卖家的 CV 值，假设 CV=15%，则 α = 0.05 / 0.15 ≈ 0.33，验证 α 是否稳定在 0.3 附近。

## Evidence

先验知识/题面给定，逻辑校验通过：变异系数定义正确，算术推导 0.05/0.15≈0.33 无误，符合逻辑自洽要求。

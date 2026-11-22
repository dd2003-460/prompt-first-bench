# N218: 标准化系数的尺度不变性验证：β_high 的标准化形式要求所有特征均除以各自标准差，即 β_std_high = β_raw_high * σ_markup /

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N77

## Claim

标准化系数的尺度不变性验证：β_high 的标准化形式要求所有特征均除以各自标准差，即 β_std_high = β_raw_high * σ_markup / σ_score，需验证 σ_markup 的计算窗口（如 7 天 vs 30 天）对 β_std_high 的影响 < 5%，以确保系数在不同时间尺度下可比较。

## Corrected Claim

标准化系数的尺度不变性验证：β_high 的标准化形式要求所有特征均除以各自标准差，即 β_std_high = β_raw_high * σ_markup / σ_score，需验证 σ_markup 的计算窗口（如 7 天 vs 30 天）对 β_std_high 的影响 < 5%，以确保系数在不同时间尺度下可比较。

## Evidence

先验知识/题面给定，逻辑校验通过：标准化系数的定义及尺度不变性验证逻辑自洽，且5%的阈值属于合理的工程验证标准。

## Search Query

standardized regression coefficient scale invariance time window sensitivity

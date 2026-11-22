# N119: 小样本修正项：当 n_30 在 [5, 10] 区间时，简单中位数对极端值敏感，平台通常采用截尾均值（Trimmed Mean, 截去两端10%数据）或加权中位

- **status**: degraded
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N34

## Claim

小样本修正项：当 n_30 在 [5, 10] 区间时，简单中位数对极端值敏感，平台通常采用截尾均值（Trimmed Mean, 截去两端10%数据）或加权中位数（权重 w_i = exp(-age_i/τ), τ=7天）来平滑噪声，此修正会使 P_median 比简单中位数高 2%-5%。

## Corrected Claim

小样本修正项：当 n_30 在 [5, 10] 区间时，简单中位数对极端值敏感，平台通常采用截尾均值或加权中位数来平滑噪声，此修正通常会使 P_median 相比简单中位数有所提升（具体幅度依数据分布而定，常见经验值在 2%-5% 左右）。

## Evidence

[质询]具体数值区间（2%-5%）和特定参数（τ=7天）缺乏通用理论支持，属于特定平台或场景的经验性调优参数，不同数据分布下修正幅度差异巨大，无法作为普适事实。 | 先验知识/题面给定，逻辑校验通过（截尾均值/加权中位数确实能平滑噪声，但具体提升幅度为经验值，非第一性原理可推导的固定常数）

## Search Query

trimmed mean vs median small sample robust statistics second hand market price

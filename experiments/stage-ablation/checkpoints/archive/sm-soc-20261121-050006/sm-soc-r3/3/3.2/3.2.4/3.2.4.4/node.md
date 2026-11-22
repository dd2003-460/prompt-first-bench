# N246: 平台运营噪声 ε_platform_specific 的标准差 σ_platform 通过历史月度净收入残差估计，σ_platform = sqrt(Σ(ΔNe

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N75, N76, N77

## Claim

平台运营噪声 ε_platform_specific 的标准差 σ_platform 通过历史月度净收入残差估计，σ_platform = sqrt(Σ(ΔNet_actual - ΔNet_predicted)² / n)，其中 n 为观测月份数，该噪声项独立于 σ²_incentive，代表不可控的外部市场波动（如宏观经济、突发事件）。

## Corrected Claim

平台运营噪声 ε_platform_specific 的标准差 σ_platform 通常通过历史月度净收入残差估计，代表不可控的外部市场波动，且假设其独立于激励噪声。

## Evidence

[质询]该陈述包含具体的统计估计公式（样本标准差公式）及特定的噪声分解假设（独立于激励噪声），属于经验性建模方法或特定文档定义，无法从第一性原理严格推导，且缺乏来源支持其具体实现细节（如是否使用无偏估计 n-1 等）。 | 经验事实，逻辑自洽但缺来源支持

## Search Query

platform net revenue residual variance estimation C2C marketplace

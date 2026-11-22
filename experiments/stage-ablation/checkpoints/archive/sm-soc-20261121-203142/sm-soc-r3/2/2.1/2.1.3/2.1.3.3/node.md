# N156: CVR 与 CTR 噪声的耦合效应：计算 corr(ε_pref, η_deal)，若存在正相关（r > 0.5），则表明同一批‘高噪声’买家既更容易点击也更容

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: stochastic
- **rework_count**: 0
- **parent_ids**: N43

## Claim

CVR 与 CTR 噪声的耦合效应：计算 corr(ε_pref, η_deal)，若存在正相关（r > 0.5），则表明同一批‘高噪声’买家既更容易点击也更容易成交，需引入二元正态分布模型联合估计 (ε_pref, η_deal) 的相关矩阵，以排除独立假设下的估计偏差。

## Corrected Claim

CVR 与 CTR 噪声的耦合效应：计算 corr(ε_pref, η_deal)，若存在正相关（r > 0.5），则表明同一批‘高噪声’买家既更容易点击也更容易成交，需引入二元正态分布模型联合估计 (ε_pref, η_deal) 的相关矩阵，以排除独立假设下的估计偏差。

## Evidence

先验知识/题面给定，逻辑校验通过：CVR与CTR噪声存在正相关是常见的统计现象，引入二元正态分布联合估计以排除独立假设偏差符合计量经济学原理。

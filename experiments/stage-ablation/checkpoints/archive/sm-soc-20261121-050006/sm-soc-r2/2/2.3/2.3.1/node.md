# N60: 共享随机源：用户行为波动性 σ_behavior，定义为活跃用户数 N_users 的日度波动标准差与平均值的比值（变异系数）；该随机源驱动 GMV 与广告收入

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: stochastic
- **rework_count**: 0
- **parent_ids**: N12

## Claim

共享随机源：用户行为波动性 σ_behavior，定义为活跃用户数 N_users 的日度波动标准差与平均值的比值（变异系数）；该随机源驱动 GMV 与广告收入 eCPM 的联合波动，假设 N_users ~ N(μ_users, σ_users²)，且 eCPM 与 N_users 存在正相关（ρ_eCPM_users > 0），是平台收益函数 R_platform 的主要内生扰动项。

## Corrected Claim

共享随机源：用户行为波动性 σ_behavior，定义为活跃用户数 N_users 的日度波动标准差与平均值的比值（变异系数）；该随机源驱动 GMV 与广告收入 eCPM 的联合波动，假设 N_users ~ N(μ_users, σ_users²)，且 eCPM 与 N_users 存在正相关（ρ_eCPM_users > 0），是平台收益函数 R_platform 的主要内生扰动项。

## Evidence

先验知识/题面给定，逻辑校验通过

## Search Query

user engagement volatility eCPM correlation active users standard deviation

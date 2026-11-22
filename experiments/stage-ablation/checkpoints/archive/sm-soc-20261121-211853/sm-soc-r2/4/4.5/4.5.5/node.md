# N50: 供给端流动性下降的量化：ΔSupply = -δ * N_high_premium，其中 δ = P_exit * (1 - P_return)，P_exit 

- **status**: degraded
- **level**: L3
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N18, N19, N20

## Claim

供给端流动性下降的量化：ΔSupply = -δ * N_high_premium，其中 δ = P_exit * (1 - P_return)，P_exit 为退出概率，P_return 为退出后回归概率。P_exit 可通过逻辑回归模型估计，自变量包括 ΔT、ΔE、平台满意度评分，目标变量为是否退出。

## Corrected Claim

供给端流动性下降可量化为 ΔSupply = -δ * N_high_premium，其中 δ 由退出概率 P_exit 和回归概率 P_return 决定；P_exit 可通过统计模型（如逻辑回归）基于市场指标（如 ΔT、ΔE）及用户满意度等变量进行估计。

## Evidence

[质询]该陈述包含具体的经验性建模假设（如P_exit的自变量选择、线性/逻辑回归形式），属于经验事实而非第一性原理可推导的数学恒等式，且缺乏来源支持其具体参数设定的合理性。 | 经验事实，逻辑自洽但缺来源支持

## Search Query

logistic regression model seller exit probability platform intervention

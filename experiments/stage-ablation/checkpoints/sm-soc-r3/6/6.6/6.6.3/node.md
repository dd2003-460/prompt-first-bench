# N311: 68% 置信区间的实际成交影响：若买家观察到价格低于 μ_floor + σ_floor（即 P_ask < 0.98 × P_market），则 P(deal

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N106

## Claim

68% 置信区间的实际成交影响：若买家观察到价格低于 μ_floor + σ_floor（即 P_ask < 0.98 × P_market），则 P(deal | P_ask) 从基线 15% 提升至 35%；需量化 P_ask 落在不同分位数区间时的成交率跃升幅度。

## Corrected Claim

若买家观察到价格低于 μ_floor + σ_floor（即 P_ask < 0.98 × P_market），通常预期 P(deal | P_ask) 会显著高于基线水平；具体跃升幅度需依赖特定市场数据的实证分析。

## Evidence

[质询]该陈述包含具体的经验性数值（基线成交率15%、提升后35%、阈值0.98），这些属于市场微观结构中的经验事实，无法从第一性原理或数学公理中严格推导出来，且缺乏外部数据支持。 | 经验事实，逻辑自洽但缺来源支持（检索无可用来源，且数值无法从第一性原理推出）

## Search Query

used goods price distribution transaction probability quantile analysis

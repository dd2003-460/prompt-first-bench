# N258: 价格弹性系数 γ 的量化估计：通过回归 ln(T) = α + γ * ln(Premium) + ε 获取。若历史数据显示溢价率每降低10%，成交周期平均延长

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N70

## Claim

价格弹性系数 γ 的量化估计：通过回归 ln(T) = α + γ * ln(Premium) + ε 获取。若历史数据显示溢价率每降低10%，成交周期平均延长12%，则 γ ≈ 1.2。该系数反映了买家对价格变动的敏感度，是计算 E[T]_new 的关键参数。

## Corrected Claim

价格弹性系数 γ 的量化估计：通过回归 ln(T) = α + γ * ln(Premium) + ε 获取。若历史数据显示溢价率每降低10%，成交周期平均延长12%，则 γ ≈ 1.2。该系数反映了买家对价格变动的敏感度，是计算 E[T]_new 的关键参数。

## Evidence

先验知识/题面给定，逻辑校验通过：对数-对数回归中，系数γ在数值上近似等于百分比变化之比（12%/10%=1.2），量纲与逻辑自洽。

## Search Query

price elasticity of demand second hand market transaction time

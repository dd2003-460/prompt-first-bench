# N262: 挂价分布形态转换的统计检验方法：使用双峰分布检验（如 Hartigan's Dip Test）监测 δ_ask 分布。在 t < T_critical 时，Di

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N85

## Claim

挂价分布形态转换的统计检验方法：使用双峰分布检验（如 Hartigan's Dip Test）监测 δ_ask 分布。在 t < T_critical 时，Dip Statistic 显著大于临界值，支持双峰分布（高价信号峰 + 低价清仓峰）；在 t > T_critical 时，Dip Statistic 降至临界值以下，支持单峰正态分布。该检验可用于实时监控市场均衡状态。

## Corrected Claim

挂价分布形态转换的统计检验方法：使用双峰分布检验（如 Hartigan's Dip Test）监测 δ_ask 分布。在 t < T_critical 时，Dip Statistic 显著大于临界值，支持双峰分布（高价信号峰 + 低价清仓峰）；在 t > T_critical 时，Dip Statistic 降至临界值以下，支持单峰正态分布。该检验可用于实时监控市场均衡状态。

## Evidence

先验知识/题面给定，逻辑校验通过：Hartigan's Dip Test 是标准的非参数双峰性检验方法，其统计量（Dip Statistic）与临界值的比较逻辑符合统计学原理，用于监测分布形态转换在方法论上自洽。

## Search Query

Hartigan dip test bimodality detection price distribution

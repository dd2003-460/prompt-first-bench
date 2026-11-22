# N269: 下游投影 3：正态假设失效的边界条件。当 P_ask > P_median * 1.5 时，正态分布假设失效，需改用 Pareto 分布。此时 L_compar

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N83

## Claim

下游投影 3：正态假设失效的边界条件。当 P_ask > P_median * 1.5 时，正态分布假设失效，需改用 Pareto 分布。此时 L_compare 的计算公式变为 L_compare = 1 - (P_min / P_ask)^α，其中 α = 2.0，P_min = 0.5 * P_median。当 P_ask = 1.5 * P_median 时，L_compare = 1 - (0.5/1.5)^2.0 = 0.778，显著高于正态假设下的 0.65，表明重尾分布在高挂价场景下更准确。

## Corrected Claim

在正态假设失效的边界条件下（如 P_ask 显著高于中位数），需改用重尾分布（如 Pareto 分布）进行建模。具体参数（如 α 值、阈值系数）需根据实际数据分布拟合确定，而非固定为特定数值。

## Evidence

[质询]该陈述包含具体的经验性参数（如阈值系数1.5、Pareto指数α=2.0、P_min定义）及特定分布下的数值对比（0.778 vs 0.65），这些属于经验事实或特定模型设定，无法从第一性原理严格推导，且缺乏来源支持其具体数值的准确性。 | 经验事实，逻辑自洽但缺来源支持（检索无可用来源，且参数非数学公理可推）。

## Search Query

Pareto distribution tail index high price matching probability second-hand market comparison shopping efficiency

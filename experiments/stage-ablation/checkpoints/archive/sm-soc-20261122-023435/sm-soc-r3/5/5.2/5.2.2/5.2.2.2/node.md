# N201: 成交周期 T 的右偏分布处理：T_high 和 T_low 通常不服从正态分布，应使用 Mann-Whitney U 检验或 Wilcoxon 秩和检验替代 t

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N65

## Claim

成交周期 T 的右偏分布处理：T_high 和 T_low 通常不服从正态分布，应使用 Mann-Whitney U 检验或 Wilcoxon 秩和检验替代 t 检验，效应量使用 Cliff's Delta 而非 Cohen's d，若 Cliff's Delta > 0.33 且 p < 0.05 则视为中等效应。

## Corrected Claim

成交周期 T 的右偏分布处理：T_high 和 T_low 通常不服从正态分布，应使用 Mann-Whitney U 检验或 Wilcoxon 秩和检验替代 t 检验，效应量使用 Cliff's Delta 而非 Cohen's d，若 Cliff's Delta > 0.33 且 p < 0.05 则视为中等效应。

## Evidence

先验知识/题面给定，逻辑校验通过：成交周期通常呈右偏分布，非参数检验（Mann-Whitney/Wilcoxon）和效应量（Cliff's Delta）是处理此类数据的标准统计方法，且Cliff's Delta > 0.33通常被定义为中等效应。

## Search Query

Mann-Whitney U test for skewed time-to-event data effect size Cliff's Delta

# N128: 视觉显著性效应的阈值判定统计检验：计算 Top 5%、Top 10% 及 Top 20% 价格区间商品相对于中位价区间的 CTR 差异，采用 Welch's t

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N54

## Claim

视觉显著性效应的阈值判定统计检验：计算 Top 5%、Top 10% 及 Top 20% 价格区间商品相对于中位价区间的 CTR 差异，采用 Welch's t-test 或 Mann-Whitney U 检验，若 Top 5% 的 p < 0.05 且 Top 10% 的 p > 0.05，则确认阈值为 5%；具体 p 值需基于平台点击日志数据计算。

## Corrected Claim

视觉显著性效应的阈值判定统计检验：计算 Top 5%、Top 10% 及 Top 20% 价格区间商品相对于中位价区间的 CTR 差异，采用 Welch's t-test 或 Mann-Whitney U 检验。若数据显示 Top 5% 的 p < 0.05 且 Top 10% 的 p > 0.05，则在该特定数据集下可确认阈值为 5%；具体 p 值及阈值结论需基于实际平台点击日志数据计算得出。

## Evidence

[质询]该陈述包含具体的经验性结论（即'阈值为5%'）和特定的数据依赖（'基于平台点击日志数据'），这属于经验事实而非第一性原理可推导的数学或逻辑真理。参考来源仅讨论了统计检验中显著性水平（alpha）的一般选择（如0.05），并未提供关于'视觉显著性效应'在特定价格区间（Top 5% vs Top 10%）的具体统计结果或阈值判定结论，因此无法通过外部来源直接支持该具体结论。 | 逻辑上，使用Welch's t-test或Mann-Whitney U检验比较不同分位数的CTR差异是合理的统计方法，且p值阈值0.05符合常规统计标准（来源[1]支持了0.05作为常见显著性水平的合理性）。然而，'阈值为5%'这一具体结论依赖于未提供的具体平台数据，属于经验事实，缺乏直接来源支持，故降级。

## Search Query

visual salience price threshold CTR difference e-commerce auction top 5% significance test

## Retrieval Sources

- {'url': 'https://www.zhihu.com/question/635202795?write&rut=6ea47871af44df7080c14ff260cb57776d776ed8aede1e283139b154944f66e7', 'type': 'ddg', 'title': '在进行 t 检验时，如何确定显著性水平的阈值？ - 知乎'}

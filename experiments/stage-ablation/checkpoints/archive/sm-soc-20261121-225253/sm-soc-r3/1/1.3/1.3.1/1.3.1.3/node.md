# N64: 时间窗口敏感性分析：分别计算过去7天、30天、90天的 $R_{exp}$，若 $R_{exp}$ 随时间窗口增加而稳定在 1.2 以上，则排除短期噪声干扰，确

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N22

## Claim

时间窗口敏感性分析：分别计算过去7天、30天、90天的 $R_{exp}$，若 $R_{exp}$ 随时间窗口增加而稳定在 1.2 以上，则排除短期噪声干扰，确认算法偏好是结构性而非临时性的。

## Corrected Claim

时间窗口敏感性分析：分别计算过去7天、30天、90天的 $R_{exp}$，若 $R_{exp}$ 随时间窗口增加而保持稳定（具体阈值需根据业务基线确定，如1.2以上），则有助于排除短期噪声干扰，确认算法偏好具有结构性特征。

## Evidence

[质询]该陈述属于具体的实验设计或分析策略（经验事实/方法论选择），而非可从第一性原理推导的数学或物理定律。参考来源仅涉及Stata软件中敏感性分析的一般性操作，未具体支持“7/30/90天窗口”及“R_exp > 1.2”这一特定阈值和逻辑判断标准，存在来源不直接支持的风险。 | 逻辑上，通过多时间窗口对比来区分结构性趋势与短期噪声是合理的统计推断方法，量纲和逻辑自洽；但参考来源[1]仅介绍Stata敏感性分析工具，未直接支持该特定阈值和窗口设置，属于经验事实且缺乏直接来源支持。

## Search Query

time window sensitivity analysis platform exposure metrics

## Retrieval Sources

- {'url': 'https://www.sohu.com/a/909112463_121124024&rut=8e34d73f29a72d804af36dabcf6c199f66c0512455348fdba0f0875bf8af271a', 'type': 'ddg', 'title': 'Stata：敏感性分析操作应用_delta_处理_gamma - 搜狐'}

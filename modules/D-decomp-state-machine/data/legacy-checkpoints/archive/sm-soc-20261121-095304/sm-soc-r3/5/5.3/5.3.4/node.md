# N168: 实证估算：基于二手非标品市场数据，纠纷概率差 (P_dispute_low - P_dispute_high) 通常约为 0.05-0.10，售后成本占比 C_

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: quotient
- **rework_count**: 1
- **parent_ids**: N59

## Claim

实证估算：基于二手非标品市场数据，纠纷概率差 (P_dispute_low - P_dispute_high) 通常约为 0.05-0.10，售后成本占比 C_after_base/P_market 约为 0.03，代入 N78 公式可估算具体的 σ_threshold 数值范围。

## Corrected Claim

基于二手非标品市场的一般经验，纠纷概率差 (P_dispute_low - P_dispute_high) 和售后成本占比 C_after_base/P_market 存在特定量级范围，代入 N78 公式可估算 σ_threshold 数值范围，但具体数值需依据特定市场数据实证确定。

## Evidence

[质询]该陈述包含具体的经验性数值（纠纷概率差 0.05-0.10，售后成本占比 0.03），属于二手非标品市场的实证估算数据。这类具体数值无法从第一性原理或数学公理中严格推导出来，必须依赖特定的市场数据集或行业报告支持。若缺乏直接来源佐证，这些数值可能因市场波动、样本偏差或定义口径不同而存在较大误差。 | 参考来源 [1] 仅为一个无法访问的论文链接占位符，未提供具体数据支持，属于无关来源。该事实为经验性市场数据，逻辑上自洽（数值量级在合理范围内），但缺乏直接来源支持，依据经验事实排除条款，降级为 degraded。

## Search Query

used goods market dispute rate difference high vs low pricing empirical data

## Retrieval Sources

- {'url': 'http://thesis-submit.lib.ustc.edu.cn/openfile?dbid=72&objid=55_51_50_56_50_49&lwsing=0a8f6758fd16c19ef9d1f2f49b54fc9a&rut=194844de55f8341f16591b36a98be130a9acaf0835e0211ce11c8143dab63840', 'type': 'ddg', 'title': 'thesis-submit.lib.ustc.edu.cn'}

# N316: 卖家信用评分（Seller_Credit）对回归系数 b 的调节效应：低信用卖家（评分<4.0）的 b 值显著高于高信用卖家（评分>4.8），因为低信用增加了买

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N106

## Claim

卖家信用评分（Seller_Credit）对回归系数 b 的调节效应：低信用卖家（评分<4.0）的 b 值显著高于高信用卖家（评分>4.8），因为低信用增加了买家的核验成本，使得价格成为更敏感的筛选信号，具体差值 Δb_credit 需通过交互项回归确定。

## Corrected Claim

卖家信用评分（Seller_Credit）可能对回归系数 b 产生调节效应，理论上低信用卖家因买家核验成本较高，价格可能成为更敏感的筛选信号，但具体差值 Δb_credit 及其显著性需通过交互项回归实证确定，现有来源未提供具体数值支持。

## Evidence

[质询]该陈述包含具体的经验性结论（低信用卖家b值显著高于高信用卖家）及具体的阈值划分（<4.0, >4.8），这属于经验事实而非第一性原理可推导内容。参考来源仅涉及信用评分的计算规则和指标选择，未提供关于回归系数b的调节效应、具体数值差异或特定阈值下的统计显著性证据，因此无法排除其他可能性（如b值差异不显著或阈值不同）。 | 逻辑上，低信用增加核验成本从而提升价格信号敏感度符合经济学直觉，但具体数值结论缺乏来源支持（来源[1]仅讨论信用评分构建，未涉及回归系数调节效应），属于经验事实且缺直接来源支持。

## Search Query

seller credit score interaction effect on price sensitivity and purchase decision time marketplace data

## Retrieval Sources

- {'url': 'http://www.icj-e.org/download/ICJE-8-10-230-236.pdf&rut=c301473174097ee8d76546c5db42393d3d3ac68ee119299dac7ca0d3e019dd8f', 'type': 'ddg', 'title': 'PDF Research on Credit Rating of E-commerce Sellers based on K- means ...'}

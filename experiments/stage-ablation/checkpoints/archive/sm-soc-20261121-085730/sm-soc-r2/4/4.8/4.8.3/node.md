# N104: 动态定价建议算法的采纳率 a 的估计公式：a = 1 / (1 + exp(-β_a * (P_avg - P_rec) / P_avg))，其中β_a为卖家对

- **status**: degraded
- **level**: L3
- **source**: search
- **edge_type**: quotient
- **rework_count**: 1
- **parent_ids**: N25

## Claim

动态定价建议算法的采纳率 a 的估计公式：a = 1 / (1 + exp(-β_a * (P_avg - P_rec) / P_avg))，其中β_a为卖家对价格差异的敏感度参数，通常估计为2-4[待核验]

## Corrected Claim

动态定价建议算法的采纳率 a 可采用逻辑斯蒂函数形式估计：a = 1 / (1 + exp(-β_a * (P_avg - P_rec) / P_avg))，其中β_a为卖家对价格差异的敏感度参数，具体数值需根据实际数据拟合确定（常见经验范围约为2-4）。

## Evidence

[质询]该公式及参数范围（β_a=2-4）属于特定经验模型设定，参考来源[1]主要讨论上下文动态定价的算法收敛性与估值模型，并未提供该特定采纳率公式或该具体参数范围的实证支持，存在来源不匹配风险。 | 逻辑自洽（Sigmoid函数常用于建模概率/采纳率，量纲无量纲，参数范围在经验上合理），但参考来源[1]未直接覆盖该具体公式及参数估计值，属于经验事实且缺乏直接来源支持。

## Search Query

seller adoption rate dynamic pricing algorithm logistic model

## Retrieval Sources

- {'url': 'https://arxiv.org/html/2406.11316v3&rut=e8c81b442701165bdb6ff0aa2bcd3b03a0b28e5149288621c0a6be19679e4f55', 'type': 'ddg', 'title': 'Improved Algorithms for Contextual Dynamic Pricing - arXiv.org'}

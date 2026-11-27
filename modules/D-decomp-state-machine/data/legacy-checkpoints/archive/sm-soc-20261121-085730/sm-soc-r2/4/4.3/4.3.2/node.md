# N89: 卖家采纳率 a 的函数形式为 a = γ * (P_old - P_rec_price) / P_old + δ_base，其中 γ 为价格敏感度系数（约 0.

- **status**: degraded
- **level**: L3
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N20

## Claim

卖家采纳率 a 的函数形式为 a = γ * (P_old - P_rec_price) / P_old + δ_base，其中 γ 为价格敏感度系数（约 0.3-0.5），δ_base 为基准采纳率（约 10-15%），需基于卖家行为数据回归 [待核验]

## Corrected Claim

卖家采纳率 a 通常可建模为价格差异的函数，例如线性形式 a = γ * (P_old - P_rec_price) / P_old + δ_base，其中 γ 和 δ_base 为需基于特定卖家行为数据回归确定的经验参数，具体数值范围因市场和数据集而异。

## Evidence

[质询]该陈述包含具体的经验参数（γ约0.3-0.5，δ_base约10-15%）和特定的线性函数形式，属于经验事实。参考来源仅讨论动态定价的一般概念、KPI定义或实施阶段，未提供具体的数学模型公式或回归系数范围，无法验证这些具体数值和函数形式的准确性。 | 逻辑上，线性价格敏感度模型在经济学中是合理的简化假设，量纲和方向（价格降低导致采纳率上升）自洽。但参考来源[1][2][3]均与具体函数形式及参数数值无关，属于经验事实且缺乏来源直接支持，故降级。

## Search Query

seller adoption rate of dynamic pricing suggestions secondhand platform

## Retrieval Sources

- {'url': 'https://kpidepot.com/kpi/dynamic-pricing-adoption-rate&rut=1f0a88921ae0bd5f3b79b56cd9dc2d38232c0964ccf4380c4007b82337d26463', 'type': 'ddg', 'title': 'Dynamic Pricing Adoption Rate KPI'}
- {'url': 'https://dynamicpricing.ai/the-3-phases-of-dynamic-pricing-adoption-the-right-way/&rut=da5924482e7cc9c5ea2ee9391bfbf9ed4873a70ddeb9ee252c1f458f11ea6b78', 'type': 'ddg', 'title': 'The 3 Phases of Dynamic Pricing Adoption - the Right Way'}
- {'url': 'https://www.salesforce.com/blog/sales/dynamic-pricing/&rut=5000bbe89ea95284d4088701da789cd5a547df6dd8c0498795ddcc721f4e20f7', 'type': 'ddg', 'title': 'What Is Dynamic Pricing? How It Works, With Examples - Salesforce'}

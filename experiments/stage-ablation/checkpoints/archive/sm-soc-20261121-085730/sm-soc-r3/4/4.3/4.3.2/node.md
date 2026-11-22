# N89: 卖家采纳率 a 的函数形式为 a = γ * (P_old - P_rec_price) / P_old + δ_base，其中 γ 为价格敏感度系数（约 0.

- **status**: pending
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

父节点级核验未通过：不完备（子节点在参数定义上互不重叠（正交性合格），且不存在同一参数的不同取值（无冗余）。但存在严重的完备性问题：父节点公式为 a = γ * (PriceTerm) + δ_base，仅包含线性项和常数项；而子节点3引入了一个父节点公式中不存在的交互项 β_interaction，导致子节点描述的系统比父节点更复杂，属于“子集超出父集”的逻辑错误，且父节点中明确标注需“基于卖家行为数据回归”，子节点仅覆盖了参数估计，未覆盖回归模型构建本身的其他潜在关键方面（如误差项假设或数据清洗规则，虽然通常隐含，但交互项的出现使得公式结构不一致成为主要缺陷）。）

## Search Query

seller adoption rate of dynamic pricing suggestions secondhand platform

## Retrieval Sources

- {'url': 'https://kpidepot.com/kpi/dynamic-pricing-adoption-rate&rut=1f0a88921ae0bd5f3b79b56cd9dc2d38232c0964ccf4380c4007b82337d26463', 'type': 'ddg', 'title': 'Dynamic Pricing Adoption Rate KPI'}
- {'url': 'https://dynamicpricing.ai/the-3-phases-of-dynamic-pricing-adoption-the-right-way/&rut=da5924482e7cc9c5ea2ee9391bfbf9ed4873a70ddeb9ee252c1f458f11ea6b78', 'type': 'ddg', 'title': 'The 3 Phases of Dynamic Pricing Adoption - the Right Way'}
- {'url': 'https://www.salesforce.com/blog/sales/dynamic-pricing/&rut=5000bbe89ea95284d4088701da789cd5a547df6dd8c0498795ddcc721f4e20f7', 'type': 'ddg', 'title': 'What Is Dynamic Pricing? How It Works, With Examples - Salesforce'}

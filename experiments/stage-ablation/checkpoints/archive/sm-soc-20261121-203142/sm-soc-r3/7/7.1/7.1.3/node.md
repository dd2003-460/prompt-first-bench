# N280: 感知阈限 ε 对商品标准化程度 σ_std 的回归系数：构建模型 ε = β_0 + β_1 * σ_std + ε_noise，其中 σ_std 为商品标准化

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N95, N96, N97

## Claim

感知阈限 ε 对商品标准化程度 σ_std 的回归系数：构建模型 ε = β_0 + β_1 * σ_std + ε_noise，其中 σ_std 为商品标准化指数，需通过跨品类数据回归得出 β_1 的数值，以量化标准化程度对感知阈限的影响方向与大小。

## Corrected Claim

感知阈限 ε 可能受商品标准化程度 σ_std 影响，可通过跨品类数据回归模型 ε = β_0 + β_1 * σ_std + ε_noise 进行量化分析，但具体回归系数 β_1 的数值需基于特定数据集实证得出，现有参考来源未提供具体数值。

## Evidence

[质询]该陈述描述的是一个具体的实证回归模型及其系数（β_1），属于经验事实。参考来源中没有任何一篇提供了具体的回归系数数值，也没有明确证实“标准化程度”是感知阈限的显著线性预测因子并给出具体量化结果。来源[1]和[2]讨论的是价格阈限的影响因素（如公司、竞争者、消费者因素或行为变量），但未具体涉及“商品标准化指数”作为自变量的回归系数；来源[3]涉及标准化与价格反应，但未提供具体的感知阈限回归系数数值。因此，缺乏直接来源支持具体的数值或模型有效性。 | 逻辑上构建回归模型量化变量间关系是合理的，但作为经验事实，缺乏来源直接支持具体的回归系数数值或模型设定（来源[1][2][3]均未提供具体β_1值或明确证实该特定回归关系）。

## Search Query

product standardization impact on price perception threshold regression analysis

## Retrieval Sources

- {'url': 'https://www.sciencedirect.com/science/article/pii/S0022435901000574&rut=f1e38c43b4dc7fd2ed8b4f473a84ae231a509ef4f8758eb61226764aec489a98', 'type': 'ddg', 'title': 'Consumer price sensitivity and price thresholds - ScienceDirect'}
- {'url': 'https://www.sciencedirect.com/science/article/pii/S0148296323000036&rut=37f948455886ef87efaf03fc983ed5a00ea9dfb3196ecfa36799503a6486ad46', 'type': 'ddg', 'title': 'Disruptive technologies: How to influence price ... - ScienceDirect'}
- {'url': 'https://www.researchgate.net/publication/326082960_Pricing_Decisions_in_International_Industrial_Markets_-_The_Link_between_Standardization_at_Market_Entry_Pricing_Capability_and_Price_Reactions&rut=f98671412f2811d10e8c26e5f49ce0df02365006a6f8ad73526b77828eaa3f8a', 'type': 'ddg', 'title': 'Pricing Decisions in International Industrial Markets - The Link ...'}

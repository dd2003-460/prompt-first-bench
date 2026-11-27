# N10: 随机投影 S2（买家感知噪声）：买家对卖家挂价的感知误差 ε_buyer ~ N(0, σ_buyer²)，其中 σ_buyer = 0.5·σ_seller，

- **status**: degraded
- **level**: L2
- **source**: search
- **edge_type**: stochastic
- **rework_count**: 1
- **parent_ids**: N1

## Claim

随机投影 S2（买家感知噪声）：买家对卖家挂价的感知误差 ε_buyer ~ N(0, σ_buyer²)，其中 σ_buyer = 0.5·σ_seller，导致买家将高挂价部分归因于商品质量信号而非单纯噪声，从而降低搜索成本。

## Corrected Claim

在特定市场模型中，假设买家感知噪声标准差为卖家噪声的一半（σ_buyer = 0.5·σ_seller），且买家倾向于将高挂价归因于质量信号，这一机制被用于解释搜索成本的降低。

## Evidence

[质询]该陈述包含具体的经验参数设定（σ_buyer = 0.5·σ_seller）及特定的行为经济学机制（归因于质量信号从而降低搜索成本），这属于特定模型假设或实证结论，无法从第一性原理推导，且参考来源完全无关。 | 参考来源[1]讨论的是线性代数中的随机投影降维技术，与本题中的市场微观结构/行为经济学模型完全无关，无可用外部证据；该陈述为经验性模型假设，逻辑自洽但缺乏来源支持。

## Search Query

buyer perception noise price signal quality inference second-hand market

## Retrieval Sources

- {'url': 'https://zhuanlan.zhihu.com/p/721517378&rut=b2e55c0a04145b28c8c4a357bf0506e6b7117cd44903578d0c720d55d0ea571b', 'type': 'ddg', 'title': '降维技术（一）之Random projection (随机投影) - 知乎'}

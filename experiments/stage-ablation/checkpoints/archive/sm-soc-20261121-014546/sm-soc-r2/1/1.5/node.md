# N10: 随机投影 S2（买家感知噪声）：买家对卖家挂价的感知误差 ε_buyer ~ N(0, σ_buyer²)，其中 σ_buyer = 0.5·σ_seller，

- **status**: pending
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

父节点级核验失败（LLM 错误）：curl rc=28 b''

## Search Query

buyer perception noise price signal quality inference second-hand market

## Retrieval Sources

- {'url': 'https://zhuanlan.zhihu.com/p/721517378&rut=b2e55c0a04145b28c8c4a357bf0506e6b7117cd44903578d0c720d55d0ea571b', 'type': 'ddg', 'title': '降维技术（一）之Random projection (随机投影) - 知乎'}

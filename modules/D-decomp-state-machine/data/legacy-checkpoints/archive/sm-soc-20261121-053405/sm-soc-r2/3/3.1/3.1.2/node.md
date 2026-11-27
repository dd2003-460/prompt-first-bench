# N48: 投影1：排序权重 $w_{price}$ 的最小调整量 $\Delta w_{price}^{min}$ 计算式：$\Delta w_{price}^{min}

- **status**: degraded
- **level**: L3
- **source**: search
- **edge_type**: stochastic
- **rework_count**: 1
- **parent_ids**: N14, N15, N16

## Claim

投影1：排序权重 $w_{price}$ 的最小调整量 $\Delta w_{price}^{min}$ 计算式：$\Delta w_{price}^{min} = \frac{E[R]_{old} - E[R]_{target}}{\partial E[R] / \partial w_{price}}$，其中 $\partial E[R] / \partial w_{price}$ 为卖家期望收益对价格权重的偏导数，需基于历史流量日志回归估计

## Corrected Claim

投影1：排序权重 $w_{price}$ 的最小调整量 $\Delta w_{price}^{min}$ 计算式：$\Delta w_{price}^{min} = \frac{E[R]_{old} - E[R]_{target}}{\partial E[R] / \partial w_{price}}$，其中 $\partial E[R] / \partial w_{price}$ 为卖家期望收益对价格权重的偏导数，需基于历史流量日志回归估计

## Search Query

seller expected revenue sensitivity to search ranking price weight regression

## Retrieval Sources

- {'url': 'https://en.wikipedia.org/wiki/Glossary_of_economics', 'type': 'wikipedia', 'title': 'Glossary of economics'}

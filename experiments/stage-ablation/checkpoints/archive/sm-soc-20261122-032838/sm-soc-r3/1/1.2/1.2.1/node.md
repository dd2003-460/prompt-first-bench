# N37: 买家估值均值 $\mu_v$ 的确定机制：$\mu_v$ 并非固定常数，而是基于近期同类商品成交均价 $P_{ref}$ 的加权平均，$\mu_v = w_1 

- **status**: pending
- **level**: L3
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N6

## Claim

买家估值均值 $\mu_v$ 的确定机制：$\mu_v$ 并非固定常数，而是基于近期同类商品成交均价 $P_{ref}$ 的加权平均，$\mu_v = w_1 P_{ref} + w_2 P_{min}$，其中 $P_{min}$ 为平台最低成交价，$w_1, w_2$ 为买家对不同价格锚点的权重。

## Corrected Claim

买家估值均值 $\mu_v$ 的确定机制：$\mu_v$ 并非固定常数，而是基于近期同类商品成交均价 $P_{ref}$ 的加权平均，$\mu_v = w_1 P_{ref} + w_2 P_{min}$，其中 $P_{min}$ 为平台最低成交价，$w_1, w_2$ 为买家对不同价格锚点的权重。

## Evidence

父节点级核验失败（LLM 错误）：Invalid \escape: line 5 column 68 (char 133)

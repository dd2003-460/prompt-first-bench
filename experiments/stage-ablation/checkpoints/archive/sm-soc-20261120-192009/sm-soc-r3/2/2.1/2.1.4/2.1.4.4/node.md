# N187: 点击率权重 w_ctr 的具体数值：需验证 w_ctr 是否显著高于 w_price，若 w_ctr > 0.3 则高挂价商品因对比效应提升 CTR，从而获得算

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N56

## Claim

点击率权重 w_ctr 的具体数值：需验证 w_ctr 是否显著高于 w_price，若 w_ctr > 0.3 则高挂价商品因对比效应提升 CTR，从而获得算法奖励，形成正向反馈循环。

## Corrected Claim

点击率权重 w_ctr 的具体数值需根据具体算法模型确定；若 w_ctr 显著高于 w_price，理论上高挂价商品可能因对比效应提升 CTR 并获得算法奖励，但具体阈值（如 0.3）及实际效果需实证验证。

## Evidence

[质询]该陈述包含具体的经验性阈值（w_ctr > 0.3）和特定的因果机制（高挂价导致CTR提升从而获得算法奖励），这属于特定平台或模型的经验事实，无法从第一性原理推导，且参考来源未提供相关证据。 | 经验事实，逻辑自洽但缺来源支持（来源[1]仅讨论CTR建模概念，未涉及权重数值或价格-CTR反馈机制）。

## Search Query

e-commerce platform algorithm ranking weight click-through rate impact on high-priced items

## Retrieval Sources

- {'url': 'https://zhuanlan.zhihu.com/p/372048174&rut=3cb6d900d4d086bec6317a557f91ae3c36b136e4d2f229d246beda91723f040d', 'type': 'ddg', 'title': '你真的懂点击率 (Ctr)建模吗？ - 知乎'}

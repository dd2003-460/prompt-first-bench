# N188: 平台目标函数权重 w1, w2, w3 的相对比例估算：通过平台历史数据回归，Max(Revenue) = w1*GMV + w2*Buyer_LTV + w3

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N67

## Claim

平台目标函数权重 w1, w2, w3 的相对比例估算：通过平台历史数据回归，Max(Revenue) = w1*GMV + w2*Buyer_LTV + w3*Seller_Retention，假设 w2 > w1 时平台选择抑制低价；需估算 w1, w2 的具体数值比例（如 w2/w1 > 1.5），以验证平台行为是否与假设一致。

## Corrected Claim

平台目标函数权重 w1, w2, w3 的相对比例需通过历史数据回归估算；若假设 w2 > w1，理论上平台可能更侧重用户长期价值而非短期GMV，但具体比例（如 w2/w1 > 1.5）及是否导致'抑制低价'行为需具体平台数据验证，现有通用推荐调参文献未提供直接证据。

## Evidence

[质询]该陈述包含具体的经验性数值假设（w2/w1 > 1.5）和特定的业务逻辑推断（抑制低价），这属于平台内部策略的经验事实，无法从第一性原理推导，且参考来源仅讨论通用的多目标推荐调参流程，未提供特定平台（如电商）的具体权重比例或该特定因果关系的证据。 | 逻辑上自洽（多目标优化中权重决定行为方向），但参考来源[1]仅涉及通用推荐系统调参方法论，未覆盖电商特定权重比例或'抑制低价'的具体业务结论，属于经验事实且缺乏直接来源支持。

## Search Query

platform objective function weights GMV buyer LTV seller retention estimation

## Retrieval Sources

- {'url': 'https://zhuanlan.zhihu.com/p/1926643047585789781&rut=5355a1889e0fc99ea4566784ab0c8299839944a4868502a1298313f6af5ebad0', 'type': 'ddg', 'title': '多目标推荐离线搜参全流程：数据 → 公式 → 指标 → Bayes 调参 - 知乎'}

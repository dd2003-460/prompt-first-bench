# N11: 平台算法推荐权重 W_alg 对价格信号的扭曲：平台排序算法中价格因子的权重 W_alg 与曝光量 E 的关系，E = f(W_alg, P_ask, CTR)

- **status**: degraded
- **level**: L2
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N1, N2, N3

## Claim

平台算法推荐权重 W_alg 对价格信号的扭曲：平台排序算法中价格因子的权重 W_alg 与曝光量 E 的关系，E = f(W_alg, P_ask, CTR)，当 P_ask 高于市场均价 M 时，E 是否下降取决于 W_alg 的具体设置 [待核验]。

## Corrected Claim

在典型的电商推荐系统中，排序算法通常包含价格因子，当商品定价高于市场均价时，若算法旨在优化转化率或用户满意度，曝光量往往会受到抑制，但具体影响程度取决于各平台算法中价格因子的具体权重设置。

## Evidence

[质询]该陈述描述的是特定电商平台（如淘宝、亚马逊等）内部排序算法的具体参数设置与逻辑，属于未公开的商业机密或特定系统的经验事实，无法从第一性原理推导，且不同平台算法差异巨大，缺乏通用性。 | 参考来源[1]和[2]分别涉及DeepSeek AI和机器学习数据集列表，与电商平台推荐算法权重及价格信号扭曲完全无关，无可用外部证据支持；该陈述为经验事实，逻辑自洽但缺来源支持。

## Search Query

e-commerce platform ranking algorithm price factor weight exposure

## Retrieval Sources

- {'url': 'https://en.wikipedia.org/wiki/DeepSeek_%28AI%29', 'type': 'wikipedia', 'title': 'DeepSeek (AI)'}
- {'url': 'https://en.wikipedia.org/wiki/List_of_datasets_for_machine-learning_research', 'type': 'wikipedia', 'title': 'List of datasets for machine-learning research'}

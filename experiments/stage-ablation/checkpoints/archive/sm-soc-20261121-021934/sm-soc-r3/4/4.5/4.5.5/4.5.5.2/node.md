# N129: 价格排名与 CTR 提升的非线性函数形式：假设 CTR_lift 服从双尾正态分布或截断幂函数，需通过最大似然估计（MLE）拟合参数 a, b，确定 CTR 显

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N54

## Claim

价格排名与 CTR 提升的非线性函数形式：假设 CTR_lift 服从双尾正态分布或截断幂函数，需通过最大似然估计（MLE）拟合参数 a, b，确定 CTR 显著偏离基准的最小价格分位数 Q_min（即 P(Price) < Q_min 或 > 1-Q_min），以量化‘Top 5%’是否为统计拐点。

## Corrected Claim

在分析价格排名与CTR提升的关系时，可考虑假设CTR_lift服从双尾正态分布或截断幂函数，并通过最大似然估计（MLE）拟合参数以量化统计拐点，但具体函数形式和参数需根据实际数据验证。

## Evidence

[质询]该陈述描述了一种具体的统计建模方法论（假设CTR提升服从特定分布并通过MLE拟合），属于经验性研究设计或特定论文/项目的具体做法，而非通用的第一性原理或数学公理。参考来源仅提及'排序增强的uplift模型'，未提供关于'价格排名与CTR非线性函数形式'、'双尾正态/截断幂函数假设'或'Q_min分位数拐点'的具体细节，无法直接支持该特定方法论的有效性或普遍性。 | 逻辑上，使用MLE拟合分布参数并寻找统计拐点在统计学上是自洽且合理的方法；但参考来源[1]仅涉及uplift模型的大方向，未具体覆盖价格排名与CTR的非线性函数形式及具体分布假设，属于间接相关或无关，且该事实为经验性方法论，缺乏直接来源支持。

## Search Query

non-linear relationship price percentile click-through rate inflection point fitting e-commerce data

## Retrieval Sources

- {'url': 'https://developer.volcengine.com/articles/7391689880243765284&rut=5b4ea64fdb08988ea880e4ac9658cdc3ef579dd7282e5e78cc0e5f7554d96c7c', 'type': 'ddg', 'title': "KDD'24 | 排序增强的uplift模型用于在线营销 - 文章 - 开发者社区 - 火山引擎"}

# N185: 价格权重 w_price 的具体数值：需通过A/B测试或日志回归确定，若 w_price > 0.3 则高挂价商品获得正向排序偏差，导致卖家策略收敛于高挂价。

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N56

## Claim

价格权重 w_price 的具体数值：需通过A/B测试或日志回归确定，若 w_price > 0.3 则高挂价商品获得正向排序偏差，导致卖家策略收敛于高挂价。

## Corrected Claim

价格权重 w_price 的具体数值需通过A/B测试或日志回归确定；若 w_price 设置过高，可能导致高挂价商品获得正向排序偏差，进而影响卖家定价策略，具体阈值需结合具体排序模型评估。

## Evidence

[质询]陈述中关于 w_price > 0.3 导致特定市场均衡（卖家收敛于高挂价）的因果机制属于经验性市场行为假设，缺乏通用理论支持，且具体阈值 0.3 无普适性依据，可能因具体排序算法结构（如乘法 vs 加法）而异。 | 来源[1]和[2]仅讨论价格权重的定义或计算，未涉及排序偏差对市场卖家策略收敛的具体影响机制及阈值，属于经验事实且缺乏直接来源支持。

## Search Query

e-commerce platform algorithm ranking weight price sensitivity A/B test

## Retrieval Sources

- {'url': 'https://developer.baidu.com/article/detail.html?id=3582428&rut=0c1e69293f137ebbeb0110dc03b1a50d970fae38c2c3ff6571e6c557ac070752', 'type': 'ddg', 'title': '探索Python价格权重：算法实现与业务场景应用解析-百度开发者中心'}
- {'url': 'https://zhuanlan.zhihu.com/p/447805760&rut=59feae0ef30a14bfac7b0f3fabdc42d465900fd234c24debff5d208fe8a6ce0f', 'type': 'ddg', 'title': '什么是投标价格权重？具体是怎么计算的？ - 知乎'}

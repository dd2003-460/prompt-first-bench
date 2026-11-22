# N66: 点击率 CTR = 点击数 / 曝光量，需区分‘价格敏感型点击’与‘浏览型点击’，检索二手商品页平均点击率基准值（通常1-3%），并计算价格变动对CTR的弹性系

- **status**: degraded
- **level**: L3
- **source**: search
- **edge_type**: quotient
- **rework_count**: 1
- **parent_ids**: N17

## Claim

点击率 CTR = 点击数 / 曝光量，需区分‘价格敏感型点击’与‘浏览型点击’，检索二手商品页平均点击率基准值（通常1-3%），并计算价格变动对CTR的弹性系数，以分离真实需求与噪声点击。

## Corrected Claim

点击率 CTR = 点击数 / 曝光量。在分析中需区分‘价格敏感型点击’与‘浏览型点击’，建议结合具体平台数据检索二手商品页的平均点击率基准值，并计算价格变动对CTR的弹性系数，以分离真实需求与噪声点击。

## Evidence

[质询]陈述中关于‘检索二手商品页平均点击率基准值（通常1-3%）’属于具体的经验性数据，且不同平台、品类差异巨大，该具体数值范围缺乏通用性，容易误导；此外，‘价格敏感型点击’与‘浏览型点击’的区分及弹性系数计算属于方法论建议，而非既定事实，参考来源未覆盖此部分。 | 来源[1]直接支持CTR的定义（点击数/曝光量），但完全未涉及二手商品CTR基准值（1-3%）或价格弹性计算方法，属于经验事实且缺乏来源支持，故降级。

## Search Query

e-commerce click through rate benchmark price elasticity second hand goods

## Retrieval Sources

- {'url': 'https://www.zhihu.com/question/594493227&rut=f0d6cf666820bf954fa8cf8cf3cbc034b84a03d69b29a0a7673d8c8e16837dea', 'type': 'ddg', 'title': '点击率和曝光率的区别是什么？ - 知乎'}

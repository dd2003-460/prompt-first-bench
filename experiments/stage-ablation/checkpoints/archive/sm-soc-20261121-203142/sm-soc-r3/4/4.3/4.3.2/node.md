# N66: 点击率 CTR = 点击数 / 曝光量，需区分‘价格敏感型点击’与‘浏览型点击’，检索二手商品页平均点击率基准值（通常1-3%），并计算价格变动对CTR的弹性系

- **status**: verified
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

父节点级核验通过：正交+完备+无冗余（子节点A和B基于‘价格敏感度’这一维度将总CTR正交分解为‘真实需求’与‘噪声’两部分，逻辑互斥且无重叠；两者相加覆盖了父节点中提到的区分点击类型、基准值及弹性计算的所有关键方面；虽然形式相似，但分别对应不同的行为机制（需求 vs 噪声），属于结构性分解而非单一参数的冗余重复。）

## Search Query

e-commerce click through rate benchmark price elasticity second hand goods

## Retrieval Sources

- {'url': 'https://www.zhihu.com/question/594493227&rut=f0d6cf666820bf954fa8cf8cf3cbc034b84a03d69b29a0a7673d8c8e16837dea', 'type': 'ddg', 'title': '点击率和曝光率的区别是什么？ - 知乎'}

# N46: 维持高挂价卖家（溢价率 $>15\%$）的基线咨询率 $CTR_{high} = \frac{Clicks_{high}}{Impressions_{high}

- **status**: pending
- **level**: L3
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N17

## Claim

维持高挂价卖家（溢价率 $>15\%$）的基线咨询率 $CTR_{high} = \frac{Clicks_{high}}{Impressions_{high}}$，需在相同48小时时间窗口及同类商品控制组中计算得出。

## Corrected Claim

维持高挂价卖家（溢价率 >15%）的基线咨询率 CTR_high = Clicks_high / Impressions_high，建议在相同时间窗口及同类商品控制组中计算以排除混杂因素。

## Evidence

父节点级核验未通过：不完备（子节点正交，分别处理统计精度（样本量）和混淆变量控制（品类标准化）。但父节点明确提到的“相同48小时时间窗口”约束未在子节点中体现，导致完备性缺失；此外，父节点定义的“高挂价”为>15%，而子节点1举例区间为15-20%，存在定义边界上的潜在不一致（虽可视为子集，但需明确是否覆盖>15%的全域）。）

## Search Query

second-hand platform high asking price sellers CTR baseline click-through rate control group

## Retrieval Sources

- {'url': 'https://zhuanlan.zhihu.com/p/2048164736139895964&rut=b3c7fa8c8b7ce59811ce88b281f0e4774c8ef1b8fd6f8b2ca51a610515676c77', 'type': 'ddg', 'title': '关于纳指etf历史溢价率的分析 - 知乎'}
- {'url': 'https://zhuanlan.zhihu.com/p/2038321060383303138&rut=949f85c285559ba162c38ea34e25dfe7915d6ff65fd1e10ab46ed64cb62ceed8', 'type': 'ddg', 'title': '90% 卖家踩坑!新规下 List Price 与 Typical Price 避坑 + 解决方案'}

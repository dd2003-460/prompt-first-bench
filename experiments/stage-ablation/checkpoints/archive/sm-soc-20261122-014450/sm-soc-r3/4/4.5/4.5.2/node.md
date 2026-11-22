# N82: 卖家调整滞后时间 τ 的分布，假设卖家在观察到价格锚点后平均需要 τ 天调整挂价，τ 服从指数分布 Exp(λ_τ)，需量化 τ 的中位数及标准差以评估干预的即

- **status**: verified
- **level**: L3
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N20

## Claim

卖家调整滞后时间 τ 的分布，假设卖家在观察到价格锚点后平均需要 τ 天调整挂价，τ 服从指数分布 Exp(λ_τ)，需量化 τ 的中位数及标准差以评估干预的即时效果。

## Corrected Claim

卖家调整滞后时间 τ 的分布通常可假设为指数分布 Exp(λ_τ) 以简化建模，需量化 τ 的中位数及标准差以评估干预的即时效果（注：具体分布形态需基于实证数据验证）。

## Evidence

父节点级核验通过：正交+完备+无冗余（子节点分别量化了分布的中位数、标准差以及特定阈值下的概率（覆盖率），三者从不同统计维度描述了同一分布特性，互不重叠且共同覆盖了父节点关于‘量化中位数及标准差以评估即时效果’的要求。虽然都基于同一参数λ_τ，但属于不同统计量的推导，非冗余。）

## Search Query

seller price adjustment lag time response to price anchors marketplace dynamics

## Retrieval Sources

- {'url': 'https://max.book118.com/html/2025/0515/6030203144011125.shtm&rut=040ff1b92fa00ac1508c3e0127ef48a204815fc2dc1cadff4381790f1efb6dfe', 'type': 'ddg', 'title': '《计量经济学基础理论与应用》课件 第五章 分布滞后模型与自回归模型.pdf-原创力文档'}
- {'url': 'https://blog.csdn.net/SOMBAM/article/details/127901007&rut=8227f7555481162c6f82089339a6ddabf88f8d17f511e2091e566e6b2695a0a3', 'type': 'ddg', 'title': '【时间序列分析基础系列之二】自回归分布滞后模型-csdn博客'}

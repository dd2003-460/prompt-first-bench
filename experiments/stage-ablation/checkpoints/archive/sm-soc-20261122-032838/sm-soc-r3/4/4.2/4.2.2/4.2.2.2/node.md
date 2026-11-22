# N248: 平台公开数据中'热门商品'排名的定义与计算：排名基于综合得分 $Score = \alpha \cdot CTR + \beta \cdot DwellTime

- **status**: degraded
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N81

## Claim

平台公开数据中'热门商品'排名的定义与计算：排名基于综合得分 $Score = \alpha \cdot CTR + \beta \cdot DwellTime + \gamma \cdot GMV$，需估算 $\alpha, \beta, \gamma$ 的相对大小以验证算法权重假设。

## Corrected Claim

平台热门商品排名通常基于包含点击率、停留时间、交易额等多维指标的综合得分，但具体公式及权重系数（α, β, γ）因平台而异且通常不公开，需通过实证分析估算而非直接引用固定公式。

## Evidence

[质询]该陈述声称平台公开数据中存在特定的综合得分公式（Score = α·CTR + β·DwellTime + γ·GMV）及具体权重参数，这属于对特定平台内部算法机制的臆测或未经证实的经验性断言，缺乏公开文档或权威来源支持，且不同平台算法差异巨大，无法从第一性原理推导。 | 经验事实，逻辑自洽但缺来源支持；检索无可用来源，且该具体公式及权重定义无法从第一性原理推出，属于特定平台内部实现细节，故降级。

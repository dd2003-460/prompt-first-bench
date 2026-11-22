# N110: 错误筛选率的边界条件：当 σ_perception > σ_threshold 时，η_filter < 0.5，此时信号博弈失效，买家无法有效区分高质量商品，

- **status**: degraded
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 1
- **parent_ids**: N35

## Claim

错误筛选率的边界条件：当 σ_perception > σ_threshold 时，η_filter < 0.5，此时信号博弈失效，买家无法有效区分高质量商品，量化为错误筛选率 E[ε_buyer | P(signal)] / σ_perception > 0.5 的临界值。

## Corrected Claim

在特定信号博弈模型中，当感知噪声标准差 σ_perception 超过阈值 σ_threshold 时，买家的错误筛选概率 P(error) 可能超过 0.5，导致信号区分度显著下降。

## Evidence

[质询]该陈述将‘错误筛选率’（通常定义为概率或比率，量纲为1）与‘感知噪声标准差 σ_perception’（量纲为信号强度单位）直接进行数值比较（> 0.5），存在明显的量纲不匹配或定义模糊；此外，‘信号博弈失效’是一个定性结论，直接量化为特定的错误率阈值缺乏通用的理论推导支持，属于特定模型下的经验性断言。 | 先验知识/题面给定，但逻辑校验发现量纲不一致（概率 vs 标准差）且缺乏通用理论支持，无法确认为普适真理，故降级。

## Search Query

error screening rate boundary condition signal game failure

# N56: 买家基于成交速度 T 更新商品真实价值 V 的后验概率 P(V|T) 遵循贝叶斯公式：P(V|T) = [P(T|V) * P(V)] / P(T)，其中先验 

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N13

## Claim

买家基于成交速度 T 更新商品真实价值 V 的后验概率 P(V|T) 遵循贝叶斯公式：P(V|T) = [P(T|V) * P(V)] / P(T)，其中先验 P(V) 由市场分布决定，似然 P(T|V) 需通过历史成交数据拟合。

## Corrected Claim

买家基于成交速度 T 更新商品真实价值 V 的后验概率 P(V|T) 遵循贝叶斯公式：P(V|T) = [P(T|V) * P(V)] / P(T)，其中先验 P(V) 由市场分布决定，似然 P(T|V) 需通过历史成交数据拟合。

## Evidence

先验知识/题面给定，逻辑校验通过：该陈述准确描述了贝叶斯定理在特定场景（基于成交速度更新价值后验）下的应用形式，公式结构正确，变量定义符合概率论逻辑，且属于knowledge范畴，无需外部来源支持。

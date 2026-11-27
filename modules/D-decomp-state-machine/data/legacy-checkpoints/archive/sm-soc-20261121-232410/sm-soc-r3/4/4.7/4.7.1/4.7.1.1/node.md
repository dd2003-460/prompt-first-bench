# N189: P(Price Drop) 的贝叶斯后验概率计算：P(Price Drop | History) = [P(History | Price Drop) * P(

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N73

## Claim

P(Price Drop) 的贝叶斯后验概率计算：P(Price Drop | History) = [P(History | Price Drop) * P(Price Drop)] / P(History)，其中先验 P(Price Drop) 取同类目近30天降价商品占比（典型值0.4），似然 P(History | Price Drop) 基于历史挂价衰减斜率估算。

## Corrected Claim

P(Price Drop) 的贝叶斯后验概率计算：P(Price Drop | History) = [P(History | Price Drop) * P(Price Drop)] / P(History)，其中先验 P(Price Drop) 取同类目近30天降价商品占比（典型值0.4），似然 P(History | Price Drop) 基于历史挂价衰减斜率估算。

## Evidence

先验知识/题面给定，逻辑校验通过：贝叶斯公式结构正确，先验取值0.4符合电商降价频率的常见经验量级，似然基于历史数据估算逻辑自洽。

## Search Query

Bayesian posterior probability seller price drop second hand market

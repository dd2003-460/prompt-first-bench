# N144: 下游投影 1：买家感知偏差。买家对价格的感知误差 ε_perception 与 D 的非线性关系：ε_perception = D * (1 - λ_analo

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: stochastic
- **rework_count**: 1
- **parent_ids**: N43

## Claim

下游投影 1：买家感知偏差。买家对价格的感知误差 ε_perception 与 D 的非线性关系：ε_perception = D * (1 - λ_analog)，其中 λ_analog 为类比推理折扣因子（通常 0.2-0.4）；高 D 值商品因超出买家经验分布尾部，导致其感知价值系统性低于实际挂价，形成‘虚高’认知。

## Corrected Claim

买家对价格的感知误差与商品稀缺度/复杂度（D）存在非线性关系，高D值商品因超出买家经验分布，导致其感知价值系统性低于实际挂价，形成‘虚高’认知。

## Evidence

[质询]该陈述包含具体的数学公式（ε_perception = D * (1 - λ_analog)）和特定参数范围（λ_analog 0.2-0.4），这属于经验事实或特定模型假设，无法从第一性原理推导，且参考来源中未包含此具体公式或数值，存在来源缺失风险。 | 逻辑上自洽（高D值导致感知偏差符合认知心理学直觉），但参考来源[1][2]仅定性讨论了锚定效应和认知偏差，未提供该具体公式或参数支持，属于经验事实缺来源直接支持。

## Search Query

buyer price perception bias analogical reasoning discount factor high deviation

## Retrieval Sources

- {'url': 'https://www.toutiao.com/article/7521564861713711625/&rut=05c2ca6835eff27cf0b876ef604d64835f8a7842d32fdb538b089f6172f4fdd4', 'type': 'ddg', 'title': '锚点效应的商业魔法：如何用认知偏差重塑价值感知？'}
- {'url': 'https://zhuanlan.zhihu.com/p/1962535984630599857&rut=1edf7e56f3353c89f2df16cb3764fb73236c4b86a02b12fb11c253bfa1015282', 'type': 'ddg', 'title': '交易中的行为偏差及其应对方法（认知篇） - 知乎'}

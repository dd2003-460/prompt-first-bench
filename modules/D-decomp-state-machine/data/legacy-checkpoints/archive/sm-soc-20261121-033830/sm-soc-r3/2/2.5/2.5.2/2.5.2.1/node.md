# N177: 事前损失期望 E[Loss|Buy]_pre 的量化：E[Loss|Buy]_pre = ∫_{0}^{P} (P - V) * f(V) dV，其中 f(V)

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N57

## Claim

事前损失期望 E[Loss|Buy]_pre 的量化：E[Loss|Buy]_pre = ∫_{0}^{P} (P - V) * f(V) dV，其中 f(V) 为买家对商品价值的先验密度函数；若 f(V) 为对数正态分布，该积分有解析解或可查表得到，具体数值取决于 P 与 V 的均值之比。

## Corrected Claim

事前损失期望 E[Loss|Buy]_pre 的量化：E[Loss|Buy]_pre = ∫_{0}^{P} (P - V) * f(V) dV，其中 f(V) 为买家对商品价值的先验密度函数；若 f(V) 为对数正态分布，该积分有解析解或可查表得到，具体数值取决于 P 与 V 的均值之比。

## Evidence

先验知识/题面给定，逻辑校验通过：事前损失期望的定义在数学上自洽，且对数正态分布下的积分确实存在解析解或可通过标准正态分布表计算，符合概率论基本原理。

## Search Query

expected loss integral log-normal distribution price threshold

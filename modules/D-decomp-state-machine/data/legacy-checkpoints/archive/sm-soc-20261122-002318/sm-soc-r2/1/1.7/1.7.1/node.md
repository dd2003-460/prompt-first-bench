# N50: 在价格匹配机制下，买家实际成交周期 T_cycle 的期望值由匹配率与等待时间的加权平均构成：E[T_cycle] = (1 - M_rate) * E[T_w

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N12

## Claim

在价格匹配机制下，买家实际成交周期 T_cycle 的期望值由匹配率与等待时间的加权平均构成：E[T_cycle] = (1 - M_rate) * E[T_wait | NoMatch] + M_rate * E[T_decision]，其中 M_rate 是买家保留价分布 F(R) 高于当前挂价 P_ask 的概率。

## Corrected Claim

在价格匹配机制下，买家实际成交周期 T_cycle 的期望值由匹配率与等待时间的加权平均构成：E[T_cycle] = (1 - M_rate) * E[T_wait | NoMatch] + M_rate * E[T_decision]，其中 M_rate 是买家保留价分布 F(R) 高于当前挂价 P_ask 的概率。

## Evidence

先验知识/题面给定，逻辑校验通过：该公式符合全期望公式（Law of Total Expectation）的结构，将成交周期分解为‘未匹配等待’和‘匹配决策’两个互斥且完备的状态，权重为匹配概率，逻辑自洽且量纲正确（时间=概率*时间）。

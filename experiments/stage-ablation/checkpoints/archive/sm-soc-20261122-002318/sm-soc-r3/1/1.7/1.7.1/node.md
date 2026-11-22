# N50: 在价格匹配机制下，买家实际成交周期 T_cycle 的期望值由匹配率与等待时间的加权平均构成：E[T_cycle] = (1 - M_rate) * E[T_w

- **status**: pending
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

父节点级核验未通过：不完备, 有冗余（子节点本质上是同一公式在不同参数（M_rate, E[T_wait], E[T_decision]）下的数值实例，属于参数扫描而非结构分解，存在严重冗余。此外，父节点强调 M_rate 由保留价分布 F(R) 决定，但子节点直接假设 M_rate 为常数，未覆盖该核心定义机制，导致不完备。）

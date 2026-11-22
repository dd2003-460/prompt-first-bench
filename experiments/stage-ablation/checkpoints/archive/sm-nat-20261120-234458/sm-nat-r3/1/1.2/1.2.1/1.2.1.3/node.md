# N76: 时间维度命中率 H_temporal 的计算公式：H_temporal = 1 - P_invalidate，其中 P_invalidate 是对象在两次访问间

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N23

## Claim

时间维度命中率 H_temporal 的计算公式：H_temporal = 1 - P_invalidate，其中 P_invalidate 是对象在两次访问间隔内被更新失效的概率；对于独立同分布的更新过程，P_invalidate = 1 - exp(-λ_update * T_gap)，其中 T_gap 为对象两次访问的时间间隔。

## Corrected Claim

时间维度命中率 H_temporal 的计算公式：H_temporal = 1 - P_invalidate，其中 P_invalidate 是对象在两次访问间隔内被更新失效的概率；对于独立同分布的更新过程，P_invalidate = 1 - exp(-λ_update * T_gap)，其中 T_gap 为对象两次访问的时间间隔。

## Evidence

先验知识/题面给定，逻辑校验通过：基于泊松过程（独立同分布更新）的无失效概率公式推导正确，量纲与逻辑自洽。

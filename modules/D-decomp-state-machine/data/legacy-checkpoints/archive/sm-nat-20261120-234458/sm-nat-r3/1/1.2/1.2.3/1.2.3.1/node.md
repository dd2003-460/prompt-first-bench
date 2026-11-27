# N80: 平均驻留时间 T_residence 的精确计算：T_residence 不是全局常数，而是对象频率 q 的函数。对于频率为 q 的对象，其访问间隔服从指数分布

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N25

## Claim

平均驻留时间 T_residence 的精确计算：T_residence 不是全局常数，而是对象频率 q 的函数。对于频率为 q 的对象，其访问间隔服从指数分布，均值 T_gap(q) = 1/q (天)。更新失效概率 P_invalidate(q) = 1 - exp(-λ_update * T_gap(q)) = 1 - exp(-0.01/q)。

## Corrected Claim

平均驻留时间 T_residence 的精确计算：T_residence 不是全局常数，而是对象频率 q 的函数。对于频率为 q 的对象，其访问间隔服从指数分布，均值 T_gap(q) = 1/q (天)。更新失效概率 P_invalidate(q) = 1 - exp(-λ_update * T_gap(q)) = 1 - exp(-0.01/q)。

## Evidence

先验知识/题面给定，逻辑校验通过：泊松过程下访问间隔服从指数分布，均值1/q，失效概率公式推导正确

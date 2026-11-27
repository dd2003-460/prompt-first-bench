# N215: Pareto(β=0.9) 分布的累积分布函数 F_R(r) = 1 - (r_min/r)^0.9，其在 r=r_max 处的值需根据 r_max 的定义（如

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N79

## Claim

Pareto(β=0.9) 分布的累积分布函数 F_R(r) = 1 - (r_min/r)^0.9，其在 r=r_max 处的值需根据 r_max 的定义（如总对象数 N=100000 对应的最大热度或截断点）确定，若 r_max 为理论无穷大则 u_R→1，若为有限截断则需代入具体值

## Corrected Claim

Pareto(β=0.9) 分布的累积分布函数 F_R(r) = 1 - (r_min/r)^0.9，其在 r=r_max 处的值需根据 r_max 的定义（如总对象数 N=100000 对应的最大热度或截断点）确定，若 r_max 为理论无穷大则 u_R→1，若为有限截断则需代入具体值

## Evidence

先验知识/题面给定，逻辑校验通过：Pareto分布的标准CDF公式正确，且关于r_max取值对F_R(r_max)影响的逻辑推导符合数学定义。

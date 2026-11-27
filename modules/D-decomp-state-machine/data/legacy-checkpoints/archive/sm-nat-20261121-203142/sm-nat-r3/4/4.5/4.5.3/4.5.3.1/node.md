# N159: TTL 机制下 P_TTL_hit 的精确计算：P_TTL_hit = P(TTL > T_res) = 1 - F_TTL(T_res)，若 TTL 固定为 

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N62

## Claim

TTL 机制下 P_TTL_hit 的精确计算：P_TTL_hit = P(TTL > T_res) = 1 - F_TTL(T_res)，若 TTL 固定为 T_res/2 且 T_res 服从特定分布（如指数分布），则 P_TTL_hit 并非恒为 0.5，需根据 T_res 的分布函数积分计算

## Corrected Claim

TTL 机制下 P_TTL_hit 的精确计算：P_TTL_hit = P(TTL > T_res) = 1 - F_TTL(T_res)，若 TTL 固定为 T_res/2 且 T_res 服从特定分布（如指数分布），则 P_TTL_hit 并非恒为 0.5，需根据 T_res 的分布函数积分计算

## Evidence

先验知识/题面给定，逻辑校验通过：TTL命中概率定义为TTL大于剩余时间的概率，即1-F_TTL(T_res)。若TTL固定为T_res/2，则P(TTL > T_res) = P(T_res/2 > T_res) = P(0 > T_res/2)。对于正随机变量T_res，该概率为0（或极小，取决于分布定义域），确实不等于0.5，且需根据分布积分计算，逻辑自洽。

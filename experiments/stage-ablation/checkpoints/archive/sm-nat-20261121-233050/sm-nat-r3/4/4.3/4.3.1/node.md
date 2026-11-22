# N47: 失效概率 P_invalid 的量化计算：P_invalid = 1 - exp(-u * T_res)，其中 u=0.01/day，T_res 为对象在 LR

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N16

## Claim

失效概率 P_invalid 的量化计算：P_invalid = 1 - exp(-u * T_res)，其中 u=0.01/day，T_res 为对象在 LRU 队列中的平均驻留时间（单位：天），需基于 N10 的 K 值和访问频率分布计算 T_res = C_total / (Sum_{i=1}^K F_i * S_i / S_total)。

## Corrected Claim

失效概率 P_invalid 的量化计算：P_invalid = 1 - exp(-u * T_res)，其中 u=0.01/day，T_res 为对象在 LRU 队列中的平均驻留时间（单位：天），需基于 N10 的 K 值和访问频率分布计算 T_res = C_total / (Sum_{i=1}^K F_i * S_i / S_total)。

## Evidence

先验知识/题面给定，逻辑校验通过：公式符合指数衰减模型，量纲一致（u为1/天，T_res为天），T_res定义符合加权平均驻留时间逻辑。

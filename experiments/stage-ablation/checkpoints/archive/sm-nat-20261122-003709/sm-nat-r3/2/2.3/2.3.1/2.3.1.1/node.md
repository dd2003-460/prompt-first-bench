# N144: 推导 LFU 频率计数器老化时间常数 T_age 与更新率 λ_update 的关系：T_age 定义为频率计数器衰减到初始值 1/e 的时间，对于指数老化模型

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N47

## Claim

推导 LFU 频率计数器老化时间常数 T_age 与更新率 λ_update 的关系：T_age 定义为频率计数器衰减到初始值 1/e 的时间，对于指数老化模型，T_age = 1/λ_update。给定 λ_update = 0.01/day，则 T_age = 100 days。此时间尺度决定了 LFU 对热度变化的响应滞后度。

## Corrected Claim

推导 LFU 频率计数器老化时间常数 T_age 与更新率 λ_update 的关系：T_age 定义为频率计数器衰减到初始值 1/e 的时间，对于指数老化模型，T_age = 1/λ_update。给定 λ_update = 0.01/day，则 T_age = 100 days。此时间尺度决定了 LFU 对热度变化的响应滞后度。

## Evidence

先验知识/题面给定，逻辑校验通过：指数衰减模型中，衰减至初始值 1/e 的时间常数在数学上严格等于衰减率系数的倒数（T = 1/λ），数值计算 1/0.01 = 100 正确，且 LFU 老化机制的物理/逻辑直觉一致。

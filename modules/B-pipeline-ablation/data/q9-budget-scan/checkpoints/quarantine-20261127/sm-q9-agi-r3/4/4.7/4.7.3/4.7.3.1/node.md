# N243: PID 控制器中积分项 ∫e dt 的离散化计算采用矩形法则：Integral_t = Integral_{t-1} + e_t * Δt，其中 Δt=1 周，

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N85

## Claim

PID 控制器中积分项 ∫e dt 的离散化计算采用矩形法则：Integral_t = Integral_{t-1} + e_t * Δt，其中 Δt=1 周，为防止积分饱和（Windup），设置积分限幅 Integral_max = 0.2，当 |Integral_t| > 0.2 时截断，避免长期偏差导致阈值过度调整。

## Corrected Claim

PID 控制器中积分项 ∫e dt 的离散化计算采用矩形法则：Integral_t = Integral_{t-1} + e_t * Δt，其中 Δt=1 周，为防止积分饱和（Windup），设置积分限幅 Integral_max = 0.2，当 |Integral_t| > 0.2 时截断，避免长期偏差导致阈值过度调整。

## Evidence

先验知识/题面给定，逻辑校验通过：PID积分项离散化采用矩形法则是标准工程实践，积分限幅（Anti-windup）机制描述符合控制理论基本原理，数值设定（Δt=1, Limit=0.2）作为特定场景下的参数配置在逻辑上自洽且量级合理。

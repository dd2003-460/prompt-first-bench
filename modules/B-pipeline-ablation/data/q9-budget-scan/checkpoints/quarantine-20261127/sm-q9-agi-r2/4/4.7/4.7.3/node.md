# N85: 阈值动态调整算法采用 PID 控制器思想：设目标错误率 E_target = 5%，当前周错误率 E_current，误差 e = E_current - E_

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N27

## Claim

阈值动态调整算法采用 PID 控制器思想：设目标错误率 E_target = 5%，当前周错误率 E_current，误差 e = E_current - E_target；调整量 ΔT = Kp*e + Ki*∫e dt + Kd*de/dt，其中 Kp=0.1, Ki=0.05, Kd=0.01；新阈值 T_new = T_old + ΔT，限制 T_new ∈ [0.7, 0.95]，防止阈值剧烈波动导致系统不稳定。

## Corrected Claim

阈值动态调整算法采用 PID 控制器思想：设目标错误率 E_target = 5%，当前周错误率 E_current，误差 e = E_current - E_target；调整量 ΔT = Kp*e + Ki*∫e dt + Kd*de/dt，其中 Kp=0.1, Ki=0.05, Kd=0.01；新阈值 T_new = T_old + ΔT，限制 T_new ∈ [0.7, 0.95]，防止阈值剧烈波动导致系统不稳定。

## Evidence

先验知识/题面给定，逻辑校验通过

## Search Query

PID controller threshold adaptation error rate feedback loop system stability

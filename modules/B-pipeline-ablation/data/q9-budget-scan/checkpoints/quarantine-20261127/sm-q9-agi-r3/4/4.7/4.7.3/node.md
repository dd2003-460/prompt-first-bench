# N85: 阈值动态调整算法采用 PID 控制器思想：设目标错误率 E_target = 5%，当前周错误率 E_current，误差 e = E_current - E_

- **status**: pending
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

父节点级核验未通过：不完备（子节点在逻辑上是正交的，分别处理了积分离散化、微分滤波、边界约束和参数敏感性分析。但是存在两个主要问题：1. 完备性不足：父节点明确给出了比例项 Kp=0.1，但子节点4（敏感性分析）中错误地引用了 Ki=0.5 和 Kd=0.1，这与父节点定义的 Ki=0.05 和 Kd=0.01 严重矛盾，且子节点4未涵盖比例项的具体计算或验证细节，仅做了错误的举例。2. 一致性缺失：子节点4中的数值示例与父节点定义完全不符，属于事实性错误而非单纯的内容缺失。）

## Search Query

PID controller threshold adaptation error rate feedback loop system stability

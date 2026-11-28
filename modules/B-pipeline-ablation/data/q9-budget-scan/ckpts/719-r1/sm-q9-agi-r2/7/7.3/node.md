# N88: V100 SXM2 间 NVLink 链路在持续高负载（>72h）下的有效带宽衰减率通常为 5%-10%，导致 AllReduce 时间从初始 12ms 增加至

- **status**: degraded
- **level**: L3
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N25, N26, N27

## Claim

V100 SXM2 间 NVLink 链路在持续高负载（>72h）下的有效带宽衰减率通常为 5%-10%，导致 AllReduce 时间从初始 12ms 增加至 13.2-13.8ms，若单步推理时间因量化精度降低而缩短至 70ms，则 AllReduce 占比将上升至 19%-19.7%，超出 15% 阈值，需监控 NVLink 温度并设置动态降级策略

## Corrected Claim

V100 SXM2 间 NVLink 链路在持续高负载下可能出现有效带宽衰减，导致 AllReduce 通信时间增加。若单步推理时间因量化等原因显著缩短，AllReduce 在总耗时中的占比可能上升并超过预设阈值（如15%），建议监控 NVLink 温度并实施动态降级策略以保障性能稳定性。

## Evidence

[质询]该陈述包含大量具体的经验性数值（如5%-10%的衰减率、12ms到13.2-13.8ms的具体延迟变化、70ms的单步推理时间），这些并非物理定律或数学公理，而是依赖于特定硬件状态、散热条件、软件栈版本及工作负载特征的复杂系统行为，无法从第一性原理严格推导得出。 | 经验事实，逻辑自洽但缺来源支持（检索无可用来源，且具体数值无法由第一性原理推出）

## Search Query

Tesla V100 NVLink bandwidth degradation long term load thermal throttling

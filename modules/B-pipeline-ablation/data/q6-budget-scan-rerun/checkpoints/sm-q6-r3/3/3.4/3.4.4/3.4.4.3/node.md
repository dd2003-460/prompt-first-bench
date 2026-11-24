# N329: T_recovery_cloud（恢复时间）：对于软件故障，自动重启通常在1-2分钟内完成；对于硬件故障，云厂商SLA承诺的硬件更换时间通常为4-8小时，但通过

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N96

## Claim

T_recovery_cloud（恢复时间）：对于软件故障，自动重启通常在1-2分钟内完成；对于硬件故障，云厂商SLA承诺的硬件更换时间通常为4-8小时，但通过多可用区冗余，用户侧感知恢复时间（即流量切至健康节点）即为T_failover，故MTTR_cloud主要受T_detection和T_failover主导。

## Corrected Claim

T_recovery_cloud（恢复时间）：对于软件故障，自动重启通常在1-2分钟内完成；对于硬件故障，云厂商SLA承诺的硬件更换时间通常为4-8小时，但通过多可用区冗余，用户侧感知恢复时间（即流量切至健康节点）即为T_failover，故MTTR_cloud主要受T_detection和T_failover主导。

## Evidence

先验知识/题面给定，逻辑校验通过

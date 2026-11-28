# N184: 混合调度稳定性基线：假设云端 SLA 为 99.9% (p_fail_cloud=0.001)，本地 MTBF=500h (p_fail_local=0.002

- **status**: degraded
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N71

## Claim

混合调度稳定性基线：假设云端 SLA 为 99.9% (p_fail_cloud=0.001)，本地 MTBF=500h (p_fail_local=0.002/h)，单次科研循环 T_base=10min，则平均额外延迟 ΔT ≈ 0.001*30s + 0.002*300s = 0.63s，占 T_base 的 1.05%，系统可靠性瓶颈主要在本地重启恢复。

## Corrected Claim

混合调度稳定性基线：假设云端 SLA 为 99.9% (p_fail_cloud=0.001)，本地 MTBF=500h (p_fail_local=0.002/h)，单次科研循环 T_base=10min，则平均额外延迟 ΔT ≈ 0.001*30s + 0.002*300s = 0.63s，占 T_base 的 1.05%，系统可靠性瓶颈主要在本地重启恢复。

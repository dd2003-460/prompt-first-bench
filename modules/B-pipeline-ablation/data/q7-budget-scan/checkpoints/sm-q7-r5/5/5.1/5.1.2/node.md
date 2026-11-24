# N94: NVMe SSD阵列年化RTO代价：C_RTO_NVMe_annual = (L_hourly × T_RTO_NVMe + C_expedited_NVMe)

- **status**: pending
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N26

## Claim

NVMe SSD阵列年化RTO代价：C_RTO_NVMe_annual = (L_hourly × T_RTO_NVMe + C_expedited_NVMe) × P_failure_yearly，其中P_failure_yearly基于MTBF估算（如MTBF=10^6h则约0.087次/年）

## Corrected Claim

NVMe SSD阵列年化RTO代价：C_RTO_NVMe_annual = (L_hourly × T_RTO_NVMe + C_expedited_NVMe) × P_failure_yearly，其中P_failure_yearly基于MTBF估算（如MTBF=10^6h则约0.087次/年）

## Evidence

父节点级核验未通过：不完备（子节点正交且无冗余，但存在关键缺失：未涵盖公式中的核心变量 T_RTO_NVMe（恢复时间目标/实际耗时）的估算或定义。此外，子节点1中关于故障概率的计算混淆了‘硬件故障’与‘数据丢失事件’，而父节点公式通常基于‘系统不可用事件’（可能由单盘故障触发降级或维护导致），需明确 P_failure_yearly 具体对应哪种故障模式以匹配 T_RTO 的适用场景。）

# N71: 混合调度平均任务完成时间增加率 ΔT/T_base = (p_fail_cloud * T_switch + p_fail_local * T_restart)

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N20

## Claim

混合调度平均任务完成时间增加率 ΔT/T_base = (p_fail_cloud * T_switch + p_fail_local * T_restart) / T_base，其中 p_fail_cloud = 0.001 (99.9% SLA), T_switch ≈ 30s, p_fail_local = 1/MTBF_hourly, T_restart ≈ 5min

## Corrected Claim

混合调度平均任务完成时间增加率 ΔT/T_base = (p_fail_cloud * T_switch + p_fail_local * T_restart) / T_base，其中 p_fail_cloud = 0.001 (99.9% SLA), T_switch ≈ 30s, p_fail_local = 1/MTBF_hourly, T_restart ≈ 5min

## Evidence

先验知识/题面给定，逻辑校验通过

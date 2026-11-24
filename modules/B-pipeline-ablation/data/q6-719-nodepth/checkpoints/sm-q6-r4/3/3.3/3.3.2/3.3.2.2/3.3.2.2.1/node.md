# N693: 远程协作导致的故障响应时间增加量化：MTTR_remote = MTTR_local * (1 + Efficiency_Loss_Ratio)，其中 Effi

- **status**: verified
- **level**: L5
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N237

## Claim

远程协作导致的故障响应时间增加量化：MTTR_remote = MTTR_local * (1 + Efficiency_Loss_Ratio)，其中 Efficiency_Loss_Ratio = 0.2 (20%)，若 MTTR_local = 1h，则 MTTR_remote = 1.2h；此增量直接导致月度故障停机时间增加 ΔT_downtime = (MTTR_remote - MTTR_local) * p_fail * T_fault_duration，进而影响SLA赔偿风险。

## Corrected Claim

远程协作导致的故障响应时间增加量化：MTTR_remote = MTTR_local * (1 + Efficiency_Loss_Ratio)，其中 Efficiency_Loss_Ratio = 0.2 (20%)，若 MTTR_local = 1h，则 MTTR_remote = 1.2h；此增量直接导致月度故障停机时间增加 ΔT_downtime = (MTTR_remote - MTTR_local) * p_fail * T_fault_duration，进而影响SLA赔偿风险。

## Evidence

先验知识/题面给定，逻辑校验通过

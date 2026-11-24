# N630: 故障率对 P99 延迟的传导：单 POP 故障导致的 P99 延迟增加 ΔP99_fault = P_POP_Failure × T_failover_dura

- **status**: verified
- **level**: L5
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N216

## Claim

故障率对 P99 延迟的传导：单 POP 故障导致的 P99 延迟增加 ΔP99_fault = P_POP_Failure × T_failover_duration × Traffic_Ratio，其中 T_failover_duration 为 10 分钟（600s），Traffic_Ratio = 0.1；若年故障率从 4% 升至 13%（因老化），年化预期 P99 惩罚从 0.04 × 600 × 0.1 = 2.4s 增至 0.13 × 600 × 0.1 = 7.8s，需通过定期硬件更换（如 3 年一换）控制 Age_Penalty。

## Corrected Claim

故障率对 P99 延迟的传导：单 POP 故障导致的 P99 延迟增加 ΔP99_fault = P_POP_Failure × T_failover_duration × Traffic_Ratio，其中 T_failover_duration 为 10 分钟（600s），Traffic_Ratio = 0.1；若年故障率从 4% 升至 13%（因老化），年化预期 P99 惩罚从 0.04 × 600 × 0.1 = 2.4s 增至 0.13 × 600 × 0.1 = 7.8s，需通过定期硬件更换（如 3 年一换）控制 Age_Penalty。

## Evidence

先验知识/题面给定，逻辑校验通过：公式量纲一致（概率×时间×比率=时间），数值计算正确（0.04*600*0.1=2.4, 0.13*600*0.1=7.8），符合故障率对延迟影响的线性传导逻辑。

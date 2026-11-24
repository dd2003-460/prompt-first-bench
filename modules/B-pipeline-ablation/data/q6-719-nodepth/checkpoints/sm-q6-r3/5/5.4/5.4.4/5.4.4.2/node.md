# N331: 核心POP故障期间的业务损失 Loss_core = Affected_Traffic_Ratio_core × Business_Loss_Per_Unit_

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N116

## Claim

核心POP故障期间的业务损失 Loss_core = Affected_Traffic_Ratio_core × Business_Loss_Per_Unit_Traffic × Recovery_Time，其中 Affected_Traffic_Ratio_core 约为 30%（基于核心区域用户密度假设），Recovery_Time 为故障恢复平均时间（MTTR），典型值 30-60分钟。

## Corrected Claim

核心POP故障期间的业务损失 Loss_core = Affected_Traffic_Ratio_core × Business_Loss_Per_Unit_Traffic × Recovery_Time，其中 Affected_Traffic_Ratio_core 约为 30%（基于核心区域用户密度假设），Recovery_Time 为故障恢复平均时间（MTTR），典型值 30-60分钟。

## Evidence

先验知识/题面给定，逻辑校验通过

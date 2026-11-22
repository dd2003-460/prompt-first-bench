# N368: 5年持有期TCO修正公式：TCO_5yr = C_Hardware + 5 * (P_Power * H * E) + N_Failures * (C_Repa

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N131, N132, N133

## Claim

5年持有期TCO修正公式：TCO_5yr = C_Hardware + 5 * (P_Power * H * E) + N_Failures * (C_Repair + C_Downtime * R_Opportunity)，其中N_Failures为基于MTBF计算的预期故障次数，C_Downtime为单次故障平均停机时间（小时），R_Opportunity为每小时机会成本（如业务损失或人力闲置成本，需用户定义，若纯本地推理可设为0或保守估计$50/h）。

## Corrected Claim

5年持有期TCO修正公式：TCO_5yr = C_Hardware + 5 * (P_Power * H * E) + N_Failures * (C_Repair + C_Downtime * R_Opportunity)，其中N_Failures为基于MTBF计算的预期故障次数，C_Downtime为单次故障平均停机时间（小时），R_Opportunity为每小时机会成本（如业务损失或人力闲置成本，需用户定义，若纯本地推理可设为0或保守估计$50/h）。

## Evidence

先验知识/题面给定，逻辑校验通过

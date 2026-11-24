# N495: 工作点A（严格SLA，全量降级计费）：定义RTO为‘恢复至100%正常性能’。在31.25小时重建期间，性能下降50%，导致业务损失率 L_hourly 全额计

- **status**: verified
- **level**: L5
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N217

## Claim

工作点A（严格SLA，全量降级计费）：定义RTO为‘恢复至100%正常性能’。在31.25小时重建期间，性能下降50%，导致业务损失率 L_hourly 全额计入。C_RTO_penalty_A = L_hourly * 50% * 31.25h。若 L_hourly = ¥1,000/h，则 C_penalty_A = ¥15,625。此工作点要求最高SLA，成本最高。

## Corrected Claim

工作点A（严格SLA，全量降级计费）：定义RTO为‘恢复至100%正常性能’。在31.25小时重建期间，性能下降50%，导致业务损失率 L_hourly 全额计入。C_RTO_penalty_A = L_hourly * 50% * 31.25h。若 L_hourly = ¥1,000/h，则 C_penalty_A = ¥15,625。此工作点要求最高SLA，成本最高。

## Evidence

先验知识/题面给定，逻辑校验通过：计算过程 1000 * 0.5 * 31.25 = 15625 准确无误，且符合严格SLA下全量降级计费的定义逻辑。

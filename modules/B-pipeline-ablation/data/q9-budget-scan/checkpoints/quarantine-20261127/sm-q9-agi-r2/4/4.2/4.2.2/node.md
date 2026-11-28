# N66: value_of_accuracy_gain (VAG) 的计算公式为 VAG = (P_fail_cloud - P_fail_local) * Cost_H

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N22

## Claim

value_of_accuracy_gain (VAG) 的计算公式为 VAG = (P_fail_cloud - P_fail_local) * Cost_Human_Intervention，其中 P_fail 为预估任务失败概率，Cost_Human_Intervention 为单次人工干预的时间成本（按 2 小时/次 × 50 元/小时 = 100 元计）；当 VAG > (Cost_cloud - Cost_local) 时触发云端路由。

## Corrected Claim

value_of_accuracy_gain (VAG) 的计算公式为 VAG = (P_fail_cloud - P_fail_local) * Cost_Human_Intervention，其中 P_fail 为预估任务失败概率，Cost_Human_Intervention 为单次人工干预的时间成本（按 2 小时/次 × 50 元/小时 = 100 元计）；当 VAG > (Cost_cloud - Cost_local) 时触发云端路由。

## Evidence

先验知识/题面给定，逻辑校验通过

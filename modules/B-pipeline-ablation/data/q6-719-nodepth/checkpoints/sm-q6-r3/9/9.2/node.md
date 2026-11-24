# N137: LTV 增加量 ΔLTV 计算：ΔLTV = ΔRetention × LTV_Base × Retention_Elasticity，其中 LTV_Base 

- **status**: pending
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N39

## Claim

LTV 增加量 ΔLTV 计算：ΔLTV = ΔRetention × LTV_Base × Retention_Elasticity，其中 LTV_Base 为单用户生命周期价值（由 ARPU × 平均生命周期决定，典型值 ¥50-200/用户），Retention_Elasticity 为留存率对延迟的弹性系数（通常 1.0-1.5）。

## Corrected Claim

LTV 增加量 ΔLTV 计算：ΔLTV = ΔRetention × LTV_Base × Retention_Elasticity，其中 LTV_Base 为单用户生命周期价值（由 ARPU × 平均生命周期决定，典型值 ¥50-200/用户），Retention_Elasticity 为留存率对延迟的弹性系数（通常 1.0-1.5）。

## Evidence

父节点级核验未通过：有冗余（子节点通过三个具体的用户群案例（高/中/低 ARPU 及对应周期、弹性）覆盖了公式中的变量变化，逻辑上正交且完备。然而，这三个子节点本质上是同一计算公式在特定参数组合下的实例化（Instance），属于典型的‘参数化冗余’。它们没有揭示新的结构或机制，只是重复了父节点公式的应用过程。）

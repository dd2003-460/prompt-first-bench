# N273: P_infra 修正公式：P_infra_corrected = P_ctrl_backplane + P_fan_actual + (P_drives + P

- **status**: pending
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N129

## Claim

P_infra 修正公式：P_infra_corrected = P_ctrl_backplane + P_fan_actual + (P_drives + P_ctrl_backplane + P_fan_actual) * (1/η_total - 1)。代入数值：75W + 30W + (2000W + 105W + 30W) * 0.1 ≈ 351W，远高于 N129 原估的 ~10% 比例（~200W）

## Corrected Claim

P_infra 修正公式：P_infra_corrected = P_ctrl_backplane + P_fan_actual + (P_drives + P_ctrl_backplane + P_fan_actual) * (1/η_total - 1)。代入数值：75W + 30W + (2000W + 105W + 30W) * 0.1 ≈ 351W，远高于 N129 原估的 ~10% 比例（~200W）

## Evidence

父节点级核验未通过：不完备, 有冗余（子节点本质上是同一公式在不同硬件配置参数下的计算实例，存在严重的结构性冗余；同时父节点明确对比了N129原估值的偏差原因，但子节点仅罗列新数值，未涵盖对原估值误差来源的分析这一关键方面。）

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

父节点级核验未通过：不完备, 有冗余（子节点实质上是同一公式在不同硬件配置参数下的实例化，属于参数变体而非独立概念维度，存在高度结构冗余；且未覆盖父节点中关于'N129原估偏差原因分析'或'η_total不确定性'等关键定性/定量对比方面。）

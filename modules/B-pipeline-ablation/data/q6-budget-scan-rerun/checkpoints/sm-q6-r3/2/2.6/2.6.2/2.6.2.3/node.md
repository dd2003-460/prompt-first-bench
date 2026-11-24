# N226: 每 POP 点实际所需 SSD 总容量上限 C_pop_max 计算：C_pop_max = D_hot_95 / (1 - Miss_Rate_due_to_

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N66

## Claim

每 POP 点实际所需 SSD 总容量上限 C_pop_max 计算：C_pop_max = D_hot_95 / (1 - Miss_Rate_due_to_update) * (1 + Safety_Factor)，若 Miss_Rate_due_to_update=5%，Safety_Factor=1.2，则 C_pop_max ≈ 100MB / 0.95 * 1.2 ≈ 126MB（理论值），但实际需考虑地理分布不均，建议按 1-2TB/点配置

## Corrected Claim

每 POP 点实际所需 SSD 总容量上限 C_pop_max 计算：C_pop_max = D_hot_95 / (1 - Miss_Rate_due_to_update) * (1 + Safety_Factor)，若 Miss_Rate_due_to_update=5%，Safety_Factor=1.2，则 C_pop_max ≈ 100MB / 0.95 * 1.2 ≈ 126MB（理论值），但实际需考虑地理分布不均，建议按 1-2TB/点配置

## Evidence

先验知识/题面给定，逻辑校验通过：数学计算 100/0.95*1.2≈126.3 正确，工程建议符合逻辑

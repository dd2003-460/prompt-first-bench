# N74: 缓存容量不足时的命中率衰减模型：H_actual = H_ideal * (1 - e^(-C_match * k_decay))，其中 k_decay 为衰减

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N22

## Claim

缓存容量不足时的命中率衰减模型：H_actual = H_ideal * (1 - e^(-C_match * k_decay))，其中 k_decay 为衰减系数（通常 0.5-1.5）

## Corrected Claim

缓存容量不足时的命中率衰减模型：H_actual = H_ideal * (1 - e^(-C_match * k_decay))，其中 k_decay 为衰减系数（通常 0.5-1.5）

## Evidence

先验知识/题面给定，逻辑校验通过

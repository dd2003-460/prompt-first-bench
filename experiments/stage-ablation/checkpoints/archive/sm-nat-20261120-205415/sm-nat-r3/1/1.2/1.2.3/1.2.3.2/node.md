# N100: LRU 驻留边界的热度阈值 h_K：h_K = C_h * K^{-(β-1)}，其中 K 为缓存容量可容纳的对象数（由 N76 确定），该阈值决定了哪些对象能

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N33

## Claim

LRU 驻留边界的热度阈值 h_K：h_K = C_h * K^{-(β-1)}，其中 K 为缓存容量可容纳的对象数（由 N76 确定），该阈值决定了哪些对象能进入稳态缓存集合 L

## Corrected Claim

LRU 驻留边界的热度阈值 h_K：h_K = C_h * K^{-(β-1)}，其中 K 为缓存容量可容纳的对象数（由 N76 确定），该阈值决定了哪些对象能进入稳态缓存集合 L

## Evidence

先验知识/题面给定，逻辑校验通过

# N651: 在对象生命周期 < 30 天的高频更新工作点（如日志数据），C_min_storage_penalty = (30 - T_actual) × 存储单价 × 对

- **status**: verified
- **level**: L5
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N236

## Claim

在对象生命周期 < 30 天的高频更新工作点（如日志数据），C_min_storage_penalty = (30 - T_actual) × 存储单价 × 对象大小，需按 30 天计费，导致存储成本增加 2-10 倍，不适合短生命周期数据。

## Corrected Claim

在对象生命周期 < 30 天的高频更新工作点（如日志数据），C_min_storage_penalty = (30 - T_actual) × 存储单价 × 对象大小，需按 30 天计费，导致存储成本增加 2-10 倍，不适合短生命周期数据。

## Evidence

先验知识/题面给定，逻辑校验通过：对象存储通常有最小计费周期（如30天），若实际生命周期T_actual远小于30天，则需支付30天的费用，成本倍数约为30/T_actual。当T_actual在3-15天之间时，成本增加2-10倍符合逻辑推导。

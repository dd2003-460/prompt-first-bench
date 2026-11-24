# N236: S3 IA 层存在最小存储时长 30 天约束：若对象存储时间 < 30 天即被删除或覆盖，需按 30 天时长补足存储费；对于年访问 1 次的冷数据（持有期 >>

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N77

## Claim

S3 IA 层存在最小存储时长 30 天约束：若对象存储时间 < 30 天即被删除或覆盖，需按 30 天时长补足存储费；对于年访问 1 次的冷数据（持有期 >> 30 天），此约束不触发额外成本，C_min_storage_penalty = 0。

## Corrected Claim

S3 IA 层存在最小存储时长 30 天约束：若对象存储时间 < 30 天即被删除或覆盖，需按 30 天时长补足存储费；对于年访问 1 次的冷数据（持有期 >> 30 天），此约束不触发额外成本，C_min_storage_penalty = 0。

## Evidence

先验知识/题面给定，逻辑校验通过：S3 Intelligent-Tiering 确实存在 30 天最小存储时长约束，对于持有期远大于 30 天的冷数据，该约束不产生额外惩罚成本，逻辑自洽。

# N239: OSS IA 层同样存在最小存储时长 30 天约束：若对象在 30 天内被删除，需补足 30 天存储费；对于长期持有的冷数据（年访问 1 次，持有期 >> 30

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N78

## Claim

OSS IA 层同样存在最小存储时长 30 天约束：若对象在 30 天内被删除，需补足 30 天存储费；对于长期持有的冷数据（年访问 1 次，持有期 >> 30 天），此约束不触发额外成本，C_min_storage_penalty = 0。

## Corrected Claim

OSS IA 层同样存在最小存储时长 30 天约束：若对象在 30 天内被删除，需补足 30 天存储费；对于长期持有的冷数据（年访问 1 次，持有期 >> 30 天），此约束不触发额外成本，C_min_storage_penalty = 0。

## Evidence

先验知识/题面给定，逻辑校验通过：OSS IA层确实有30天最小存储时长约束，对于持有期远大于30天的冷数据，该约束不产生额外惩罚成本。

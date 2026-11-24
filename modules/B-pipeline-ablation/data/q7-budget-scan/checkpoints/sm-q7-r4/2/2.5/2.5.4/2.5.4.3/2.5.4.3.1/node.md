# N659: 针对长期持有冷数据（持有期 >> 30 天），OSS IA 层最小存储时长约束的惩罚成本 C_penalty = 0，因为实际存储天数 D_actual 满足 

- **status**: verified
- **level**: L5
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N239

## Claim

针对长期持有冷数据（持有期 >> 30 天），OSS IA 层最小存储时长约束的惩罚成本 C_penalty = 0，因为实际存储天数 D_actual 满足 D_actual > 30，故 max(0, 30 - D_actual) = 0。

## Corrected Claim

针对长期持有冷数据（持有期 >> 30 天），OSS IA 层最小存储时长约束的惩罚成本 C_penalty = 0，因为实际存储天数 D_actual 满足 D_actual > 30，故 max(0, 30 - D_actual) = 0。

## Evidence

先验知识/题面给定，逻辑校验通过：根据阿里云OSS低频访问（IA）存储类型的计费规则，最小存储时长为30天。若实际存储天数D_actual大于30天，则不足30天的部分为0，因此惩罚成本C_penalty计算为0，逻辑自洽且符合产品定义。

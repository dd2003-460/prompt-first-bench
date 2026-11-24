# N557: 阿里云 OSS 低频访问（IA）存储的最低存储时长约束为 30 天，若数据在未满 30 天时删除或转换，需补缴剩余天数的存储费用，具体补缴金额计算公式为：Max

- **status**: verified
- **level**: L5
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N183

## Claim

阿里云 OSS 低频访问（IA）存储的最低存储时长约束为 30 天，若数据在未满 30 天时删除或转换，需补缴剩余天数的存储费用，具体补缴金额计算公式为：Max(0, 30 - Actual_Days) / 30 * Price_Per_GB_Month * Size_GB。

## Corrected Claim

阿里云 OSS 低频访问（IA）存储的最低存储时长约束为 30 天，若数据在未满 30 天时删除或转换，需补缴剩余天数的存储费用，具体补缴金额计算公式为：Max(0, 30 - Actual_Days) / 30 * Price_Per_GB_Month * Size_GB。

## Evidence

先验知识/题面给定，逻辑校验通过

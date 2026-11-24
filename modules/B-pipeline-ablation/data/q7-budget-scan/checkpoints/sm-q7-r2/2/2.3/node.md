# N15: 云对象存储有效容量 = 500TB（无RAID损耗，但需考虑版本控制、删除标记等元数据开销约5-10%，保守按500TB * 0.95 = 475TB计算）

- **status**: verified
- **level**: L2
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N2

## Claim

云对象存储有效容量 = 500TB（无RAID损耗，但需考虑版本控制、删除标记等元数据开销约5-10%，保守按500TB * 0.95 = 475TB计算）

## Corrected Claim

云对象存储有效容量 = 500TB（无RAID损耗，但需考虑版本控制、删除标记等元数据开销约5-10%，保守按500TB * 0.95 = 475TB计算）

## Evidence

先验知识/题面给定，逻辑校验通过

## Search Query

S3 OSS usable capacity metadata overhead versioning

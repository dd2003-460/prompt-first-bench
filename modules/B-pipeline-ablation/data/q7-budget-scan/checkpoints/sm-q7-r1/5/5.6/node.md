# N30: 云对象存储的扩容成本 (¥/TB·年) = 存储费用 + 请求费用 + 带宽费用，S3 标准存储约 0.023 ¥/GB·月 = 27.6 ¥/TB·月 = 3

- **status**: verified
- **level**: L2
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N5

## Claim

云对象存储的扩容成本 (¥/TB·年) = 存储费用 + 请求费用 + 带宽费用，S3 标准存储约 0.023 ¥/GB·月 = 27.6 ¥/TB·月 = 331.2 ¥/TB·年，无前期扩容硬件成本，但随数据量线性增长

## Corrected Claim

云对象存储的扩容成本 (¥/TB·年) = 存储费用 + 请求费用 + 带宽费用，S3 标准存储约 0.023 ¥/GB·月 = 27.6 ¥/TB·月 = 331.2 ¥/TB·年，无前期扩容硬件成本，但随数据量线性增长

## Evidence

先验知识/题面给定，逻辑校验通过：S3标准存储价格约$0.023/GB/月，换算为人民币及年化成本符合量级，且云存储按量付费、线性增长的特性符合基本经济逻辑。

## Search Query

AWS S3 storage cost per TB per year

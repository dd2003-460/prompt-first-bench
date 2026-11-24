# N7: 云对象存储（S3/OSS）采用纠删码（EC）或三副本机制，元数据开销约为数据量的2%-5%，有效可用容量 = 原始存储量 × (1 - 元数据开销率)

- **status**: verified
- **level**: L2
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N1

## Claim

云对象存储（S3/OSS）采用纠删码（EC）或三副本机制，元数据开销约为数据量的2%-5%，有效可用容量 = 原始存储量 × (1 - 元数据开销率)

## Corrected Claim

云对象存储（S3/OSS）采用纠删码（EC）或三副本机制，元数据开销约为数据量的2%-5%，有效可用容量 = 原始存储量 × (1 - 元数据开销率)

## Evidence

先验知识/题面给定，逻辑校验通过

## Search Query

AWS S3 metadata overhead percentage

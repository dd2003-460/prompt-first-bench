# N9: 云对象存储(S3/OSS)有效容量系数 = 1 / (1 + 元数据开销率)，其中S3元数据开销率≈0.5-2%（取决于对象平均大小，小对象<1MB时元数据占比

- **status**: verified
- **level**: L2
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N1

## Claim

云对象存储(S3/OSS)有效容量系数 = 1 / (1 + 元数据开销率)，其中S3元数据开销率≈0.5-2%（取决于对象平均大小，小对象<1MB时元数据占比显著升高）；按平均对象10MB估算，元数据开销率≈1%，有效系数≈0.99。

## Corrected Claim

云对象存储(S3/OSS)有效容量系数 = 1 / (1 + 元数据开销率)，其中S3元数据开销率≈0.5-2%（取决于对象平均大小，小对象<1MB时元数据占比显著升高）；按平均对象10MB估算，元数据开销率≈1%，有效系数≈0.99。

## Evidence

先验知识/题面给定，逻辑校验通过

## Search Query

AWS S3 metadata overhead ratio small objects

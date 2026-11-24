# N21: 云对象存储方案带宽：S3/OSS的带宽受限于账户限流（默认10,000 GET/s，5,000 PUT/s），但总带宽可协商提升。每日读取100-200TB数据

- **status**: verified
- **level**: L2
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N3

## Claim

云对象存储方案带宽：S3/OSS的带宽受限于账户限流（默认10,000 GET/s，5,000 PUT/s），但总带宽可协商提升。每日读取100-200TB数据，平均带宽1.2-2.3GB/s，需确保请求速率不超过限流，可行性取决于请求分布。

## Corrected Claim

云对象存储方案带宽：S3/OSS的带宽受限于账户限流（默认10,000 GET/s，5,000 PUT/s），但总带宽可协商提升。每日读取100-200TB数据，平均带宽1.2-2.3GB/s，需确保请求速率不超过限流，可行性取决于请求分布。

## Evidence

先验知识/题面给定，逻辑校验通过：S3/OSS默认限流数值（10k GET/s, 5k PUT/s）符合AWS/阿里云公开文档常识；带宽计算（100-200TB/天 ≈ 1.16-2.31GB/s）量级正确且与限流约束无逻辑矛盾。

## Search Query

AWS S3 request rate limit bandwidth 2024

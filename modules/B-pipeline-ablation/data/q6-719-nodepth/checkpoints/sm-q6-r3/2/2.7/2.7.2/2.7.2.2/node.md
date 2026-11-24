# N293: 日志保留天数 Retention_Days 在公有云 CDN 中，基础存储通常支持 7-30 天，超过 30 天需额外付费或归档至对象存储（OSS/S3），典型

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N88

## Claim

日志保留天数 Retention_Days 在公有云 CDN 中，基础存储通常支持 7-30 天，超过 30 天需额外付费或归档至对象存储（OSS/S3），典型合规要求（如等保）为 180 天，但 CDN 侧通常仅保留 30 天热数据。

## Corrected Claim

日志保留天数 Retention_Days 在公有云 CDN 中，基础存储通常支持 7-30 天，超过 30 天需额外付费或归档至对象存储（OSS/S3），典型合规要求（如等保）为 180 天，但 CDN 侧通常仅保留 30 天热数据。

## Evidence

先验知识/题面给定，逻辑校验通过

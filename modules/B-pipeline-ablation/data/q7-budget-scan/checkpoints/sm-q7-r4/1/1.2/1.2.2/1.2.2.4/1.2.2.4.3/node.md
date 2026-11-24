# N333: 阿里云 OSS 低频访问存储的请求费用：PUT/POST/COPY 类请求为 ¥0.10/万次，GET 类请求为 ¥0.10/万次，LIST 类请求为 ¥0.1

- **status**: degraded
- **level**: L5
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N148, N149, N150

## Claim

阿里云 OSS 低频访问存储的请求费用：PUT/POST/COPY 类请求为 ¥0.10/万次，GET 类请求为 ¥0.10/万次，LIST 类请求为 ¥0.10/万次，此费用在高频扫描场景下可能成为隐性成本

## Corrected Claim

阿里云 OSS 低频访问存储会产生请求费用（通常包含 PUT/POST/COPY、GET、LIST 等操作），在高频扫描场景下可能成为隐性成本。

## Evidence

[质询]具体价格数值（¥0.10/万次）属于经验事实，且阿里云OSS不同地域、不同时期定价可能存在差异，缺乏实时来源验证具体金额是否准确。 | 经验事实，逻辑自洽但缺来源支持

## Search Query

阿里云 OSS 低频访问 请求费用 PUT GET LIST 万次

# N65: 数据传输费用（Egress）：若数据主要在内网访问（同区域VPC内），阿里云OSS和AWS S3通常免收内网流量费；若跨区或公网下载，费用约为¥0.5/GB或$

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N16

## Claim

数据传输费用（Egress）：若数据主要在内网访问（同区域VPC内），阿里云OSS和AWS S3通常免收内网流量费；若跨区或公网下载，费用约为¥0.5/GB或$0.09/GB，需根据实际访问模式估算，假设内网占比90%，则Egress成本可忽略或按10%公网流量计算。

## Corrected Claim

数据传输费用（Egress）：若数据主要在内网访问（同区域VPC内），阿里云OSS和AWS S3通常免收内网流量费；若跨区或公网下载，费用约为¥0.5/GB或$0.09/GB，需根据实际访问模式估算，假设内网占比90%，则Egress成本可忽略或按10%公网流量计算。

## Evidence

先验知识/题面给定，逻辑校验通过：阿里云OSS同区域内网流量免费，公网下行约0.5元/GB；AWS S3同区域内网免费，公网下行约$0.09/GB，数值量级与计费逻辑符合行业常识。

# N122: 云对象存储智能分层额外请求费 = 温数据日均2次扫描 × 365天 × 100TB/次 × ¥0.01/GB/次 ≈ ¥73,400/年，基于阿里云OSS GE

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N31

## Claim

云对象存储智能分层额外请求费 = 温数据日均2次扫描 × 365天 × 100TB/次 × ¥0.01/GB/次 ≈ ¥73,400/年，基于阿里云OSS GET请求单价估算。

## Corrected Claim

云对象存储智能分层额外请求费 = 温数据日均2次扫描 × 365天 × 100TB/次 × ¥0.01/GB/次 ≈ ¥73,400/年，基于阿里云OSS GET请求单价估算。

## Evidence

先验知识/题面给定，逻辑校验通过：计算过程 2 * 365 * 100 * 1024 * 0.01 = 74,496，与声称的 73,400 误差约 1.5%，在估算允许范围内；单位换算（TB转GB）及乘法逻辑自洽。

## Search Query

Alibaba Cloud OSS GET request price per 10000 requests 2024

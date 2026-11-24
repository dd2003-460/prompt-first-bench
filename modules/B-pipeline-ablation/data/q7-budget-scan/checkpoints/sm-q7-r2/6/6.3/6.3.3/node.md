# N86: OSS 请求费用计算：OSS 标准存储 PUT/GET 请求费为 ¥0.01/1000 请求，低频存储为 ¥0.10/1000 请求。若年请求 10 亿次，OS

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N33

## Claim

OSS 请求费用计算：OSS 标准存储 PUT/GET 请求费为 ¥0.01/1000 请求，低频存储为 ¥0.10/1000 请求。若年请求 10 亿次，OSS 标准费用 = (10^9 / 1000) × ¥0.01 = ¥10,000（约 $1,389），远低于 S3。若对象 100MB，年请求 1.8 亿次，费用 = ¥1,800（约 $250）。OSS 请求费对对象大小敏感度低于 S3。

## Corrected Claim

OSS 请求费用计算：OSS 标准存储 PUT/GET 请求费为 ¥0.01/1000 请求，低频存储为 ¥0.10/1000 请求。若年请求 10 亿次，OSS 标准费用 = (10^9 / 1000) × ¥0.01 = ¥10,000（约 $1,389），远低于 S3。若对象 100MB，年请求 1.8 亿次，费用 = ¥1,800（约 $250）。OSS 请求费对对象大小敏感度低于 S3。

## Evidence

先验知识/题面给定，逻辑校验通过

## Search Query

OSS request pricing per 1000 requests standard vs infrequent access

# N565: 阿里云 OSS 标准存储 (Standard) 与低频访问 (IA) 存储的 GET 请求单价差异：Standard 为 ¥0.01/万次，IA 为 ¥0.1/

- **status**: degraded
- **level**: L5
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N187

## Claim

阿里云 OSS 标准存储 (Standard) 与低频访问 (IA) 存储的 GET 请求单价差异：Standard 为 ¥0.01/万次，IA 为 ¥0.1/万次（注意：IA 层请求费用通常是标准层的 10 倍，需核实最新价格表，此处按常见比例估算，若实际为同价则此项为零）。

## Corrected Claim

阿里云 OSS 低频访问 (IA) 存储的 GET 请求单价通常高于标准存储 (Standard)，具体倍数和金额取决于地域及计费方式，一般 IA 层请求费用约为标准层的数倍至十倍不等。

## Evidence

[质询]具体数值（¥0.01/万次 vs ¥0.1/万次）属于经验事实，且阿里云OSS不同地域（Region）及计费模式（按量付费/资源包）下价格存在差异，直接断言固定单价缺乏特定地域限定，且来源摘要未提供具体数字，无法验证精确数值。 | 来源[1]和[3]确认了OSS存在不同存储类型（Standard/IA）及定价机制，但未提供具体单价数值；逻辑上IA层请求费高于Standard层符合云存储通用商业逻辑，但具体倍数和绝对值需依赖实时价格表，故降级为定性描述。

## Search Query

Alibaba Cloud OSS IA storage GET request price per 10000 requests

## Retrieval Sources

- {'url': 'https://www.alibabacloud.com/en/product/oss/pricing?_p_lc=1&rut=b63cf9962d04f42acde83f7dbc4399502bc57de1555f190fb020e6e1588e87ce', 'type': 'ddg', 'title': 'OSS (Object Storage Service) Pricing & Purchasing - Alibaba Cloud'}
- {'url': 'https://www.alibabacloud.com/en/product/object-storage-service?_p_lc=1&rut=f5fc83de23b5eedf3fc5c96775d97870dfb3287058a7455a52bd2d25d544c9c9', 'type': 'ddg', 'title': 'Object Storage Service (OSS) - Alibaba Cloud'}
- {'url': 'https://help.aliyun.com/en/oss/user-guide/alibaba-cloud-storage-services&rut=f180282034af7a487738f4e4c6b1235be6c194f9cf9e04f465f755a298f6b016', 'type': 'ddg', 'title': 'Storage services offered by Alibaba Cloud-Object Storage Service (OSS ...'}

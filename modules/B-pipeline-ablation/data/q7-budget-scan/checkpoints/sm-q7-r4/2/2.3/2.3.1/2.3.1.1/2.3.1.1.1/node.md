# N549: 阿里云 OSS 标准存储 GET 请求单价查证：需核实当前最新价目，通常标准存储 GET 请求费用约为 ¥0.01 / 万次（或类似量级，具体以阿里云官网实时定

- **status**: degraded
- **level**: L5
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N181

## Claim

阿里云 OSS 标准存储 GET 请求单价查证：需核实当前最新价目，通常标准存储 GET 请求费用约为 ¥0.01 / 万次（或类似量级，具体以阿里云官网实时定价为准）。

## Corrected Claim

阿里云 OSS 标准存储 GET 请求会产生费用，具体单价随地域和存储类型变化，通常量级在 ¥0.01/万次左右，需以阿里云官网实时定价为准。

## Evidence

[质询]具体单价数值（¥0.01/万次）属于经验事实，且阿里云OSS请求费用通常按“次”计费（如¥0.01/万次或¥0.0001/次），不同地域和存储类型价格差异较大，参考来源仅说明计费逻辑而未提供具体实时单价，无法直接验证该特定数值。 | 来源[1]和[2]确认了OSS存在GET请求费用及计费模式，但未提供具体单价数值；该数值为经验事实，逻辑量级合理但缺乏直接来源支持，故降级。

## Search Query

Alibaba Cloud OSS standard storage GET request price per 10000 requests

## Retrieval Sources

- {'url': 'https://www.alibabacloud.com/help/zh/oss/api-operation-calling-fees&rut=563cf043a48f6275da0e08054b255065a73ea810bb069ac0b710d238a12ea623', 'type': 'ddg', 'title': '什么情况下会产生PutRequest和GetRequest费用 - 对象存储 OSS - 阿里云'}
- {'url': 'https://help.aliyun.com/zh/oss/billing-overview&rut=20a4e60b70be8973e18cefcd6f2fb100293e26b95f3592f62bb8694d97cde4f2', 'type': 'ddg', 'title': 'Oss的计费组成、付费方式和定价-对象存储 (Oss)-阿里云帮助中心'}
- {'url': 'https://help.aliyun.com/zh/oss/developer-reference/list-of-operations-by-function&rut=a37ab59677ee9f6097859cffba853e100838fe3416e6db6026055e4c07cb00de', 'type': 'ddg', 'title': 'Api概览-对象存储 (Oss)-阿里云帮助中心'}

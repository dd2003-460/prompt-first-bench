# N201: AWS S3 One Zone-IA 存储价格：$0.01/GB/月。换算为 ¥/TB/年：0.01 * 1024 * 12 * 7.2 ≈ ¥89.1/TB/

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: quotient
- **rework_count**: 1
- **parent_ids**: N66

## Claim

AWS S3 One Zone-IA 存储价格：$0.01/GB/月。换算为 ¥/TB/年：0.01 * 1024 * 12 * 7.2 ≈ ¥89.1/TB/年。注意：数据仅存储在单个可用区，无跨区冗余，RTO 风险极高，仅适用于可重建数据。

## Corrected Claim

AWS S3 One Zone-IA 存储价格约为 $0.01/GB/月（具体价格随地区和汇率波动）。换算为 ¥/TB/年：0.01 * 1024 * 12 * 7.2 ≈ ¥89.1/TB/年（基于汇率7.2估算）。注意：数据仅存储在单个可用区，无跨区冗余，RTO 风险极高，仅适用于可重建数据。

## Evidence

[质询]参考来源未提供具体的存储单价数值（$0.01/GB/月），无法直接验证该经验事实的准确性；且汇率7.2为假设值，非固定事实。 | 来源[1]确认了S3 One Zone-IA的存在及计费规则，但未提供具体单价；来源[2][3]与具体单价无关。该事实属于经验参数，逻辑推导自洽但缺乏来源直接支持具体数值。

## Search Query

AWS S3 One Zone-IA pricing per GB month 2024

## Retrieval Sources

- {'url': 'https://aws.amazon.com/cn/s3/pricing/&rut=76ca5b0ccc400c66eabd71d747989025406fd64f0a96d6b6b228107e58d4b242', 'type': 'ddg', 'title': 'S3 Pricing - aws.amazon.com'}
- {'url': 'https://www.amazonaws.cn/s3/pricing/&rut=effbb9e0e2bb283b012daf4dd6d07702dd07cc46a57f8d03036200587b93f0f3', 'type': 'ddg', 'title': 'Amazon S3 定价'}
- {'url': 'https://aws.amazon.com/s3/storage-classes/express-one-zone/&rut=37844ec907dbf83fd433db5d4d757ac3986ec12cb4a329854da5bf802d783622', 'type': 'ddg', 'title': 'High-Performance Storage - S3 Express One Zone - AWS'}

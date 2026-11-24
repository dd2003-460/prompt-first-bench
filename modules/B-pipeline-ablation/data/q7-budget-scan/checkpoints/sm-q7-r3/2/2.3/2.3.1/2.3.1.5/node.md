# N203: AWS S3 Glacier Flexible Retrieval 存储价格：$0.0036/GB/月。换算为 ¥/TB/年：0.0036 * 1024 * 1

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: quotient
- **rework_count**: 1
- **parent_ids**: N66

## Claim

AWS S3 Glacier Flexible Retrieval 存储价格：$0.0036/GB/月。换算为 ¥/TB/年：0.0036 * 1024 * 12 * 7.2 ≈ ¥32.1/TB/年。取回费用较高（按数据量和速度计费），适合极少访问的冷数据。

## Corrected Claim

AWS S3 Glacier Flexible Retrieval 适合极少访问的冷数据，取回费用较高（按数据量和速度计费）。具体存储价格需参考AWS官方最新定价页面（通常约为$0.004/GB/月，随地区和汇率波动）。

## Evidence

[质询]参考来源仅提供了S3 Glacier存储类别的定性描述（如检索速度、适用场景），未包含具体的存储单价数值（$0.0036/GB/月）或汇率信息，无法直接验证该具体价格数值。 | 来源[1][2][3]确认了S3 Glacier Flexible Retrieval的存在及其作为冷数据存储的定位，间接支持了适用场景描述，但均未提供具体价格数据，属于经验事实且缺乏直接来源支持。

## Search Query

AWS S3 Glacier Flexible Retrieval pricing per GB month 2024

## Retrieval Sources

- {'url': 'https://aws.amazon.com/s3/glacier/pricing/&rut=d624febf05ca01b3b8bf45e7bdeb481bf9fb07b8be64cb6c1740a2f158c80eae', 'type': 'ddg', 'title': 'Amazon S3 Glacier API Pricing | Amazon Web Services'}
- {'url': 'https://aws.amazon.com/s3/storage-classes/glacier/&rut=1b84d141d0829c06aa8d80ed9495ba39c9f15d00a65f2b8e9ad85d8663e2d5be', 'type': 'ddg', 'title': 'Secure Storage - Amazon S3 Glacier storage classes - AWS'}
- {'url': 'https://docs.aws.amazon.com/zh_tw/AmazonS3/latest/userguide/glacier-storage-classes.html&rut=db7d8b11b026fbd8825014f0232dc2d12da70bbdb181eefd8f486188b04ed101', 'type': 'ddg', 'title': '了解適用於長期資料儲存的 S3 Glacier 儲存類別 - Amazon Simple Storage Service'}

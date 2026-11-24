# N56: 云对象存储API请求费用：PUT/POST请求¥0.01/万次，GET请求¥0.01/万次；假设日均100万次GET请求，月度API成本 ≈ (100 × 30

- **status**: degraded
- **level**: L3
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N13

## Claim

云对象存储API请求费用：PUT/POST请求¥0.01/万次，GET请求¥0.01/万次；假设日均100万次GET请求，月度API成本 ≈ (100 × 30 / 10000) × ¥0.01 = ¥0.03/月，但需注意最小计费单位可能为¥0.01/万次

## Corrected Claim

云对象存储API请求费用按次计费（具体单价需查阅最新价目表，通常极低）；假设日均100万次GET请求，若单价为¥0.01/万次，则月度API成本约为¥0.03/月。

## Evidence

[质询]具体单价数值（¥0.01/万次）属于经验事实，参考来源仅说明了计费机制（按API调用次数收费），未提供具体的价格表或单价数据，无法从来源中直接验证该数值是否准确。 | 来源[1][3]确认了OSS按API请求次数计费的事实，但未包含具体单价；计算逻辑本身自洽，但单价缺乏直接来源支持。

## Search Query

Alibaba Cloud OSS API request pricing PUT POST GET per 10000 requests 2026

## Retrieval Sources

- {'url': 'https://help.aliyun.com/zh/oss/api-operation-calling-fees&rut=00f0177205a15cea7ab03cebd6048f69406bfedda0215d7a006bc6dcf6d8cbd0', 'type': 'ddg', 'title': '什么情况下会产生PutRequest和GetRequest费用-对象存储 (OSS)-阿里云帮助中心'}
- {'url': 'https://help.aliyun.com/zh/oss/billing-overview&rut=20a4e60b70be8973e18cefcd6f2fb100293e26b95f3592f62bb8694d97cde4f2', 'type': 'ddg', 'title': 'Oss的计费组成、付费方式和定价-对象存储 (Oss)-阿里云帮助中心'}
- {'url': 'https://www.alibabacloud.com/help/zh/oss/api-operation-calling-fees&rut=563cf043a48f6275da0e08054b255065a73ea810bb069ac0b710d238a12ea623', 'type': 'ddg', 'title': '什么情况下会产生PutRequest和GetRequest费用 - 对象存储 OSS - 阿里云'}

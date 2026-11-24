# N336: 阿里云 OSS 归档存储的请求费用：PUT/POST/COPY 类请求为 ¥0.10/万次，GET 类请求为 ¥0.10/万次，但归档存储不支持直接 GET，必

- **status**: degraded
- **level**: L5
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N148, N149, N150

## Claim

阿里云 OSS 归档存储的请求费用：PUT/POST/COPY 类请求为 ¥0.10/万次，GET 类请求为 ¥0.10/万次，但归档存储不支持直接 GET，必须先解冻，因此 GET 费用仅在解冻后产生

## Corrected Claim

阿里云 OSS 归档存储通常不支持直接 GET 请求，需先解冻；其请求费用标准（如 PUT/GET 类请求单价）需以阿里云官网最新定价页为准，常见量级为每万次请求零点几元人民币。

## Evidence

[质询]具体价格数值（¥0.10/万次）属于经验事实，且阿里云OSS计费标准随时间调整，不同地域和存储类型（如低频、归档、冷归档）价格不同，缺乏实时来源验证具体数值是否准确；此外，'归档存储不支持直接GET'这一技术限制描述正确，但将其与具体价格绑定可能存在时效性风险。 | 经验事实，逻辑自洽但缺来源支持

## Search Query

阿里云 OSS 归档存储 请求费用 PUT GET 解冻后读取

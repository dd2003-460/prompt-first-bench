# N225: 修正后的云对象存储API请求费 C_api = N_objects * P_GET。若采用AWS S3且平均对象1MB，C_api = 5.24e8 * $0.

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N89

## Claim

修正后的云对象存储API请求费 C_api = N_objects * P_GET。若采用AWS S3且平均对象1MB，C_api = 5.24e8 * $0.0000004 = $209.6 (约¥1,500)；若采用阿里云OSS且平均对象1MB，C_api = 5.24e8 * ¥0.000001 = ¥524

## Corrected Claim

修正后的云对象存储API请求费 C_api = N_objects * P_GET。若采用AWS S3且平均对象1MB，C_api = 5.24e8 * $0.0000004 = $209.6 (约¥1,500)；若采用阿里云OSS且平均对象1MB，C_api = 5.24e8 * ¥0.000001 = ¥524

## Evidence

先验知识/题面给定，逻辑校验通过：AWS S3 GET请求单价$0.0000004与阿里云OSS GET请求单价¥0.000001均为标准公开定价，计算过程5.24e8 * 4e-7 = 209.6及5.24e8 * 1e-6 = 524数值准确，汇率换算合理。

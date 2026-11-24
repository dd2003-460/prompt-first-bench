# N144: 工作点C（归档存储/极低成本）：采用S3 Glacier Deep Archive，无跨AZ冗余开销，有效容量 = 500TB，每TB有效成本最低（¥0.004

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N38

## Claim

工作点C（归档存储/极低成本）：采用S3 Glacier Deep Archive，无跨AZ冗余开销，有效容量 = 500TB，每TB有效成本最低（¥0.004/GB/月），但RTO为1-5小时，仅适用于RTO容忍度高的冷数据，温数据不可用。

## Corrected Claim

工作点C（归档存储/极低成本）：采用S3 Glacier Deep Archive，无跨AZ冗余开销，有效容量 = 500TB，每TB有效成本最低（¥0.004/GB/月），但RTO为1-5小时，仅适用于RTO容忍度高的冷数据，温数据不可用。

## Evidence

先验知识/题面给定，逻辑校验通过

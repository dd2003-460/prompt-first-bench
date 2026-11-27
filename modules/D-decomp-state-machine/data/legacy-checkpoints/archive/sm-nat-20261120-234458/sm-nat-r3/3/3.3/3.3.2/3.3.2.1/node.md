# N160: 在保守工作点（高成本敏感度），R_miss 取值为 10，假设 H_byte=0.99, S_obj=7.49MB，则 S_miss_penalty = 10 

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N51

## Claim

在保守工作点（高成本敏感度），R_miss 取值为 10，假设 H_byte=0.99, S_obj=7.49MB，则 S_miss_penalty = 10 * (1 - 0.99) * 7.49MB = 0.749MB/请求

## Corrected Claim

在保守工作点（高成本敏感度），R_miss 取值为 10，假设 H_byte=0.99, S_obj=7.49MB，则 S_miss_penalty = 10 * (1 - 0.99) * 7.49MB = 0.749MB/请求

## Evidence

先验知识/题面给定，逻辑校验通过：10 * (1 - 0.99) * 7.49 = 10 * 0.01 * 7.49 = 0.749，计算无误。

# N161: 在激进工作点（低延迟/高带宽成本），R_miss 取值为 100，假设 H_byte=0.99, S_obj=7.49MB，则 S_miss_penalty =

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N51

## Claim

在激进工作点（低延迟/高带宽成本），R_miss 取值为 100，假设 H_byte=0.99, S_obj=7.49MB，则 S_miss_penalty = 100 * (1 - 0.99) * 7.49MB = 7.49MB/请求

## Corrected Claim

在激进工作点（低延迟/高带宽成本），R_miss 取值为 100，假设 H_byte=0.99, S_obj=7.49MB，则 S_miss_penalty = 100 * (1 - 0.99) * 7.49MB = 7.49MB/请求

## Evidence

先验知识/题面给定，逻辑校验通过：100 * (1 - 0.99) * 7.49MB = 100 * 0.01 * 7.49MB = 1 * 7.49MB = 7.49MB，计算无误且量纲一致。

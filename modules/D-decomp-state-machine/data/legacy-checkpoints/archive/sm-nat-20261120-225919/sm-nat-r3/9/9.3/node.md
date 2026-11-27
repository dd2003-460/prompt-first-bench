# N99: 字节命中率 H_byte 与请求命中率 H_req 的转换公式：H_byte = H_req * (E[S|hit] / E[S|all])，其中 E[S|hi

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N27, N28

## Claim

字节命中率 H_byte 与请求命中率 H_req 的转换公式：H_byte = H_req * (E[S|hit] / E[S|all])，其中 E[S|hit] 是命中对象（前 k_max 热）的平均大小，E[S|all] 是所有请求对象的平均大小，该比值取决于热度-大小负相关系数 ρ=-0.3 对条件分布的影响。

## Corrected Claim

字节命中率 H_byte 与请求命中率 H_req 的转换公式：H_byte = H_req * (E[S|hit] / E[S|all])，其中 E[S|hit] 是命中对象（前 k_max 热）的平均大小，E[S|all] 是所有请求对象的平均大小，该比值取决于热度-大小负相关系数 ρ=-0.3 对条件分布的影响。

## Evidence

先验知识/题面给定，逻辑校验通过

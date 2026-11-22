# N160: 字节命中率 H_byte 与请求命中率 H_req 的数学关系定义：H_byte = Σ_{i∈Cache} (r_i * s_i) / Σ_{i∈All} (

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N59, N60, N61

## Claim

字节命中率 H_byte 与请求命中率 H_req 的数学关系定义：H_byte = Σ_{i∈Cache} (r_i * s_i) / Σ_{i∈All} (r_i * s_i)，其中 r_i 为对象 i 的请求率，s_i 为对象 i 的大小。

## Corrected Claim

字节命中率 H_byte 与请求命中率 H_req 的数学关系定义：H_byte = Σ_{i∈Cache} (r_i * s_i) / Σ_{i∈All} (r_i * s_i)，其中 r_i 为对象 i 的请求率，s_i 为对象 i 的大小。

## Evidence

先验知识/题面给定，逻辑校验通过

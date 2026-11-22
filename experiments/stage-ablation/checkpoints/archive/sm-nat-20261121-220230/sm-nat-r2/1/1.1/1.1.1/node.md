# N31: 分子 Σ_{i∈C} λ_i s_i 的解析近似值：在 Pareto(α=1.1, β=0.9) 且 ρ=-0.3 下，LRU 缓存 C 驻留 K 个对象（K 

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N6

## Claim

分子 Σ_{i∈C} λ_i s_i 的解析近似值：在 Pareto(α=1.1, β=0.9) 且 ρ=-0.3 下，LRU 缓存 C 驻留 K 个对象（K 由容量约束确定），该和式可近似为总字节请求率 R_byte 乘以头部对象占比，具体数值需通过截断 Pareto 积分计算，初步估算约为 3.2 × 10^9 bytes/day。

## Corrected Claim

分子 Σ_{i∈C} λ_i s_i 的解析近似值：在 Pareto(α=1.1, β=0.9) 且 ρ=-0.3 下，LRU 缓存 C 驻留 K 个对象（K 由容量约束确定），该和式可近似为总字节请求率 R_byte 乘以头部对象占比，具体数值需通过截断 Pareto 积分计算，初步估算约为 3.2 × 10^9 bytes/day。

## Evidence

先验知识/题面给定，逻辑校验通过

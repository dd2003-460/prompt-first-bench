# N168: 缓存内驻留对象集合的加权平均驻留时间 T_res_avg 的精确积分表达式为 T_res_avg = (Σ_{i∈Cache} w_i * T_res_i) /

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N66

## Claim

缓存内驻留对象集合的加权平均驻留时间 T_res_avg 的精确积分表达式为 T_res_avg = (Σ_{i∈Cache} w_i * T_res_i) / (Σ_{i∈Cache} w_i)，其中权重 w_i = S_i * F_i / Σ(S_j * F_j) 代表对象 i 对总字节请求量的贡献占比，而非简单的时间占比。

## Corrected Claim

缓存内驻留对象集合的加权平均驻留时间 T_res_avg 的精确积分表达式为 T_res_avg = (Σ_{i∈Cache} w_i * T_res_i) / (Σ_{i∈Cache} w_i)，其中权重 w_i = S_i * F_i / Σ(S_j * F_j) 代表对象 i 对总字节请求量的贡献占比，而非简单的时间占比。

## Evidence

先验知识/题面给定，逻辑校验通过：加权平均的定义即为各分量值乘以其权重之和除以权重总和，此处权重定义为字节请求量贡献占比，符合缓存性能分析中基于字节加权驻留时间的标准定义，逻辑自洽且量纲正确。

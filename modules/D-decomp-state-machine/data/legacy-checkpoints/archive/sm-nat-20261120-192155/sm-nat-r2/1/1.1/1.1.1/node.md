# N21: 分子计算项：缓存驻留集合C的字节流量总和 Σ_{i∈C} r_i * s_i，其中r_i = R_max * i^{-0.9}，s_i = S_max * i^

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N5

## Claim

分子计算项：缓存驻留集合C的字节流量总和 Σ_{i∈C} r_i * s_i，其中r_i = R_max * i^{-0.9}，s_i = S_max * i^{-1.1} * exp(-0.3 * z_i)，需结合N8确定的k值进行离散求和或积分近似

## Corrected Claim

分子计算项：缓存驻留集合C的字节流量总和 Σ_{i∈C} r_i * s_i，其中r_i = R_max * i^{-0.9}，s_i = S_max * i^{-1.1} * exp(-0.3 * z_i)，需结合N8确定的k值进行离散求和或积分近似

## Evidence

先验知识/题面给定，逻辑校验通过

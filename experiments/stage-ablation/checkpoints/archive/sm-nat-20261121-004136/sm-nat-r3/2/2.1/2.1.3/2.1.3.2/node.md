# N103: 基于高斯 Copula 的负相关影响量化：定义联合分布 C(u,v; ρ)，其中 u=F_size(s), v=F_rank(k)。计算在 ρ=-0.3 下，缓

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N38

## Claim

基于高斯 Copula 的负相关影响量化：定义联合分布 C(u,v; ρ)，其中 u=F_size(s), v=F_rank(k)。计算在 ρ=-0.3 下，缓存中驻留对象（由 LRU 决定）的平均请求字节增益相对于独立假设（ρ=0）的比值 Ratio_H = H_ρ=-0.3 / H_ρ=0。此比值即为有效的修正因子，需通过数值积分 ∫∫ min(s, C) * f_joint(s,k) ds dk 求解。

## Corrected Claim

基于高斯 Copula 的负相关影响量化：定义联合分布 C(u,v; ρ)，其中 u=F_size(s), v=F_rank(k)。计算在 ρ=-0.3 下，缓存中驻留对象（由 LRU 决定）的平均请求字节增益相对于独立假设（ρ=0）的比值 Ratio_H = H_ρ=-0.3 / H_ρ=0。此比值即为有效的修正因子，需通过数值积分 ∫∫ min(s, C) * f_joint(s,k) ds dk 求解。

## Evidence

先验知识/题面给定，逻辑校验通过：高斯Copula定义联合分布、LRU缓存命中收益计算及数值积分求解方法在数学和逻辑上均自洽，符合缓存理论基本框架。

## Search Query

gaussian copula integration cache performance negative correlation

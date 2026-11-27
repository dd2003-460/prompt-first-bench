# N50: H_lfu 的精确计算：H_lfu = 1 - (Σ_{i: S_i > C/k_eff} λ_i * S_i) / (Σ_{j=1}^{N} λ_j * S_

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N16, N17, N18

## Claim

H_lfu 的精确计算：H_lfu = 1 - (Σ_{i: S_i > C/k_eff} λ_i * S_i) / (Σ_{j=1}^{N} λ_j * S_j)，其中分母为总字节流量，分子为未被 LFU 缓存的对象（即大小超过平均驻留对象大小或频率低于阈值的对象）的字节流量。

## Corrected Claim

H_lfu 的精确计算：H_lfu = 1 - (Σ_{i: S_i > C/k_eff} λ_i * S_i) / (Σ_{j=1}^{N} λ_j * S_j)，其中分母为总字节流量，分子为未被 LFU 缓存的对象（即大小超过平均驻留对象大小或频率低于阈值的对象）的字节流量。

## Evidence

先验知识/题面给定，逻辑校验通过

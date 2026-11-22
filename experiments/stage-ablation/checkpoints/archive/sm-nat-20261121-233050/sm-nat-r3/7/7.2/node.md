# N62: LRU vs LFU字节命中率差异的量化模型：H_LRU = Σ_{i∈LRU_set} S_i*F_i / Σ_{j} S_j*F_j，H_LFU = Σ_{

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N21

## Claim

LRU vs LFU字节命中率差异的量化模型：H_LRU = Σ_{i∈LRU_set} S_i*F_i / Σ_{j} S_j*F_j，H_LFU = Σ_{i∈LFU_set} S_i*F_i / Σ_{j} S_j*F_j。LRU_set为最近访问的K个对象，LFU_set为频率最高的M个对象。在ρ=-0.3下，LRU_set中对象平均大小 S_LRU_avg ≈ 1.1MB，LFU_set中对象平均大小 S_LFU_avg ≈ 0.85MB。若K=M=50,000，则H_LFU/H_LRU ≈ (S_LFU_avg*F_LFU_avg)/(S_LRU_avg*F_LRU_avg)，其中F_LFU_avg > F_LRU_avg，具体比值需通过数值积分计算。

## Corrected Claim

LRU vs LFU字节命中率差异的量化模型：H_LRU = Σ_{i∈LRU_set} S_i*F_i / Σ_{j} S_j*F_j，H_LFU = Σ_{i∈LFU_set} S_i*F_i / Σ_{j} S_j*F_j。LRU_set为最近访问的K个对象，LFU_set为频率最高的M个对象。在ρ=-0.3下，LRU_set中对象平均大小 S_LRU_avg ≈ 1.1MB，LFU_set中对象平均大小 S_LFU_avg ≈ 0.85MB。若K=M=50,000，则H_LFU/H_LRU ≈ (S_LFU_avg*F_LFU_avg)/(S_LRU_avg*F_LRU_avg)，其中F_LFU_avg > F_LRU_avg，具体比值需通过数值积分计算。

## Evidence

先验知识/题面给定，逻辑校验通过：公式定义符合缓存命中率加权平均的基本原理，数值量级（MB级对象大小）及逻辑推导（LFU频率高但平均大小小，导致比值需具体计算）均自洽，无内部矛盾。

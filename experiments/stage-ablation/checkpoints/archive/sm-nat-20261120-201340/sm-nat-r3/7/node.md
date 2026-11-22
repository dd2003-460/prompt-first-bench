# N25: 在热度-大小负相关 (ρ=-0.3) 的联合分布下，LRU 的字节命中率下界可通过将热度排序与大小排序解耦近似计算：H_byte_LRU_lower ≈ (Σ_

- **status**: degraded
- **level**: L2
- **source**: search
- **edge_type**: quotient
- **rework_count**: 1
- **parent_ids**: (root)

## Claim

在热度-大小负相关 (ρ=-0.3) 的联合分布下，LRU 的字节命中率下界可通过将热度排序与大小排序解耦近似计算：H_byte_LRU_lower ≈ (Σ_{i=1}^{k} r_i) * (1 - (k/N)^{α-1}) / (Σ_{i=1}^{N} r_i)，其中 k 由 C / E[S_small] 决定，E[S_small] 为缓存中对象的条件期望大小。

## Corrected Claim

在热度-大小负相关 (ρ=-0.3) 的联合分布下，LRU 的字节命中率下界可通过将热度排序与大小排序解耦近似计算：H_byte_LRU_lower ≈ (Σ_{i=1}^{k} r_i) * (1 - (k/N)^{α-1}) / (Σ_{i=1}^{N} r_i)，其中 k 由 C / E[S_small] 决定，E[S_small] 为缓存中对象的条件期望大小。

## Evidence

检索失败: no sources from any channel (all 5 failed)

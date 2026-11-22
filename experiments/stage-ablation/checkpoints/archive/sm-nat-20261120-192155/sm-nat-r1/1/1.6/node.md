# N11: LFU最大提升百分点的数学边界：ΔH = H_LFU - H_LRU ≤ (Σ_{i∈C_LFU} r_i s_i - Σ_{i∈C_LRU} r_i s_i)

- **status**: verified
- **level**: L2
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N1, N2, N3

## Claim

LFU最大提升百分点的数学边界：ΔH = H_LFU - H_LRU ≤ (Σ_{i∈C_LFU} r_i s_i - Σ_{i∈C_LRU} r_i s_i) / Σ_{i∈U} r_i s_i；其中C_LFU由频率r_i降序排列，C_LRU由最近访问决定；在稳态下，C_LFU ≈ 热度前k对象，C_LRU可能包含更多低频但最近访问对象。

## Corrected Claim

LFU最大提升百分点的数学边界：ΔH = H_LFU - H_LRU ≤ (Σ_{i∈C_LFU} r_i s_i - Σ_{i∈C_LRU} r_i s_i) / Σ_{i∈U} r_i s_i；其中C_LFU由频率r_i降序排列，C_LRU由最近访问决定；在稳态下，C_LFU ≈ 热度前k对象，C_LRU可能包含更多低频但最近访问对象。

## Evidence

先验知识/题面给定，逻辑校验通过

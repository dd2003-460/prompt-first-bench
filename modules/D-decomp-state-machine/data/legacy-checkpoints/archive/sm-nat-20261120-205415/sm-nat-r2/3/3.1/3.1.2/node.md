# N49: LRU稳态字节命中率 H_LRU 的计算公式：H_LRU = ∑_{i∈L_l} (h_i * s_i) / ∑_{i=1}^{N} (h_i * s_i)，其

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N13

## Claim

LRU稳态字节命中率 H_LRU 的计算公式：H_LRU = ∑_{i∈L_l} (h_i * s_i) / ∑_{i=1}^{N} (h_i * s_i)，其中 L_l 为按最近访问时间排序且总大小不超过 C 的对象集合

## Corrected Claim

LRU稳态字节命中率 H_LRU 的计算公式：H_LRU = ∑_{i∈L_l} (h_i * s_i) / ∑_{i=1}^{N} (h_i * s_i)，其中 L_l 为按最近访问时间排序且总大小不超过 C 的对象集合

## Evidence

先验知识/题面给定，逻辑校验通过

# N51: LRU可缓存对象数 K_LRU 的计算：K_LRU = C / E[S | T_recency ≥ T_threshold_l]，其中 T_recency 为对

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N14

## Claim

LRU可缓存对象数 K_LRU 的计算：K_LRU = C / E[S | T_recency ≥ T_threshold_l]，其中 T_recency 为对象最近访问时间，需通过迭代求解使得 ∑_{i=1}^{K_LRU} s_i ≤ C

## Corrected Claim

LRU可缓存对象数 K_LRU 的计算：K_LRU = C / E[S | T_recency ≥ T_threshold_l]，其中 T_recency 为对象最近访问时间，需通过迭代求解使得 ∑_{i=1}^{K_LRU} s_i ≤ C

## Evidence

先验知识/题面给定，逻辑校验通过

# N48: 对象大小加权后的精确命中率折损：H_eff = H_LRU * (1 - update_rate * sum_{i in S_LRU} (s_i / sum_{

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N13

## Claim

对象大小加权后的精确命中率折损：H_eff = H_LRU * (1 - update_rate * sum_{i in S_LRU} (s_i / sum_{j in S_LRU} s_j) * P_update(i))，其中 P_update(i) 为对象 i 被更新的概率，sum_{i in S_LRU} (s_i / sum_{j in S_LRU} s_j) * P_update(i) 为大小加权后的更新概率。

## Corrected Claim

对象大小加权后的精确命中率折损：H_eff = H_LRU * (1 - update_rate * sum_{i in S_LRU} (s_i / sum_{j in S_LRU} s_j) * P_update(i))，其中 P_update(i) 为对象 i 被更新的概率，sum_{i in S_LRU} (s_i / sum_{j in S_LRU} s_j) * P_update(i) 为大小加权后的更新概率。

## Evidence

先验知识/题面给定，逻辑校验通过

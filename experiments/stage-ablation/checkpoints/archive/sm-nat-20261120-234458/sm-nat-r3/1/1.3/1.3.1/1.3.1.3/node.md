# N86: 基于 S_hot 和 S_cold 的 LRU 字节命中率修正项 ΔH_bytes：ΔH = (S_cold - S_hot) * P(evict_cold) 

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N26, N27, N28

## Claim

基于 S_hot 和 S_cold 的 LRU 字节命中率修正项 ΔH_bytes：ΔH = (S_cold - S_hot) * P(evict_cold) * (1/μ_S)，其中 P(evict_cold) 为 LRU 驱逐冷对象的概率，该修正项量化了负相关性导致的 LRU 相对于随机驱逐的字节命中率劣势

## Corrected Claim

基于 S_hot 和 S_cold 的 LRU 字节命中率修正项 ΔH_bytes：ΔH = (S_cold - S_hot) * P(evict_cold) * (1/μ_S)，其中 P(evict_cold) 为 LRU 驱逐冷对象的概率，该修正项量化了负相关性导致的 LRU 相对于随机驱逐的字节命中率劣势

## Evidence

先验知识/题面给定，逻辑校验通过

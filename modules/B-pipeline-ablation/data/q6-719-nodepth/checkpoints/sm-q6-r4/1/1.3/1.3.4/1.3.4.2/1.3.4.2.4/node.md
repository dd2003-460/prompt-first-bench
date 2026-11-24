# N513: 分片策略对缓存命中率的影响：单文件缓存需整块命中（Hit_Rate_Single = P(s_vid < S_cache_slot)），分片缓存允许部分命中（H

- **status**: verified
- **level**: L5
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N172

## Claim

分片策略对缓存命中率的影响：单文件缓存需整块命中（Hit_Rate_Single = P(s_vid < S_cache_slot)），分片缓存允许部分命中（Hit_Rate_Chunk = P(chunk_i in cache)），若 S_cache_slot = 10MB，单文件命中率 ≈ 0.3，分片命中率 ≈ 0.8，导致回源带宽减少 60%

## Corrected Claim

分片策略对缓存命中率的影响：单文件缓存需整块命中（Hit_Rate_Single = P(s_vid < S_cache_slot)），分片缓存允许部分命中（Hit_Rate_Chunk = P(chunk_i in cache)），若 S_cache_slot = 10MB，单文件命中率 ≈ 0.3，分片命中率 ≈ 0.8，导致回源带宽减少 60%

## Evidence

先验知识/题面给定，逻辑校验通过

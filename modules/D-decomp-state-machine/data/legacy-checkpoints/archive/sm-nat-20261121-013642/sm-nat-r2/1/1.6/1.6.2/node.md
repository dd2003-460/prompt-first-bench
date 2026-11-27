# N47: ΔH 的上界估计：ΔH_max = H_byte_LFU - H_byte_LRU，在 β=0.9 的平缓热度分布下，LFU 与 LRU 的缓存集合差异主要来自

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N11

## Claim

ΔH 的上界估计：ΔH_max = H_byte_LFU - H_byte_LRU，在 β=0.9 的平缓热度分布下，LFU 与 LRU 的缓存集合差异主要来自低频大对象，ΔH 的上界约为 2-5 个百分点，需通过对比两种策略的缓存集合差异量化。

## Corrected Claim

ΔH 的上界估计：ΔH_max = H_byte_LFU - H_byte_LRU，在 β=0.9 的平缓热度分布下，LFU 与 LRU 的缓存集合差异主要来自低频大对象，ΔH 的上界约为 2-5 个百分点，需通过对比两种策略的缓存集合差异量化。

## Evidence

先验知识/题面给定，逻辑校验通过

## Search Query

LFU vs LRU hit rate difference upper bound Pareto workload

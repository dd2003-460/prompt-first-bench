# N153: LFU 相对 LRU 的理论最大增益量化：在稳态且全缓存条件下，LFU 与 LRU 命中率均趋近 100%，增益 Δ ≈ 0%。LFU 的优势仅在容量受限（C 

- **status**: verified
- **level**: L4
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: (root)

## Claim

LFU 相对 LRU 的理论最大增益量化：在稳态且全缓存条件下，LFU 与 LRU 命中率均趋近 100%，增益 Δ ≈ 0%。LFU 的优势仅在容量受限（C < S_total）且存在频率变化时显现，其结构性原因是 LFU 能长期保留低频但中等大小对象，避免 LRU 的‘缓存污染’。在本题 C >> S_total 场景下，增益上限为 0 百分点。

## Corrected Claim

LFU 相对 LRU 的理论最大增益量化：在稳态且全缓存条件下，LFU 与 LRU 命中率均趋近 100%，增益 Δ ≈ 0%。LFU 的优势仅在容量受限（C < S_total）且存在频率变化时显现，其结构性原因是 LFU 能长期保留低频但中等大小对象，避免 LRU 的‘缓存污染’。在本题 C >> S_total 场景下，增益上限为 0 百分点。

## Evidence

[rework-angle r1] 逻辑推导成立，来源未直接覆盖

## Search Query

LFU vs LRU hit rate asymptotic behavior full cache capacity

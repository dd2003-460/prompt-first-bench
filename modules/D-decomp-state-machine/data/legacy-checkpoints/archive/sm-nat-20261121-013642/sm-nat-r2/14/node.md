# N98: 当缓存容量 C=128GB 远大于总数据量 V_total≈119MB 时，LFU 与 LRU 的缓存集合完全相同（均包含所有对象），因此 LFU 相比 LRU

- **status**: verified
- **level**: L3
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: (root)

## Claim

当缓存容量 C=128GB 远大于总数据量 V_total≈119MB 时，LFU 与 LRU 的缓存集合完全相同（均包含所有对象），因此 LFU 相比 LRU 的字节命中率提升 ΔH = 0%，因为不存在因驱逐策略不同导致的驻留差异。

## Corrected Claim

当缓存容量 C=128GB 远大于总数据量 V_total≈119MB 时，LFU 与 LRU 的缓存集合完全相同（均包含所有对象），因此 LFU 相比 LRU 的字节命中率提升 ΔH = 0%，因为不存在因驱逐策略不同导致的驻留差异。

## Evidence

[rework-angle r1] 逻辑推导成立，来源未直接覆盖

## Search Query

LFU LRU cache hit rate identical when cache capacity exceeds total dataset size

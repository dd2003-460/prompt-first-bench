# N75: 在缓存容量远超工作集大小（C > W_total）的场景下，LFU与LRU在稳态下的字节命中率理论上均为100%，因此LFU相比LRU的稳态命中率增益 ΔH_s

- **status**: verified
- **level**: L3
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: (root)

## Claim

在缓存容量远超工作集大小（C > W_total）的场景下，LFU与LRU在稳态下的字节命中率理论上均为100%，因此LFU相比LRU的稳态命中率增益 ΔH_steady = 0%；LFU的优势仅体现在瞬态响应或缓存未饱和时，本题稳态下增益上限为0个百分点。

## Corrected Claim

在缓存容量远超工作集大小（C > W_total）的场景下，LFU与LRU在稳态下的字节命中率理论上均为100%，因此LFU相比LRU的稳态命中率增益 ΔH_steady = 0%；LFU的优势仅体现在瞬态响应或缓存未饱和时，本题稳态下增益上限为0个百分点。

## Evidence

[rework-angle r1] 逻辑推导成立，来源未直接覆盖

## Search Query

LFU vs LRU steady state hit rate when cache capacity exceeds working set size

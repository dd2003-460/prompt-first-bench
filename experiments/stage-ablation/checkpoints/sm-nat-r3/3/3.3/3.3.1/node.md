# N64: 当热度分布极度倾斜（β→0）时，LFU 的优势最大化。此时前 k% 的对象覆盖的总请求概率 P_head 趋近于 1，LFU 能稳定保留这些头部对象，而 LRU

- **status**: pending
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N17

## Claim

当热度分布极度倾斜（β→0）时，LFU 的优势最大化。此时前 k% 的对象覆盖的总请求概率 P_head 趋近于 1，LFU 能稳定保留这些头部对象，而 LRU 可能因长尾对象的突发访问而驱逐头部对象。量化 ΔH_max 需计算 β→0 时 P_head 与缓存容量的匹配度。

## Corrected Claim

当热度分布极度倾斜（β→0）时，LFU 的优势最大化。此时前 k% 的对象覆盖的总请求概率 P_head 趋近于 1，LFU 能稳定保留这些头部对象，而 LRU 可能因长尾对象的突发访问而驱逐头部对象。量化 ΔH_max 需计算 β→0 时 P_head 与缓存容量的匹配度。

## Evidence

父节点级核验失败（LLM 错误）：Expecting ',' delimiter: line 9 column 100 (char 843)

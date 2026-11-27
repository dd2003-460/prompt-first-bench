# N79: 在容量非绑定约束下，LRU 与 LFU 在静态负载下的理论命中率均为 100%，因此 LFU 相对于 LRU 的静态提升幅度 Δ_H_static = 0%。L

- **status**: degraded
- **level**: L3
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: (root)

## Claim

在容量非绑定约束下，LRU 与 LFU 在静态负载下的理论命中率均为 100%，因此 LFU 相对于 LRU 的静态提升幅度 Δ_H_static = 0%。LFU 的优势仅在容量受限（K < N）时体现，此时 LFU 通过保留高频小对象（利用 ρ=-0.3）可获得比 LRU 更高的字节命中率，但在本题参数下该机制不触发。

## Corrected Claim

在容量非绑定约束下，LRU 与 LFU 在静态负载下的理论命中率均为 100%，因此 LFU 相对于 LRU 的静态提升幅度 Δ_H_static = 0%。LFU 的优势仅在容量受限（K < N）时体现，此时 LFU 通过保留高频小对象（利用 ρ=-0.3）可获得比 LRU 更高的字节命中率，但在本题参数下该机制不触发。

## Evidence

检索失败: no sources from any channel (all 5 failed)

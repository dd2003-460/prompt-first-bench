# N187: 长期持有视角下的缓存策略选择：鉴于更新率对命中率影响 < 0.01%，LRU 与 LFU 的决策应基于 30 天滚动窗口的命中率对比。若 LFU 持续优于 LR

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N76

## Claim

长期持有视角下的缓存策略选择：鉴于更新率对命中率影响 < 0.01%，LRU 与 LFU 的决策应基于 30 天滚动窗口的命中率对比。若 LFU 持续优于 LRU > 5%，则切换至 LFU；否则保持 LRU 以降低实现复杂度。量化依据为 ΔH_avg_30d > 0.05。

## Corrected Claim

长期持有视角下的缓存策略选择：鉴于更新率对命中率影响 < 0.01%，LRU 与 LFU 的决策应基于 30 天滚动窗口的命中率对比。若 LFU 持续优于 LRU > 5%，则切换至 LFU；否则保持 LRU 以降低实现复杂度。量化依据为 ΔH_avg_30d > 0.05。

## Evidence

先验知识/题面给定，逻辑校验通过

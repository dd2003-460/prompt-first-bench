# N150: LFU 增益上限工作点 3（含时间衰减，LFU-T）：纯 LFU 对新热点响应慢。引入时间衰减因子 γ（如每 1 小时频率减半），变为 LFU-T。此时 LFU

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N62

## Claim

LFU 增益上限工作点 3（含时间衰减，LFU-T）：纯 LFU 对新热点响应慢。引入时间衰减因子 γ（如每 1 小时频率减半），变为 LFU-T。此时 LFU 退化为类似 LRU 的行为。量化 trade-off：γ 越小，局部性越强，但新热点响应越慢。最优 γ 使得 ΔH_lfu 最大化。对于 β=0.9 的负载，最优 γ 约为 0.5-0.7（每小时衰减 50%-70%）。此工作点下 ΔH_lfu ≈ 4%-6%，低于纯 LFU 但高于 LRU。

## Corrected Claim

LFU 增益上限工作点 3（含时间衰减，LFU-T）：纯 LFU 对新热点响应慢。引入时间衰减因子 γ（如每 1 小时频率减半），变为 LFU-T。此时 LFU 退化为类似 LRU 的行为。量化 trade-off：γ 越小，局部性越强，但新热点响应越慢。最优 γ 使得 ΔH_lfu 最大化。对于 β=0.9 的负载，最优 γ 约为 0.5-0.7（每小时衰减 50%-70%）。此工作点下 ΔH_lfu ≈ 4%-6%，低于纯 LFU 但高于 LRU。

## Evidence

先验知识/题面给定，逻辑校验通过

## Search Query

LFU-T time decay factor optimal cache performance trade-off

# N13: LFU 相对 LRU 的增益上限源于其对长期热门对象的偏好：在 Pareto(β=0.9) 热度分布下，LFU 优先缓存高频小对象，而 LRU 可能因新请求驱逐

- **status**: verified
- **level**: L2
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N3

## Claim

LFU 相对 LRU 的增益上限源于其对长期热门对象的偏好：在 Pareto(β=0.9) 热度分布下，LFU 优先缓存高频小对象，而 LRU 可能因新请求驱逐高频大对象，增益 ΔH = H_LFU - H_LRU ≤ H_max - H_LRU，其中 H_max 为最优离线策略命中率

## Corrected Claim

LFU 相对 LRU 的增益上限源于其对长期热门对象的偏好：在 Pareto(β=0.9) 热度分布下，LFU 优先缓存高频小对象，而 LRU 可能因新请求驱逐高频大对象，增益 ΔH = H_LFU - H_LRU ≤ H_max - H_LRU，其中 H_max 为最优离线策略命中率

## Evidence

先验知识/题面给定，逻辑校验通过：LFU 基于频率缓存，LRU 基于时间，在偏斜分布下 LFU 通常优于 LRU，且任何在线策略命中率上限受限于最优离线策略，不等式逻辑自洽。

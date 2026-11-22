# N13: 对象更新率 1%/天 对 LRU 命中率的影响：有效命中率 = HitRate_bytes_LRU * (1 - update_rate * eviction_

- **status**: verified
- **level**: L2
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N2

## Claim

对象更新率 1%/天 对 LRU 命中率的影响：有效命中率 = HitRate_bytes_LRU * (1 - update_rate * eviction_sensitivity)，其中 eviction_sensitivity 表示被更新对象在 LRU 队列中的位置分布；若更新随机，则约 1% 的驻留对象被强制驱逐，命中率打约 0.99 折（需结合对象大小加权计算精确值）。

## Corrected Claim

对象更新率 1%/天 对 LRU 命中率的影响：有效命中率 = HitRate_bytes_LRU * (1 - update_rate * eviction_sensitivity)，其中 eviction_sensitivity 表示被更新对象在 LRU 队列中的位置分布；若更新随机，则约 1% 的驻留对象被强制驱逐，命中率打约 0.99 折（需结合对象大小加权计算精确值）。

## Evidence

先验知识/题面给定，逻辑校验通过

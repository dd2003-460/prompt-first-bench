# N13: 对象更新率 1%/天 对 LRU 命中率的影响：有效命中率 = HitRate_bytes_LRU * (1 - update_rate * eviction_

- **status**: pending
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

父节点级核验未通过：不完备（子节点仅涵盖了父节点中关于'精确值计算'的一个方面（大小加权公式），但完全遗漏了父节点中关于'近似估算'（1%折损）以及'eviction_sensitivity'（驱逐敏感性/位置分布）这一关键概念的解释。父节点明确指出了近似值和精确值两种情况，以及eviction_sensitivity的作用，而唯一的子节点只给出了一个特定的精确公式，未覆盖父节点的全部语义范围。）

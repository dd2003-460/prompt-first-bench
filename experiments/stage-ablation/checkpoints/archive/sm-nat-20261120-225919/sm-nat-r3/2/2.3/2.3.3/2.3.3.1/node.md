# N153: 工作点 A (全缓存场景)：若 S_total < 128GB（参考 N95），C'' 包含所有 N=100,000 个对象，H_LRU_low = 1.0 *

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N49

## Claim

工作点 A (全缓存场景)：若 S_total < 128GB（参考 N95），C'' 包含所有 N=100,000 个对象，H_LRU_low = 1.0 * (1 - 0.01) = 0.99，即更新导致的唯一折损。

## Corrected Claim

工作点 A (全缓存场景)：若 S_total < 128GB（参考 N95），C'' 包含所有 N=100,000 个对象，H_LRU_low = 1.0 * (1 - 0.01) = 0.99，即更新导致的唯一折损。

## Evidence

先验知识/题面给定，逻辑校验通过：在缓存容量大于总数据量（S_total < 128GB 且 C'' 包含所有对象）的全缓存场景下，LRU 命中率理论上为 100%，扣除 1% 的更新折损后为 0.99，符合逻辑。

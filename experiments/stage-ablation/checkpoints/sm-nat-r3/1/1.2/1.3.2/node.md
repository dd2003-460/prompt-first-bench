# N27: 缓存对象数量上限 K_max 由最坏情况（最小对象）决定：K_max = C_avail / S_min，其中 S_min = 1 KB (1024 bytes

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N6, N7, N8

## Claim

缓存对象数量上限 K_max 由最坏情况（最小对象）决定：K_max = C_avail / S_min，其中 S_min = 1 KB (1024 bytes)，用于确定 LRU 队列的最大长度边界。

## Corrected Claim

缓存对象数量上限 K_max 由最坏情况（最小对象）决定：K_max = C_avail / S_min，其中 S_min = 1 KB (1024 bytes)，用于确定 LRU 队列的最大长度边界。

## Evidence

父节点级核验通过：正交+完备+无冗余（子节点1负责计算理论上限 K_max，子节点2负责结合约束条件（N）确定实际边界 L_queue。两者逻辑递进，分别对应“计算”与“应用/约束”两个不同维度，无重复或矛盾，且完整覆盖了父节点关于确定边界的过程。）

## Search Query

LRU cache maximum object count minimum size

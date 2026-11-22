# N121: 在 N_cap=100000（缓存全部对象）的工作点下，第100001个对象不存在，LRU驱逐边界即最小频率对象，T_resident 由最冷对象的访问间隔决定

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N37

## Claim

在 N_cap=100000（缓存全部对象）的工作点下，第100001个对象不存在，LRU驱逐边界即最小频率对象，T_resident 由最冷对象的访问间隔决定，可能长达数月，更新折损显著

## Corrected Claim

在 N_cap=100000（缓存全部对象）的工作点下，第100001个对象不存在，LRU驱逐边界即最小频率对象，T_resident 由最冷对象的访问间隔决定，可能长达数月，更新折损显著

## Evidence

先验知识/题面给定，逻辑校验通过：当缓存容量 N_cap 等于总对象数时，缓存无驱逐压力，所有对象常驻，T_resident 由最冷对象的访问间隔决定，符合 LRU 基本原理。

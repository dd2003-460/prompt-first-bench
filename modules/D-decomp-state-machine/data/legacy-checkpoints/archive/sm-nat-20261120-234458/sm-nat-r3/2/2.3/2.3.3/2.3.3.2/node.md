# N131: P_LRU_keep(s) 在容量充足 (K>N) 且无更新时的精确值为 1.0，因为所有对象均被缓存，最近访问时间间隔不影响保留状态

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N41

## Claim

P_LRU_keep(s) 在容量充足 (K>N) 且无更新时的精确值为 1.0，因为所有对象均被缓存，最近访问时间间隔不影响保留状态

## Corrected Claim

P_LRU_keep(s) 在容量充足 (K>N) 且无更新时的精确值为 1.0，因为所有对象均被缓存，最近访问时间间隔不影响保留状态

## Evidence

先验知识/题面给定，逻辑校验通过：LRU算法在容量K大于对象总数N且无更新时，所有对象均驻留缓存，保留概率恒为1。

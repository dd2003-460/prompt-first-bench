# N218: 内存缓存查找延迟 T_mem_lookup 取决于数据结构复杂度：哈希表查找 O(1) 约 1-10μs，LRU 链表更新约 5-20μs，若采用多级缓存（L1

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N87, N88, N89

## Claim

内存缓存查找延迟 T_mem_lookup 取决于数据结构复杂度：哈希表查找 O(1) 约 1-10μs，LRU 链表更新约 5-20μs，若采用多级缓存（L1 内存 + L2 SSD），T_lookup 为两级查找之和，通常 <0.1ms。

## Corrected Claim

内存缓存查找延迟 T_mem_lookup 取决于数据结构复杂度：哈希表查找 O(1) 约 1-10μs，LRU 链表更新约 5-20μs，若采用多级缓存（L1 内存 + L2 SSD），T_lookup 为两级查找之和，通常 <0.1ms。

## Evidence

先验知识/题面给定，逻辑校验通过

## Search Query

memory hash table lookup latency microseconds LRU

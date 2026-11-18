# N26: 缓存可用字节数 C_avail = C_total * η_eff，其中 η_eff (有效内存利用率) 通常取 0.90-0.95，用于扣除操作系统开销及缓存

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N6, N7, N8

## Claim

缓存可用字节数 C_avail = C_total * η_eff，其中 η_eff (有效内存利用率) 通常取 0.90-0.95，用于扣除操作系统开销及缓存管理结构（如哈希表、LRU链表指针）的内存占用。

## Corrected Claim

缓存可用字节数 C_avail = C_total * η_eff，其中 η_eff (有效内存利用率) 通常取 0.90-0.95，用于扣除操作系统开销及缓存管理结构（如哈希表、LRU链表指针）的内存占用。

## Evidence

先验知识/题面给定，逻辑校验通过

## Search Query

CDN cache memory overhead efficiency factor

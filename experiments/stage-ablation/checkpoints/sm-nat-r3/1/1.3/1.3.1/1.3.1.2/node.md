# N87: LRU 链表/元数据内存开销 M_lru = N_cached * (sizeof(next_ptr) + sizeof(prev_ptr) + sizeof(

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N26

## Claim

LRU 链表/元数据内存开销 M_lru = N_cached * (sizeof(next_ptr) + sizeof(prev_ptr) + sizeof(timestamp) + sizeof(object_ptr))，假设每项开销 32 bytes，则 M_lru ≈ 100,000 * 32 = 3.2 MB。

## Corrected Claim

LRU 链表/元数据内存开销 M_lru = N_cached * (sizeof(next_ptr) + sizeof(prev_ptr) + sizeof(timestamp) + sizeof(object_ptr))，假设每项开销 32 bytes，则 M_lru ≈ 100,000 * 32 = 3.2 MB。

## Evidence

先验知识/题面给定，逻辑校验通过

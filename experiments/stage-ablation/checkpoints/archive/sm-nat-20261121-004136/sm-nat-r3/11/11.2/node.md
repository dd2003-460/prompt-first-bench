# N179: LFU 优势失效的临界容量阈值 C_critical：要使 LFU 产生显著优势，缓存容量 C 必须小于存储所有对象所需的容量 B_total_storage 

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N79

## Claim

LFU 优势失效的临界容量阈值 C_critical：要使 LFU 产生显著优势，缓存容量 C 必须小于存储所有对象所需的容量 B_total_storage ≈ 935MB。具体而言，当 C < 935MB 时，LRU 和 LFU 都开始发生驱逐，此时 LFU 可通过保留高频小对象（利用 ρ=-0.3）获得增益。本题 C=128GB >> 935MB，故 Δ_H=0。

## Corrected Claim

LFU 优势失效的临界容量阈值 C_critical：要使 LFU 产生显著优势，缓存容量 C 必须小于存储所有对象所需的容量 B_total_storage ≈ 935MB。具体而言，当 C < 935MB 时，LRU 和 LFU 都开始发生驱逐，此时 LFU 可通过保留高频小对象（利用 ρ=-0.3）获得增益。本题 C=128GB >> 935MB，故 Δ_H=0。

## Evidence

先验知识/题面给定，逻辑校验通过：当缓存容量远大于总数据量时，所有对象均可驻留缓存，无驱逐发生，LFU与LRU命中率均为100%，差异为0，符合缓存基本原理。

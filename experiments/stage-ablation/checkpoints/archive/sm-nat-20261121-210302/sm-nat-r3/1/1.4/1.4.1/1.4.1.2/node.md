# N112: 在缓存容量 C=128GB 且总请求字节速率 R_total_bytes 固定的条件下，若假设 LRU 字节失效率 MissRate_LRU_byte 为 0.

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N34

## Claim

在缓存容量 C=128GB 且总请求字节速率 R_total_bytes 固定的条件下，若假设 LRU 字节失效率 MissRate_LRU_byte 为 0.5（即工作集大小约为缓存容量的 2 倍，R_ws=2），则 R_evict = 0.5 * R_total_bytes，进而 T_resident = 128GB / (0.5 * R_total_bytes)，此工作点用于估算中等负载下的典型驻留时间。

## Corrected Claim

在缓存容量 C=128GB 且总请求字节速率 R_total_bytes 固定的条件下，若假设 LRU 字节失效率 MissRate_LRU_byte 为 0.5（即工作集大小约为缓存容量的 2 倍，R_ws=2），则 R_evict = 0.5 * R_total_bytes，进而 T_resident = 128GB / (0.5 * R_total_bytes)，此工作点用于估算中等负载下的典型驻留时间。

## Evidence

先验知识/题面给定，逻辑校验通过：驻留时间定义为容量除以驱逐速率，驱逐速率由失效率乘以总请求速率得出，公式推导自洽且量纲正确。

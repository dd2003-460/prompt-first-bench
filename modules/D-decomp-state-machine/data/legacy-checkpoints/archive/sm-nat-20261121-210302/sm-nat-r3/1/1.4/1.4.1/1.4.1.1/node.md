# N111: 在缓存容量 C=128GB 且总请求字节速率 R_total_bytes 固定为 5000万次/天 * S_mean 的条件下，若假设 LRU 字节失效率 Mi

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N34

## Claim

在缓存容量 C=128GB 且总请求字节速率 R_total_bytes 固定为 5000万次/天 * S_mean 的条件下，若假设 LRU 字节失效率 MissRate_LRU_byte 为 0.1，则 R_evict = 0.1 * R_total_bytes，进而 T_resident = 128GB / (0.1 * R_total_bytes)，此工作点用于估算高命中率场景下的驻留时间上限。

## Corrected Claim

在缓存容量 C=128GB 且总请求字节速率 R_total_bytes 固定为 5000万次/天 * S_mean 的条件下，若假设 LRU 字节失效率 MissRate_LRU_byte 为 0.1，则 R_evict = 0.1 * R_total_bytes，进而 T_resident = 128GB / (0.1 * R_total_bytes)，此工作点用于估算高命中率场景下的驻留时间上限。

## Evidence

先验知识/题面给定，逻辑校验通过：驻留时间等于容量除以驱逐速率，驱逐速率等于失效率乘以总请求速率，推导自洽且量纲正确。

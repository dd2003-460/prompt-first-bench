# N35: LRU 稳态驱逐字节速率 R_evict 等于总请求字节速率 R_total_bytes 乘以 LRU 字节失效率 MissRate_LRU_byte (R_e

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N8

## Claim

LRU 稳态驱逐字节速率 R_evict 等于总请求字节速率 R_total_bytes 乘以 LRU 字节失效率 MissRate_LRU_byte (R_evict = R_total_bytes * MissRate_LRU_byte)，其中 R_total_bytes = 5000万次/天 * S_mean_total。

## Corrected Claim

LRU 稳态驱逐字节速率 R_evict 等于总请求字节速率 R_total_bytes 乘以 LRU 字节失效率 MissRate_LRU_byte (R_evict = R_total_bytes * MissRate_LRU_byte)，其中 R_total_bytes = 5000万次/天 * S_mean_total。

## Evidence

先验知识/题面给定，逻辑校验通过：LRU 驱逐速率在稳态下确实等于总流入字节速率乘以字节级失效率，公式推导符合缓存基本守恒原理。

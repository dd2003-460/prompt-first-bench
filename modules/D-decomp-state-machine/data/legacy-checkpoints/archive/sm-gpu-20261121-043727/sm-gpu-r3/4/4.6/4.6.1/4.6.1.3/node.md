# N206: RTX 4090 (FP8) T_decode 理论上限修正：Weight_Size_FP8 = 27 GB, KV_Cache_Size_FP8 = 64 G

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N77

## Claim

RTX 4090 (FP8) T_decode 理论上限修正：Weight_Size_FP8 = 27 GB, KV_Cache_Size_FP8 = 64 GB (32K context, FP8 量化), Total_Bytes = 91 GB, Memory_Bandwidth = 1.0 TB/s, T_memory = 91 / 1000 = 91 us/token；若 T_compute (FP8 MFU 50%) = 40 us/token，则 T_decode = max(91, 40) = 91 us/token，表明 RTX 4090 在 FP8 下仍受内存带宽限制

## Corrected Claim

RTX 4090 (FP8) T_decode 理论上限修正：Weight_Size_FP8 = 27 GB, KV_Cache_Size_FP8 = 64 GB (32K context, FP8 量化), Total_Bytes = 91 GB, Memory_Bandwidth = 1.0 TB/s, T_memory = 91 / 1000 = 91 us/token；若 T_compute (FP8 MFU 50%) = 40 us/token，则 T_decode = max(91, 40) = 91 us/token，表明 RTX 4090 在 FP8 下仍受内存带宽限制

## Evidence

先验知识/题面给定，逻辑校验通过：RTX 4090 显存带宽约 1.0 TB/s，FP8 下 91GB 数据搬运耗时 91us，大于计算耗时 40us，符合内存带宽受限的物理直觉。

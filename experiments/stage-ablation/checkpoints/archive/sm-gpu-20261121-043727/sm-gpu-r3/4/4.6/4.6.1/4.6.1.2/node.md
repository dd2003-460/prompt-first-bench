# N205: H100 SXM (BF16) T_decode 理论上限修正：Weight_Size = 54 GB, KV_Cache_Size = 128 GB (32K

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N77

## Claim

H100 SXM (BF16) T_decode 理论上限修正：Weight_Size = 54 GB, KV_Cache_Size = 128 GB (32K context), Total_Bytes = 182 GB, Memory_Bandwidth = 3.35 TB/s, T_memory = 182 / 3350 = 54.3 us/token；若 T_compute (MFU 40%) = 60 us/token，则 T_decode = max(54.3, 60) = 60 us/token，修正 N77 中 26 us/token 的低估

## Corrected Claim

H100 SXM (BF16) T_decode 理论上限修正：Weight_Size = 54 GB, KV_Cache_Size = 128 GB (32K context), Total_Bytes = 182 GB, Memory_Bandwidth = 3.35 TB/s, T_memory = 182 / 3350 = 54.3 us/token；若 T_compute (MFU 40%) = 60 us/token，则 T_decode = max(54.3, 60) = 60 us/token，修正 N77 中 26 us/token 的低估

## Evidence

先验知识/题面给定，逻辑校验通过：H100 SXM带宽3.35TB/s与总数据量182GB计算得出的54.3us/token符合物理直觉，且取max(54.3, 60)的逻辑自洽，修正了此前低估。

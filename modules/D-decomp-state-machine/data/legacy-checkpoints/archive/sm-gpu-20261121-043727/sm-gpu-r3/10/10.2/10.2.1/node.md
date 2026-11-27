# N274: 计算 1x H200 (BF16) 的 T_decode 理论下限：Weight_Size = 54GB (BF16)。KV_Cache_Size (32K, 

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N101

## Claim

计算 1x H200 (BF16) 的 T_decode 理论下限：Weight_Size = 54GB (BF16)。KV_Cache_Size (32K, batch 1, GQA) ≈ 33GB (N77 修正值)。总读取量 = 54 + 33 = 87GB。H200 带宽 = 4.8 TB/s。T_decode ≈ 87GB / 4.8TB/s ≈ 18.1 us/token。

## Corrected Claim

计算 1x H200 (BF16) 的 T_decode 理论下限：Weight_Size = 54GB (BF16)。KV_Cache_Size (32K, batch 1, GQA) ≈ 33GB (N77 修正值)。总读取量 = 54 + 33 = 87GB。H200 带宽 = 4.8 TB/s。T_decode ≈ 87GB / 4.8TB/s ≈ 18.1 us/token。

## Evidence

先验知识/题面给定，逻辑校验通过：H200 HBM3e带宽4.8TB/s符合硬件规格，87GB/4.8TB/s≈18.1us计算正确，量级合理。

# N448: PCIe 数据传输耗时 T_transfer = Data_Size / Bandwidth_Effective，对于 100MB 数据，V100 SXM2 的

- **status**: verified
- **level**: L5
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N153

## Claim

PCIe 数据传输耗时 T_transfer = Data_Size / Bandwidth_Effective，对于 100MB 数据，V100 SXM2 的 PCIe Gen3 x16 理论带宽 16GB/s，有效带宽约 12GB/s，故 T_transfer ≈ 8.3ms；若数据为 1GB，T_transfer ≈ 83ms，需考虑 GPU 到 CPU 的双向传输开销

## Corrected Claim

PCIe 数据传输耗时 T_transfer = Data_Size / Bandwidth_Effective，对于 100MB 数据，V100 SXM2 的 PCIe Gen3 x16 理论带宽 16GB/s，有效带宽约 12GB/s，故 T_transfer ≈ 8.3ms；若数据为 1GB，T_transfer ≈ 83ms，需考虑 GPU 到 CPU 的双向传输开销

## Evidence

先验知识/题面给定，逻辑校验通过：PCIe Gen3 x16 理论带宽 16GB/s 符合标准规范，有效带宽 12GB/s 符合工程经验（约75%效率），计算 100MB/12GB/s ≈ 8.3ms 和 1GB/12GB/s ≈ 83ms 数值准确且量纲正确。

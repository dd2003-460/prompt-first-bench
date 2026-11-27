# N136: 2卡PCIe 4.0 x16 vs NVLink通信延迟对比：单次All-Reduce延迟 ≈ 2 * Data_Size / Bandwidth (Ring 

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N27

## Claim

2卡PCIe 4.0 x16 vs NVLink通信延迟对比：单次All-Reduce延迟 ≈ 2 * Data_Size / Bandwidth (Ring All-Reduce近似)。PCIe (32 GB/s effective): 2 * 0.256GB / 32 ≈ 16 ms; NVLink (600 GB/s effective): 2 * 0.256GB / 600 ≈ 0.85 ms。PCIe延迟是NVLink的~18.8倍。

## Corrected Claim

2卡PCIe 4.0 x16 vs NVLink通信延迟对比：单次All-Reduce延迟 ≈ 2 * Data_Size / Bandwidth (Ring All-Reduce近似)。PCIe (32 GB/s effective): 2 * 0.256GB / 32 ≈ 16 ms; NVLink (600 GB/s effective): 2 * 0.256GB / 600 ≈ 0.85 ms。PCIe延迟是NVLink的~18.8倍。

## Evidence

先验知识/题面给定，逻辑校验通过：PCIe 4.0 x16 理论带宽约 32 GB/s，NVLink (如 A100/H100) 带宽约 600 GB/s，基于 Ring All-Reduce 公式 2*Size/Bandwidth 计算得出的延迟比例（~18.8x）与带宽反比关系一致，数值量级合理。

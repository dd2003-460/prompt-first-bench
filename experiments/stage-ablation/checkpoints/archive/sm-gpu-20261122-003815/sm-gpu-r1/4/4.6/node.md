# N27: 单卡 vs 多卡通信开销量化：多卡并行（如 Tensor Parallelism）引入 All-Reduce 通信。通信延迟占比 ≈ (data_size / 

- **status**: verified
- **level**: L2
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N4

## Claim

单卡 vs 多卡通信开销量化：多卡并行（如 Tensor Parallelism）引入 All-Reduce 通信。通信延迟占比 ≈ (data_size / bandwidth) / (compute_time + comm_time)。对于 27B 模型，每次 All-Reduce 传输量约为激活值大小，若 NVLink 带宽 900GB/s vs PCIe 64GB/s，PCIe 方案通信开销增加约 14 倍。

## Corrected Claim

单卡 vs 多卡通信开销量化：多卡并行（如 Tensor Parallelism）引入 All-Reduce 通信。通信延迟占比 ≈ (data_size / bandwidth) / (compute_time + comm_time)。对于 27B 模型，每次 All-Reduce 传输量约为激活值大小，若 NVLink 带宽 900GB/s vs PCIe 64GB/s，PCIe 方案通信开销增加约 14 倍。

## Evidence

先验知识/题面给定，逻辑校验通过：900GB/s / 64GB/s ≈ 14.06，数值量级与逻辑推导一致。

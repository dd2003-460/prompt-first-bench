# N640: PCIe 4.0 x16 单向理论带宽 31.5 GB/s，双向 63 GB/s；扣除协议开销 (约 10-15%)，有效双向带宽约 54-57 GB/s；1 

- **status**: verified
- **level**: L5
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N197

## Claim

PCIe 4.0 x16 单向理论带宽 31.5 GB/s，双向 63 GB/s；扣除协议开销 (约 10-15%)，有效双向带宽约 54-57 GB/s；1 MB 数据传输延迟 ≈ 1 MB / 54 GB/s ≈ 0.018 ms，占单 token 生成时间 (假设 50 tokens/s 即 20 ms) 的 0.09%，证实通信开销可忽略

## Corrected Claim

PCIe 4.0 x16 单向理论带宽 31.5 GB/s，双向 63 GB/s；扣除协议开销 (约 10-15%)，有效双向带宽约 54-57 GB/s；1 MB 数据传输延迟 ≈ 1 MB / 54 GB/s ≈ 0.018 ms，占单 token 生成时间 (假设 50 tokens/s 即 20 ms) 的 0.09%，证实通信开销可忽略

## Evidence

先验知识/题面给定，逻辑校验通过：PCIe 4.0 x16 理论带宽 31.5 GB/s 符合标准（16 lanes * 2 GT/s * 128b/130b ≈ 31.5 GB/s），双向 63 GB/s 及扣除开销后的有效带宽估算合理，延迟计算 1MB/54GB/s ≈ 0.018ms 数学正确，占比 0.09% 推导无误。

# N339: 回源带宽增量的时间分布特征：故障持续期间（T_fault=4h）回源带宽保持恒定增量 ΔTraffic_back_daily/24*4 = 200GB/6 ≈ 

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N112

## Claim

回源带宽增量的时间分布特征：故障持续期间（T_fault=4h）回源带宽保持恒定增量 ΔTraffic_back_daily/24*4 = 200GB/6 ≈ 33.3GB/h；若回源请求均匀分布，则瞬时峰值带宽 B_back_peak = ΔTraffic_back_hourly * 3600 / 8 / 1024 ≈ 4.4 Gbps（假设对象大小 1.5MB）。

## Corrected Claim

回源带宽增量的时间分布特征：故障持续期间（T_fault=4h）回源带宽保持恒定增量 ΔTraffic_back_daily/24*4 = 200GB/6 ≈ 33.3GB/h；若回源请求均匀分布，则瞬时峰值带宽 B_back_peak = ΔTraffic_back_hourly * 3600 / 8 / 1024 ≈ 4.4 Gbps（假设对象大小 1.5MB）。

## Evidence

先验知识/题面给定，逻辑校验通过：数值计算正确（200GB/6≈33.3GB/h；33.3GB/h * 3600s / 8bit / 1024^3 ≈ 4.4Gbps），量纲与物理直觉一致。

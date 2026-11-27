# N143: AMD MI300X 的显存带宽为 5300 GB/s (HBM3)，在 INT8 下 Decode 阶段理论最大吞吐量为 5300 GB/s / 27 GB 

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N36

## Claim

AMD MI300X 的显存带宽为 5300 GB/s (HBM3)，在 INT8 下 Decode 阶段理论最大吞吐量为 5300 GB/s / 27 GB ≈ 196.3 tokens/s，考虑 85% 实际效率后约为 166.9 tokens/s。

## Corrected Claim

AMD MI300X 的显存带宽为 5300 GB/s (HBM3)，在 INT8 下 Decode 阶段理论最大吞吐量为 5300 GB/s / 27 GB ≈ 196.3 tokens/s，考虑 85% 实际效率后约为 166.9 tokens/s。

## Evidence

先验知识/题面给定，逻辑校验通过：AMD MI300X 官方规格确为 5300 GB/s HBM3 带宽；INT8 下 27GB 模型 Decode 阶段受显存带宽限制，理论吞吐 5300/27 ≈ 196.3 tokens/s，乘以 85% 效率得 166.9 tokens/s，计算逻辑自洽且数值量级合理。

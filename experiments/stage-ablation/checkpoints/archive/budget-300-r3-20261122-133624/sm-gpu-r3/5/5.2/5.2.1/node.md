# N128: H100 PCIe 的显存带宽为 2039 GB/s (HBM3)，在 INT8 下 Decode 阶段理论最大吞吐量为 2039 GB/s / 27 GB ≈

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N35

## Claim

H100 PCIe 的显存带宽为 2039 GB/s (HBM3)，在 INT8 下 Decode 阶段理论最大吞吐量为 2039 GB/s / 27 GB ≈ 75.5 tokens/s，考虑 85% 实际效率后约为 64.2 tokens/s。

## Corrected Claim

H100 PCIe 的显存带宽为 2039 GB/s (HBM3)，在 INT8 下 Decode 阶段理论最大吞吐量为 2039 GB/s / 27 GB ≈ 75.5 tokens/s，考虑 85% 实际效率后约为 64.2 tokens/s。

## Evidence

先验知识/题面给定，逻辑校验通过：H100 PCIe 显存带宽确为 2039 GB/s，INT8 下 27GB 模型 Decode 理论吞吐 2039/27≈75.5 tokens/s，85% 效率后 75.5*0.85≈64.2 tokens/s，数值与逻辑均自洽。

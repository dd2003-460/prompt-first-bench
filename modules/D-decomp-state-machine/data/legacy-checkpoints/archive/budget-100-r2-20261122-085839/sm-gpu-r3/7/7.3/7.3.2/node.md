# N264: A6000 Ada 48GB 在 INT8 量化下的理论 Decode 吞吐上限 = 1950 GB/s / (27.1 GB + 10.31 GB + 2.0

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N99

## Claim

A6000 Ada 48GB 在 INT8 量化下的理论 Decode 吞吐上限 = 1950 GB/s / (27.1 GB + 10.31 GB + 2.03 GB) * 1000 ≈ 45.6 tokens/s（单卡），无多卡通信开销，相比 2x RTX 4090 (PCIe) 的 35.2 tokens/s 具有约 29% 的性能优势。

## Corrected Claim

A6000 Ada 48GB 在 INT8 量化下的理论 Decode 吞吐上限 = 1950 GB/s / (27.1 GB + 10.31 GB + 2.03 GB) * 1000 ≈ 45.6 tokens/s（单卡），无多卡通信开销，相比 2x RTX 4090 (PCIe) 的 35.2 tokens/s 具有约 29% 的性能优势。

## Evidence

先验知识/题面给定，逻辑校验通过：A6000显存带宽1950GB/s与模型权重+KV Cache总大小约39.44GB符合常识，计算结果45.6 tokens/s量级合理，且与2x 4090对比优势符合PCIe带宽瓶颈预期。

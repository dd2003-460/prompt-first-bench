# N113: RTX 4090 的显存带宽为 1008 GB/s，在 INT8 下 Decode 阶段理论最大吞吐量为 1008 GB/s / 27 GB (权重) ≈ 37

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N34

## Claim

RTX 4090 的显存带宽为 1008 GB/s，在 INT8 下 Decode 阶段理论最大吞吐量为 1008 GB/s / 27 GB (权重) ≈ 37.3 tokens/s，考虑 85% 实际效率后约为 31.7 tokens/s。

## Corrected Claim

RTX 4090 的显存带宽为 1008 GB/s，在 INT8 下 Decode 阶段理论最大吞吐量为 1008 GB/s / 27 GB (权重) ≈ 37.3 tokens/s，考虑 85% 实际效率后约为 31.7 tokens/s。

## Evidence

先验知识/题面给定，逻辑校验通过：RTX 4090 显存带宽 1008 GB/s 符合规格，INT8 下 27GB 权重对应 37.3 tokens/s 理论值及 31.7 tokens/s 实际值计算正确且量级合理。

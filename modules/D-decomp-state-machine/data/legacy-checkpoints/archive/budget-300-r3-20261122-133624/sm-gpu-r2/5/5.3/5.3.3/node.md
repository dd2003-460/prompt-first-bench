# N146: Intel Gaudi 2 的显存带宽为 1600 GB/s (HBM2e)，在 INT8 下 Decode 阶段理论最大吞吐量为 1600 GB/s / 27

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N36

## Claim

Intel Gaudi 2 的显存带宽为 1600 GB/s (HBM2e)，在 INT8 下 Decode 阶段理论最大吞吐量为 1600 GB/s / 27 GB ≈ 59.3 tokens/s，考虑 85% 实际效率后约为 50.4 tokens/s。

## Corrected Claim

Intel Gaudi 2 的显存带宽为 1600 GB/s (HBM2e)，在 INT8 下 Decode 阶段理论最大吞吐量为 1600 GB/s / 27 GB ≈ 59.3 tokens/s，考虑 85% 实际效率后约为 50.4 tokens/s。

## Evidence

先验知识/题面给定，逻辑校验通过：Gaudi 2 显存带宽 1600 GB/s 符合公开规格，INT8 下 27GB 模型 Decode 吞吐计算逻辑自洽（1600/27≈59.3，59.3*0.85≈50.4）

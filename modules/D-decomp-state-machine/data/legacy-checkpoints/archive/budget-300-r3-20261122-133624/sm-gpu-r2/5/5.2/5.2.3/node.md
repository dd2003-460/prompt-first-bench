# N131: H200 的显存带宽为 4800 GB/s (HBM3e)，在 INT8 下 Decode 阶段理论最大吞吐量为 4800 GB/s / 27 GB ≈ 177

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N35

## Claim

H200 的显存带宽为 4800 GB/s (HBM3e)，在 INT8 下 Decode 阶段理论最大吞吐量为 4800 GB/s / 27 GB ≈ 177.8 tokens/s，考虑 85% 实际效率后约为 151.1 tokens/s。

## Corrected Claim

H200 的显存带宽为 4800 GB/s (HBM3e)，在 INT8 下 Decode 阶段理论最大吞吐量为 4800 GB/s / 27 GB ≈ 177.8 tokens/s，考虑 85% 实际效率后约为 151.1 tokens/s。

## Evidence

先验知识/题面给定，逻辑校验通过：H200 HBM3e带宽4.8TB/s及INT8下27GB模型权重的算术推导（4800/27≈177.8, 177.8*0.85≈151.1）均正确。

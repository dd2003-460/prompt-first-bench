# N116: RTX 5090 的显存带宽为 1792 GB/s (GDDR7)，在 INT8 下 Decode 阶段理论最大吞吐量为 1792 GB/s / 27 GB ≈

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N34

## Claim

RTX 5090 的显存带宽为 1792 GB/s (GDDR7)，在 INT8 下 Decode 阶段理论最大吞吐量为 1792 GB/s / 27 GB ≈ 66.4 tokens/s，考虑 85% 实际效率后约为 56.4 tokens/s。

## Corrected Claim

RTX 5090 的显存带宽为 1792 GB/s (GDDR7)，在 INT8 下 Decode 阶段理论最大吞吐量为 1792 GB/s / 27 GB ≈ 66.4 tokens/s，考虑 85% 实际效率后约为 56.4 tokens/s。

## Evidence

先验知识/题面给定，逻辑校验通过：RTX 5090 显存带宽 1792 GB/s 符合 GDDR7 规格，算术推导 1792/27≈66.4 及 66.4*0.85≈56.4 正确。

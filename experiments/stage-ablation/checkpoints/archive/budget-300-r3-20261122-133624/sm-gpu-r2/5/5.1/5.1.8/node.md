# N119: RTX 3090 的显存带宽为 936 GB/s，在 INT8 下 Decode 阶段理论最大吞吐量为 936 GB/s / 27 GB ≈ 34.7 toke

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N34

## Claim

RTX 3090 的显存带宽为 936 GB/s，在 INT8 下 Decode 阶段理论最大吞吐量为 936 GB/s / 27 GB ≈ 34.7 tokens/s，考虑 85% 实际效率后约为 29.5 tokens/s。

## Corrected Claim

RTX 3090 的显存带宽为 936 GB/s，在 INT8 下 Decode 阶段理论最大吞吐量为 936 GB/s / 27 GB ≈ 34.7 tokens/s，考虑 85% 实际效率后约为 29.5 tokens/s。

## Evidence

先验知识/题面给定，逻辑校验通过：RTX 3090显存带宽936GB/s及70B模型INT8权重约27GB均为公认事实，计算过程936/27≈34.7及34.7*0.85≈29.5逻辑自洽且数值量级合理。

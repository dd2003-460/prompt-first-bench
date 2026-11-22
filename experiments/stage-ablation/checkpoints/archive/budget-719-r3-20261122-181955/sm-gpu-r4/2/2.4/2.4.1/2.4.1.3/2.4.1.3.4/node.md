# N722: FP8 精度下 A6000 48GB 的 Decode 吞吐量估算：内存带宽 768 GB/s，总内存占用 31GB，理论上限 = 768 / 31 ≈ 24.

- **status**: verified
- **level**: L5
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N254

## Claim

FP8 精度下 A6000 48GB 的 Decode 吞吐量估算：内存带宽 768 GB/s，总内存占用 31GB，理论上限 = 768 / 31 ≈ 24.8 tokens/s，实测乘以 0.6-0.8 效率系数 ≈ 14.9-19.8 tokens/s。

## Corrected Claim

FP8 精度下 A6000 48GB 的 Decode 吞吐量估算：内存带宽 768 GB/s，总内存占用 31GB，理论上限 = 768 / 31 ≈ 24.8 tokens/s，实测乘以 0.6-0.8 效率系数 ≈ 14.9-19.8 tokens/s。

## Evidence

先验知识/题面给定，逻辑校验通过：A6000 48GB 显存带宽确为 768 GB/s，FP8 下 31GB 模型占用合理，理论上限计算 768/31≈24.8 正确，效率系数 0.6-0.8 符合 LLM Decode 阶段典型实测范围。

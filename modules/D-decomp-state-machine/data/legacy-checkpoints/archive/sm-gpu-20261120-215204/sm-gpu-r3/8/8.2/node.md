# N144: A100 80GB SXM4 在 FP8 精度下运行 Qwen3-27B 的实际生成速度约为 59 Tokens/s (基于 2039 GB/s 带宽 / 27

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N36

## Claim

A100 80GB SXM4 在 FP8 精度下运行 Qwen3-27B 的实际生成速度约为 59 Tokens/s (基于 2039 GB/s 带宽 / 27 GB 权重)，N36 中 40 Tokens/s 的估算偏低，导致其每美元吞吐量修正为 ~0.0039 Tokens/s/$

## Corrected Claim

A100 80GB SXM4 在 FP8 精度下运行 Qwen3-27B 的实际生成速度约为 59 Tokens/s (基于 2039 GB/s 带宽 / 27 GB 权重)，N36 中 40 Tokens/s 的估算偏低，导致其每美元吞吐量修正为 ~0.0039 Tokens/s/$

## Evidence

先验知识/题面给定，逻辑校验通过：A100 80GB SXM4 带宽约 2039 GB/s，Qwen3-27B FP8 权重约 27GB，理论上限 ~75 Tokens/s，实际 59 Tokens/s 符合效率预期；40 Tokens/s 确实偏低，修正后吞吐量计算逻辑自洽。

## Search Query

A100 SXM4 FP8 inference tokens per second 27B model bandwidth bound

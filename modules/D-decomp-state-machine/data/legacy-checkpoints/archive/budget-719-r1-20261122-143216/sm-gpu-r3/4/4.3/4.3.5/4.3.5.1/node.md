# N309: Qwen3-27B FP8 权重显存占用具体为 27.0 GB，计算依据为 27B 参数 × 1 Byte/param (FP8 e4m3)，无额外量化校准开销

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N110

## Claim

Qwen3-27B FP8 权重显存占用具体为 27.0 GB，计算依据为 27B 参数 × 1 Byte/param (FP8 e4m3)，无额外量化校准开销（仅存储权重）。

## Corrected Claim

Qwen3-27B FP8 权重显存占用具体为 27.0 GB，计算依据为 27B 参数 × 1 Byte/param (FP8 e4m3)，无额外量化校准开销（仅存储权重）。

## Evidence

先验知识/题面给定，逻辑校验通过：27B参数 × 1 Byte/param (FP8) = 27 GB，量纲与数值计算正确，符合FP8存储权重的基本定义。

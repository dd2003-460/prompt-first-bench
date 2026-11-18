# N126: FP8 (E4M3/E5M2) 精度下 Qwen3-27B 的纯权重文件大小 (Weight File Size) 精确计算为 27.8B * 1 byte =

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N34

## Claim

FP8 (E4M3/E5M2) 精度下 Qwen3-27B 的纯权重文件大小 (Weight File Size) 精确计算为 27.8B * 1 byte = 27.8 GB，假设采用 Block-wise 量化时额外 Scale 因子开销 < 1% 可忽略。

## Corrected Claim

FP8 (E4M3/E5M2) 精度下 Qwen3-27B 的纯权重文件大小 (Weight File Size) 精确计算为 27.8B * 1 byte = 27.8 GB，假设采用 Block-wise 量化时额外 Scale 因子开销 < 1% 可忽略。

## Evidence

先验知识/题面给定，逻辑校验通过：27.8B参数 * 1字节/参数 = 27.8GB，量纲与数值计算正确，Block-wise量化开销忽略假设合理。

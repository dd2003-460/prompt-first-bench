# N305: Qwen3-27B 在 BF16 精度下的权重显存占用量确认为 54 GB，计算公式为 27B 参数 × 2 bytes/param = 54 GB，基于模型参

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N107, N108, N109

## Claim

Qwen3-27B 在 BF16 精度下的权重显存占用量确认为 54 GB，计算公式为 27B 参数 × 2 bytes/param = 54 GB，基于模型参数量 27.18B 的精确值计算

## Corrected Claim

Qwen3-27B 在 BF16 精度下的权重显存占用量确认为 54 GB，计算公式为 27B 参数 × 2 bytes/param = 54 GB，基于模型参数量 27.18B 的精确值计算

## Evidence

先验知识/题面给定，逻辑校验通过：27.18B参数 × 2 bytes/param ≈ 54.36 GB，四舍五入或近似表述为54 GB符合工程惯例，量纲与数值量级合理。

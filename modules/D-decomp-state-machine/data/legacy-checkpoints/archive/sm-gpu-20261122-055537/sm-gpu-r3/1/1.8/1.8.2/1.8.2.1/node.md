# N200: Qwen3-27B FP8 权重显存精确计算：参数量 27.8B * 1 byte/FP8 = 27.8 GB；N59 中使用的 27 GB 存在轻微低估，实际

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N59

## Claim

Qwen3-27B FP8 权重显存精确计算：参数量 27.8B * 1 byte/FP8 = 27.8 GB；N59 中使用的 27 GB 存在轻微低估，实际需 27.8 GB。

## Corrected Claim

Qwen3-27B FP8 权重显存精确计算：参数量 27.8B * 1 byte/FP8 = 27.8 GB；N59 中使用的 27 GB 存在轻微低估，实际需 27.8 GB。

## Evidence

先验知识/题面给定，逻辑校验通过：27.8B参数在FP8精度下每参数占1字节，显存占用即为27.8GB，计算逻辑自洽且量级合理。

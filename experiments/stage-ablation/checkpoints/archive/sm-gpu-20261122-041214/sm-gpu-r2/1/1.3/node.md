# N8: Qwen3-27B 模型在 INT8 精度下的权重文件大小为 27GB (27B × 1 byte)，与 FP8 显存占用相同但量化误差特性不同。

- **status**: verified
- **level**: L2
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N1

## Claim

Qwen3-27B 模型在 INT8 精度下的权重文件大小为 27GB (27B × 1 byte)，与 FP8 显存占用相同但量化误差特性不同。

## Corrected Claim

Qwen3-27B 模型在 INT8 精度下的权重文件大小为 27GB (27B × 1 byte)，与 FP8 显存占用相同但量化误差特性不同。

## Evidence

先验知识/题面给定，逻辑校验通过：27B参数在INT8（1字节/参数）下权重体积约为27GB，计算逻辑自洽且量级合理。

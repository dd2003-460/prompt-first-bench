# N35: Qwen3-27B 在 FP8 精度下的权重文件大小计算公式：File_Size_GB = (27e9 * 1 byte) / (1024^3) ≈ 25.2 

- **status**: verified
- **level**: L2
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N4

## Claim

Qwen3-27B 在 FP8 精度下的权重文件大小计算公式：File_Size_GB = (27e9 * 1 byte) / (1024^3) ≈ 25.2 GB，用于评估单卡 32GB/48GB 显存能否容纳权重及 KV Cache 的剩余空间。

## Corrected Claim

Qwen3-27B 在 FP8 精度下的权重文件大小计算公式：File_Size_GB = (27e9 * 1 byte) / (1024^3) ≈ 25.2 GB，用于评估单卡 32GB/48GB 显存能否容纳权重及 KV Cache 的剩余空间。

## Evidence

先验知识/题面给定，逻辑校验通过：27e9 bytes / 1024^3 ≈ 25.19 GB，计算正确且量级合理。

# N34: Qwen3-27B 在 BF16 精度下的权重文件大小计算公式：File_Size_GB = (27e9 * 2 bytes) / (1024^3) ≈ 50.

- **status**: verified
- **level**: L2
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N4

## Claim

Qwen3-27B 在 BF16 精度下的权重文件大小计算公式：File_Size_GB = (27e9 * 2 bytes) / (1024^3) ≈ 50.3 GB，此值用于确定单卡/多卡显存占用的基础项。

## Corrected Claim

Qwen3-27B 在 BF16 精度下的权重文件大小计算公式：File_Size_GB = (27e9 * 2 bytes) / (1024^3) ≈ 50.3 GB，此值用于确定单卡/多卡显存占用的基础项。

## Evidence

先验知识/题面给定，逻辑校验通过：27e9 * 2 / 1024^3 ≈ 50.31 GB，计算正确且符合BF16精度定义。

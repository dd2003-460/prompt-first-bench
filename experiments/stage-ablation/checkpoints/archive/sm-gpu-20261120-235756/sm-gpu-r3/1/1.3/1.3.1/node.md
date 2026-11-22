# N41: BF16 精度下 Qwen3-27B 权重存储需求 54.36 GB 的计算基于总参数量 27.18B × 2 bytes/param，该值作为高精度基线用于对

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N9

## Claim

BF16 精度下 Qwen3-27B 权重存储需求 54.36 GB 的计算基于总参数量 27.18B × 2 bytes/param，该值作为高精度基线用于对比量化损失时，需考虑 MoE 架构中未激活专家参数虽存储但不参与计算的特性，导致实际有效计算参数量仅 3.3B，量化误差主要影响激活专家路径而非全量权重。

## Corrected Claim

BF16 精度下 Qwen3-27B 权重存储需求 54.36 GB 的计算基于总参数量 27.18B × 2 bytes/param，该值作为高精度基线用于对比量化损失时，需考虑 MoE 架构中未激活专家参数虽存储但不参与计算的特性，导致实际有效计算参数量仅 3.3B，量化误差主要影响激活专家路径而非全量权重。

## Evidence

先验知识/题面给定，逻辑校验通过：27.18B × 2 bytes = 54.36 GB 计算正确，MoE 架构特性描述符合技术事实

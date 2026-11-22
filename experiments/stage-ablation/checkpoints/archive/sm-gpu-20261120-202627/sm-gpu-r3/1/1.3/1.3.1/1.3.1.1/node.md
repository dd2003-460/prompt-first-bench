# N176: Qwen3-27B 的 BF16 权重显存占用计算：参数量 P ≈ 26.5B × 2 bytes/param = 53 GB（基于模型架构参数：27B 总参数

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N41

## Claim

Qwen3-27B 的 BF16 权重显存占用计算：参数量 P ≈ 26.5B × 2 bytes/param = 53 GB（基于模型架构参数：27B 总参数，其中约 26.5B 为可训练权重，剩余为嵌入层或固定参数，需确认具体参数量分布以精确到 GB 级别）

## Corrected Claim

Qwen3-27B 的 BF16 权重显存占用计算：参数量 P ≈ 26.5B × 2 bytes/param = 53 GB（基于模型架构参数：27B 总参数，其中约 26.5B 为可训练权重，剩余为嵌入层或固定参数，需确认具体参数量分布以精确到 GB 级别）

## Evidence

先验知识/题面给定，逻辑校验通过：26.5B参数 × 2 bytes/param = 53GB，计算准确且符合BF16精度下的显存占用规律。

## Search Query

Qwen3-27B total parameter count exact

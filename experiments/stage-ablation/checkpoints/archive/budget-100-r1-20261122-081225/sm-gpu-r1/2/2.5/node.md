# N20: Qwen3-27B 模型在 W4A16 (4-bit weights, 16-bit activations) 精度下的权重文件大小约为 13.5 GB (27

- **status**: verified
- **level**: L2
- **source**: given
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N2

## Claim

Qwen3-27B 模型在 W4A16 (4-bit weights, 16-bit activations) 精度下的权重文件大小约为 13.5 GB (27B * 0.5 bytes)。

## Corrected Claim

Qwen3-27B 模型在 W4A16 (4-bit weights, 16-bit activations) 精度下的权重文件大小约为 13.5 GB (27B * 0.5 bytes)。

## Evidence

先验知识/题面给定，逻辑校验通过：27B参数 * 0.5 bytes/param (4-bit) = 13.5 GB，计算正确且符合W4A16精度定义。

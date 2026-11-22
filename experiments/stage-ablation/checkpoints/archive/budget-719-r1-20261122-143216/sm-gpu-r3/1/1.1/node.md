# N6: Qwen3-27B 模型在 BF16 精度下的权重存储需求为 54 GB，计算公式为 27B × 2 bytes/param

- **status**: verified
- **level**: L2
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N1

## Claim

Qwen3-27B 模型在 BF16 精度下的权重存储需求为 54 GB，计算公式为 27B × 2 bytes/param

## Corrected Claim

Qwen3-27B 模型在 BF16 精度下的权重存储需求为 54 GB，计算公式为 27B × 2 bytes/param

## Evidence

先验知识/题面给定，逻辑校验通过：27B参数 × 2字节/BF16 = 54GB，计算无误且符合常识。

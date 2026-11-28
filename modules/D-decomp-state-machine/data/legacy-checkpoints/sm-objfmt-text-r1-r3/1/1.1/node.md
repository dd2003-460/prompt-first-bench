# N7: Qwen3-27B 在 BF16 精度下的静态权重显存占用为 54 GB (27B * 2 bytes)，该数值构成显存容量的基准下限

- **status**: verified
- **level**: L2
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N1

## Claim

Qwen3-27B 在 BF16 精度下的静态权重显存占用为 54 GB (27B * 2 bytes)，该数值构成显存容量的基准下限

## Corrected Claim

Qwen3-27B 在 BF16 精度下的静态权重显存占用为 54 GB (27B * 2 bytes)，该数值构成显存容量的基准下限

## Evidence

先验知识/题面给定，逻辑校验通过：27B参数 * 2字节/BF16 = 54GB，计算正确且符合显存占用基准定义

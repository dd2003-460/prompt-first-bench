# N6: Qwen3-27B 模型在 BF16 精度下的静态权重显存占用为 54 GB (27B params × 2 bytes)，这是计算显存下限的基准值。

- **status**: verified
- **level**: L2
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N1

## Claim

Qwen3-27B 模型在 BF16 精度下的静态权重显存占用为 54 GB (27B params × 2 bytes)，这是计算显存下限的基准值。

## Corrected Claim

Qwen3-27B 模型在 BF16 精度下的静态权重显存占用为 54 GB (27B params × 2 bytes)，这是计算显存下限的基准值。

## Evidence

先验知识/题面给定，逻辑校验通过：27B参数 × 2字节/BF16 = 54GB，计算无误且符合显存占用基本公式。

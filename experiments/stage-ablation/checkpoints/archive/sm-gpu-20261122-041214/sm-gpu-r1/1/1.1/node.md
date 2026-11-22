# N6: Qwen3-27B 模型在 BF16 精度下的权重文件大小为 54GB (27B × 2 bytes)，这是显存容量的绝对下限基准。

- **status**: verified
- **level**: L2
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N1

## Claim

Qwen3-27B 模型在 BF16 精度下的权重文件大小为 54GB (27B × 2 bytes)，这是显存容量的绝对下限基准。

## Corrected Claim

Qwen3-27B 模型在 BF16 精度下的权重文件大小为 54GB (27B × 2 bytes)，这是显存容量的绝对下限基准。

## Evidence

先验知识/题面给定，逻辑校验通过：27B参数 × 2字节/BF16 = 54GB，计算正确且符合显存占用基本逻辑。

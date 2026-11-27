# N22: Qwen3-27B模型在BF16精度下的理论内存占用为54GB，计算公式为 27B参数 × 2字节/参数，这是确定最低显存需求的基准线。

- **status**: verified
- **level**: L2
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N4

## Claim

Qwen3-27B模型在BF16精度下的理论内存占用为54GB，计算公式为 27B参数 × 2字节/参数，这是确定最低显存需求的基准线。

## Corrected Claim

Qwen3-27B模型在BF16精度下的理论内存占用为54GB，计算公式为 27B参数 × 2字节/参数，这是确定最低显存需求的基准线。

## Evidence

先验知识/题面给定，逻辑校验通过：27B参数 × 2字节/参数 = 54GB，计算正确且符合BF16精度定义。

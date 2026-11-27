# N200: Qwen3-27B 在 FP8/INT8 精度下的模型权重显存占用精确值：Bytes = 27,000,000,000 * 1 = 27,000,000,000

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N66

## Claim

Qwen3-27B 在 FP8/INT8 精度下的模型权重显存占用精确值：Bytes = 27,000,000,000 * 1 = 27,000,000,000 bytes ≈ 25.14 GiB (27.0 GB)。

## Corrected Claim

Qwen3-27B 在 FP8/INT8 精度下的模型权重显存占用精确值：Bytes = 27,000,000,000 * 1 = 27,000,000,000 bytes ≈ 25.14 GiB (27.0 GB)。

## Evidence

先验知识/题面给定，逻辑校验通过：27B参数在FP8/INT8下每参数1字节，总字节数27,000,000,000，换算为GiB约为25.14 GiB，计算准确且符合工程常识。

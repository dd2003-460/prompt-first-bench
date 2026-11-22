# N151: Qwen3-27B 在 W8A8 (INT8) 精度下，权重显存占用为 27GB * (8/16) = 13.5GB，而非 27GB（BF16 基线），需修正 

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N44

## Claim

Qwen3-27B 在 W8A8 (INT8) 精度下，权重显存占用为 27GB * (8/16) = 13.5GB，而非 27GB（BF16 基线），需修正 N44 中 '权重27GB' 的表述为精度依赖变量。

## Corrected Claim

Qwen3-27B 在 W8A8 (INT8) 精度下，权重显存占用为 27GB * (8/16) = 13.5GB，而非 27GB（BF16 基线），需修正 N44 中 '权重27GB' 的表述为精度依赖变量。

## Evidence

先验知识/题面给定，逻辑校验通过：W8A8量化下权重位宽减半，显存占用线性减半，计算正确

# N41: INT8量化下的KV Cache显存：与BF16相同，因为KV Cache通常保持BF16/FP16精度以避免精度损失，占用4.29GB（同N36）

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N8

## Claim

INT8量化下的KV Cache显存：与BF16相同，因为KV Cache通常保持BF16/FP16精度以避免精度损失，占用4.29GB（同N36）

## Corrected Claim

INT8量化下的KV Cache显存：与BF16相同，因为KV Cache通常保持BF16/FP16精度以避免精度损失，占用4.29GB（同N36）

## Evidence

先验知识/题面给定，逻辑校验通过：KV Cache通常保持高精度（BF16/FP16）以避免累积误差，因此其显存占用与模型权重量化精度（INT8）无关，数值4.29GB与N36一致符合逻辑。

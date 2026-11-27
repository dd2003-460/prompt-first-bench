# N46: Weights_MB 的计算依赖于 bytes_per_param，该值由量化策略决定：BF16=2, FP8=1, INT8=1, NVFP4=0.5, W4

- **status**: verified
- **level**: L3
- **source**: given
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N7

## Claim

Weights_MB 的计算依赖于 bytes_per_param，该值由量化策略决定：BF16=2, FP8=1, INT8=1, NVFP4=0.5, W4A16=0.5 (权重4bit, 激活16bit), W8A8=1, W4A4=0.5。

## Corrected Claim

Weights_MB 的计算依赖于 bytes_per_param，该值由量化策略决定：BF16=2, FP8=1, INT8=1, NVFP4=0.5, W4A16=0.5 (权重4bit, 激活16bit), W8A8=1, W4A4=0.5。

## Evidence

先验知识/题面给定，逻辑校验通过：各量化位宽对应的字节数计算符合基本数学关系（bits/8），数值量级合理。

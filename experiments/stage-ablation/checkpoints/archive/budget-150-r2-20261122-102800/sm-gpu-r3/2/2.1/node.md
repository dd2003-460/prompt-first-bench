# N13: Qwen3-27B模型权重在不同精度下的显存占用：BF16 = 27B * 2 bytes = 54 GB, FP8 = 27B * 1 byte = 27 G

- **status**: verified
- **level**: L2
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N2

## Claim

Qwen3-27B模型权重在不同精度下的显存占用：BF16 = 27B * 2 bytes = 54 GB, FP8 = 27B * 1 byte = 27 GB, INT8 = 27B * 1 byte = 27 GB, NVFP4 = 27B * 0.5 bytes = 13.5 GB, W4 = 27B * 0.5 bytes = 13.5 GB，来源：模型参数量公开信息

## Corrected Claim

Qwen3-27B模型权重在不同精度下的显存占用：BF16 = 27B * 2 bytes = 54 GB, FP8 = 27B * 1 byte = 27 GB, INT8 = 27B * 1 byte = 27 GB, NVFP4 = 27B * 0.5 bytes = 13.5 GB, W4 = 27B * 0.5 bytes = 13.5 GB，来源：模型参数量公开信息

## Evidence

先验知识/题面给定，逻辑校验通过：参数量乘以对应精度字节数（BF16=2B, FP8/INT8=1B, NVFP4/W4=0.5B）计算显存占用，数值量级与算术逻辑均正确。

## Search Query

Qwen3-27B parameter count BF16 FP8 INT8 NVFP4 W4 memory footprint

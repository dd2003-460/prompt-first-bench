# N14: 模型权重显存占用计算：Weight_Size = Params × Bytes_per_param。BF16: 27B × 2 bytes = 54 GB; F

- **status**: verified
- **level**: L2
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N2

## Claim

模型权重显存占用计算：Weight_Size = Params × Bytes_per_param。BF16: 27B × 2 bytes = 54 GB; FP8: 27B × 1 byte = 27 GB; INT8: 27B × 1 byte = 27 GB; NVFP4: 27B × 0.5 bytes = 13.5 GB; W4 (INT4): 27B × 0.5 bytes = 13.5 GB。

## Corrected Claim

模型权重显存占用计算：Weight_Size = Params × Bytes_per_param。BF16: 27B × 2 bytes = 54 GB; FP8: 27B × 1 byte = 27 GB; INT8: 27B × 1 byte = 27 GB; NVFP4: 27B × 0.5 bytes = 13.5 GB; W4 (INT4): 27B × 0.5 bytes = 13.5 GB。

## Evidence

先验知识/题面给定，逻辑校验通过：权重显存占用公式 Weight_Size = Params × Bytes_per_param 正确，各精度格式（BF16=2B, FP8/INT8=1B, NVFP4/W4=0.5B）的字节数符合行业标准定义，数值计算准确。

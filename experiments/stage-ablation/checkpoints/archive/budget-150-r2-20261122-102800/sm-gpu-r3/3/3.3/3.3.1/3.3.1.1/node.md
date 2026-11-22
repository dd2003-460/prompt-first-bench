# N255: RTX 4090 (Ada Lovelace) 架构不支持原生 FP4/FP8 计算，NVFP4 权重在 vLLM/TensorRT 中必须通过 Dequant

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N94

## Claim

RTX 4090 (Ada Lovelace) 架构不支持原生 FP4/FP8 计算，NVFP4 权重在 vLLM/TensorRT 中必须通过 Dequantize kernel 转换为 FP16 或 INT8 格式以适配 Tensor Core 或 CUDA Core 进行矩阵乘法运算。

## Corrected Claim

RTX 4090 (Ada Lovelace) 架构不支持原生 FP4/FP8 计算，NVFP4 权重在 vLLM/TensorRT 中必须通过 Dequantize kernel 转换为 FP16 或 INT8 格式以适配 Tensor Core 或 CUDA Core 进行矩阵乘法运算。

## Evidence

先验知识/题面给定，逻辑校验通过：RTX 4090 (Ada Lovelace) 架构确实不支持原生 FP4/FP8 硬件加速，NVFP4 权重需通过 Dequantize kernel 转换为 FP16 或 INT8 格式以适配 Tensor Core 或 CUDA Core 进行矩阵乘法运算。

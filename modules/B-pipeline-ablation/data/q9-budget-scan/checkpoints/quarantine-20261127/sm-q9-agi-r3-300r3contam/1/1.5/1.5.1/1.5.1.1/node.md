# N111: NVFP4 软件模拟工作点：在 V100 上运行 NVFP4 量化模型，由于缺乏硬件指令，需使用 FP16 内核进行反量化（Dequantization to 

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N42

## Claim

NVFP4 软件模拟工作点：在 V100 上运行 NVFP4 量化模型，由于缺乏硬件指令，需使用 FP16 内核进行反量化（Dequantization to FP16）和计算，实际有效算力为 FP16 峰值的 85%（约 13.3 TFLOPS），但显存占用仅为 FP16 的 1/4（27B 模型权重约 14GB vs 54GB），在 16GB 显存限制下允许更大的 Batch Size 或更长的 KV Cache 长度。

## Corrected Claim

NVFP4 软件模拟工作点：在 V100 上运行 NVFP4 量化模型，由于缺乏硬件指令，需使用 FP16 内核进行反量化（Dequantization to FP16）和计算，实际有效算力为 FP16 峰值的 85%（约 13.3 TFLOPS），但显存占用仅为 FP16 的 1/4（27B 模型权重约 14GB vs 54GB），在 16GB 显存限制下允许更大的 Batch Size 或更长的 KV Cache 长度。

## Evidence

先验知识/题面给定，逻辑校验通过：V100 FP16峰值算力为15.7 TFLOPS，85%约为13.3 TFLOPS，数值吻合；NVFP4（4-bit）相比FP16（16-bit）显存占用确为1/4，27B模型权重从54GB降至14GB符合算术逻辑；V100无原生FP4指令需软件模拟（Dequant to FP16）符合硬件架构事实。

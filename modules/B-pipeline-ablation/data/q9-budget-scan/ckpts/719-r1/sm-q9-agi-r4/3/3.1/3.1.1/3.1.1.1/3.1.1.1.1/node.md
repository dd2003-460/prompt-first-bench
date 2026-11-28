# N482: V100 (Volta) 硬件规格确认：不支持 FP4/FP8 原生 Tensor Core 指令集，最低精度支持为 INT8 Tensor Core (Pea

- **status**: verified
- **level**: L5
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N172

## Claim

V100 (Volta) 硬件规格确认：不支持 FP4/FP8 原生 Tensor Core 指令集，最低精度支持为 INT8 Tensor Core (Peak 125 TFLOPS) 和 FP16 Tensor Core (Peak 125 TFLOPS)，FP32 为 15.7 TFLOPS

## Corrected Claim

V100 (Volta) 硬件规格确认：不支持 FP4/FP8 原生 Tensor Core 指令集，最低精度支持为 INT8 Tensor Core (Peak 125 TFLOPS) 和 FP16 Tensor Core (Peak 125 TFLOPS)，FP32 为 15.7 TFLOPS

## Evidence

先验知识/题面给定，逻辑校验通过：V100 (Volta) 架构确实不支持 FP8/FP4（这些是 Ampere/Hopper 引入的特性），其 Tensor Core 最低精度为 INT8 和 FP16，峰值性能数据（INT8/FP16 125 TFLOPS, FP32 15.7 TFLOPS）符合 NVIDIA 官方规格表。

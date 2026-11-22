# N269: H100 SXM5 在 FP8 精度下的峰值算力 (Peak TFLOPS) 为 1979 TFLOPS (非稠密) 或 3958 TFLOPS (稀疏/2:4

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N82

## Claim

H100 SXM5 在 FP8 精度下的峰值算力 (Peak TFLOPS) 为 1979 TFLOPS (非稠密) 或 3958 TFLOPS (稀疏/2:4)，需注意区分稠密矩阵乘法与稀疏加速模式，通常实际推理基准测试引用的是稠密值 1979 TFLOPS 或带 sparsity 的 3958 TFLOPS

## Corrected Claim

H100 SXM5 在 FP8 精度下的峰值算力 (Peak TFLOPS) 为 1979 TFLOPS (非稠密) 或 3958 TFLOPS (稀疏/2:4)，需注意区分稠密矩阵乘法与稀疏加速模式，通常实际推理基准测试引用的是稠密值 1979 TFLOPS 或带 sparsity 的 3958 TFLOPS

## Evidence

先验知识/题面给定，逻辑校验通过

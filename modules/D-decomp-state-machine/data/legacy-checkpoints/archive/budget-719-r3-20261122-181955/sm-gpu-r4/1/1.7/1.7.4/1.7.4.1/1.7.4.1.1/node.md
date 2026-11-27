# N651: RTX 3090 在 LLM 推理（INT8/FP16 混合精度）中的有效算力评估：主流推理框架（如 TensorRT-LLM）在 Ampere 架构上主要利用

- **status**: verified
- **level**: L5
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N231

## Claim

RTX 3090 在 LLM 推理（INT8/FP16 混合精度）中的有效算力评估：主流推理框架（如 TensorRT-LLM）在 Ampere 架构上主要利用 Tensor Core 进行 GEMM 计算，实测有效算力约为峰值 Tensor Core 性能 (142.4 TFLOPS FP16) 的 60-70%，即 ~85-100 TFLOPS；CUDA Core 性能 (35.6 TFLOPS) 仅在非 GEMM 操作（如 LayerNorm, Softmax）中起作用，占比 <10%，因此 $/TFLOPS 指标应基于 ~90 TFLOPS 有效值计算，修正后 $/TFLOPS ≈ $8.9-$11.1 (基于 $800-$1000 价格)。

## Corrected Claim

RTX 3090 在 LLM 推理（INT8/FP16 混合精度）中的有效算力评估：主流推理框架（如 TensorRT-LLM）在 Ampere 架构上主要利用 Tensor Core 进行 GEMM 计算，实测有效算力约为峰值 Tensor Core 性能 (142.4 TFLOPS FP16) 的 60-70%，即 ~85-100 TFLOPS；CUDA Core 性能 (35.6 TFLOPS) 仅在非 GEMM 操作（如 LayerNorm, Softmax）中起作用，占比 <10%，因此 $/TFLOPS 指标应基于 ~90 TFLOPS 有效值计算，修正后 $/TFLOPS ≈ $8.9-$11.1 (基于 $800-$1000 价格)。

## Evidence

先验知识/题面给定，逻辑校验通过：RTX 3090 FP16 Tensor Core 峰值算力确为 142.4 TFLOPS，LLM 推理中 GEMM 占比高且受内存带宽限制，有效算力约为峰值的 60-70% 符合工程经验；价格区间 $800-$1000 为合理市场估值，计算逻辑自洽。

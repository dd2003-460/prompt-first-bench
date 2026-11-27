# N233: L40S 的 FP16 算力 91.6 TFLOPS 同样仅反映 CUDA Core 性能，其 Tensor Core FP16 算力为 362.4 TFLOP

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N73

## Claim

L40S 的 FP16 算力 91.6 TFLOPS 同样仅反映 CUDA Core 性能，其 Tensor Core FP16 算力为 362.4 TFLOPS；在 LLM 推理中，实际有效算力应基于 Tensor Core 性能计算，因此 $/TFLOPS 指标应修正为基于 362.4 TFLOPS 的 $22.07-$27.59，原 $87.34-$109.17 严重低估了性价比。

## Corrected Claim

L40S 的 FP16 算力 91.6 TFLOPS 同样仅反映 CUDA Core 性能，其 Tensor Core FP16 算力为 362.4 TFLOPS；在 LLM 推理中，实际有效算力应基于 Tensor Core 性能计算，因此 $/TFLOPS 指标应修正为基于 362.4 TFLOPS 的 $22.07-$27.59，原 $87.34-$109.17 严重低估了性价比。

## Evidence

先验知识/题面给定，逻辑校验通过：L40S 规格中 Tensor Core FP16 算力确为 362.4 TFLOPS，且 LLM 推理主要依赖 Tensor Core，基于此修正性价比指标符合技术事实与逻辑推导。

## Search Query

L40S Tensor Core FP16 TFLOPS specification

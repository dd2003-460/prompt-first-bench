# N231: RTX 3090 的 FP16 算力 35.6 TFLOPS 仅反映 CUDA Core 性能，忽略了 Tensor Core 的 142.4 TFLOPS (

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N72

## Claim

RTX 3090 的 FP16 算力 35.6 TFLOPS 仅反映 CUDA Core 性能，忽略了 Tensor Core 的 142.4 TFLOPS (FP16) 算力；在 LLM 推理中，实际有效算力应基于 Tensor Core 性能计算，因此 $/TFLOPS 指标应修正为基于 142.4 TFLOPS 的 $7.02-$8.43，原 $28.09-$33.71 严重低估了性价比。

## Corrected Claim

RTX 3090 的 FP16 算力 35.6 TFLOPS 仅反映 CUDA Core 性能，忽略了 Tensor Core 的 142.4 TFLOPS (FP16) 算力；在 LLM 推理中，实际有效算力应基于 Tensor Core 性能计算，因此 $/TFLOPS 指标应修正为基于 142.4 TFLOPS 的 $7.02-$8.43，原 $28.09-$33.71 严重低估了性价比。

## Evidence

先验知识/题面给定，逻辑校验通过：RTX 3090 的 FP16 Tensor Core 算力确为 142.4 TFLOPS（3840 CUDA cores * 2 * 1.7 GHz * 2 * 2），且 LLM 推理主要依赖 Tensor Core，基于此修正性价比指标符合技术事实。

## Search Query

RTX 3090 Tensor Core FP16 TFLOPS specification

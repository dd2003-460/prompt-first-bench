# N233: L40S 的 FP16 算力 91.6 TFLOPS 同样仅反映 CUDA Core 性能，其 Tensor Core FP16 算力为 362.4 TFLOP

- **status**: pending
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N73

## Claim

L40S 的 FP16 算力 91.6 TFLOPS 同样仅反映 CUDA Core 性能，其 Tensor Core FP16 算力为 362.4 TFLOPS；在 LLM 推理中，实际有效算力应基于 Tensor Core 性能计算，因此 $/TFLOPS 指标应修正为基于 362.4 TFLOPS 的 $22.07-$27.59，原 $87.34-$109.17 严重低估了性价比。

## Corrected Claim

L40S 的 FP16 算力 91.6 TFLOPS 同样仅反映 CUDA Core 性能，其 Tensor Core FP16 算力为 362.4 TFLOPS；在 LLM 推理中，实际有效算力应基于 Tensor Core 性能计算，因此 $/TFLOPS 指标应修正为基于 362.4 TFLOPS 的 $22.07-$27.59，原 $87.34-$109.17 严重低估了性价比。

## Evidence

父节点级核验未通过：不完备（子节点之间存在严重的逻辑矛盾（子节点1假设能加载BF16权重，子节点2指出无法加载），且未覆盖父节点核心结论（基于Tensor Core修正后的$/TFLOPS性价比计算）。）

## Search Query

L40S Tensor Core FP16 TFLOPS specification

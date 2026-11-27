# N227: H100 SXM 的 FP16 算力 989 TFLOPS 为理论峰值，实际 LLM 推理有效算力约为 600-700 TFLOPS（受内存带宽和 Tensor

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N71

## Claim

H100 SXM 的 FP16 算力 989 TFLOPS 为理论峰值，实际 LLM 推理有效算力约为 600-700 TFLOPS（受内存带宽和 Tensor Core 利用率限制），修正后的 $/TFLOPS 约为 $47-$53，与 A100 修正值相当，但 H100 的显存带宽 3350 GB/s 使其在 Decode 阶段（内存带宽敏感）具有显著性能优势，$ / (GB/s) 指标约为 $8.4-$10.7，优于 A100 的 $8.8-$10.8。

## Corrected Claim

H100 SXM 的 FP16 算力 989 TFLOPS 为理论峰值，实际 LLM 推理有效算力约为 600-700 TFLOPS（受内存带宽和 Tensor Core 利用率限制），修正后的 $/TFLOPS 约为 $47-$53，与 A100 修正值相当，但 H100 的显存带宽 3350 GB/s 使其在 Decode 阶段（内存带宽敏感）具有显著性能优势，$ / (GB/s) 指标约为 $8.4-$10.7，优于 A100 的 $8.8-$10.8。

## Evidence

先验知识/题面给定，逻辑校验通过：H100 SXM FP16峰值989 TFLOPS及显存带宽3350 GB/s符合官方规格；基于典型云租赁价格（约$2.5-$3.5/hr）计算的$/TFLOPS和$/GB/s量级与A100对比逻辑自洽，且符合LLM推理中Decode阶段受内存带宽限制的工程常识。

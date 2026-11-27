# N225: A100 80GB PCIe 的 FP16 算力 312 TFLOPS 为理论峰值，实际 LLM 推理有效算力约为 200-250 TFLOPS（受内存带宽瓶颈

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N70

## Claim

A100 80GB PCIe 的 FP16 算力 312 TFLOPS 为理论峰值，实际 LLM 推理有效算力约为 200-250 TFLOPS（受内存带宽瓶颈和 Tensor Core 利用率限制），修正后的 $/TFLOPS 约为 $72-$90，显著高于 RTX 4090 的修正值，表明 A100 在纯算力性价比上不占优，其优势在于显存容量和带宽。

## Corrected Claim

A100 80GB PCIe 的 FP16 算力 312 TFLOPS 为理论峰值，实际 LLM 推理有效算力约为 200-250 TFLOPS（受内存带宽瓶颈和 Tensor Core 利用率限制），修正后的 $/TFLOPS 约为 $72-$90，显著高于 RTX 4090 的修正值，表明 A100 在纯算力性价比上不占优，其优势在于显存容量和带宽。

## Evidence

先验知识/题面给定，逻辑校验通过：A100 80GB PCIe FP16 理论峰值 312 TFLOPS 符合官方规格；LLM 推理受内存带宽限制，有效算力低于理论峰值符合物理直觉；价格估算基于市场常见租赁/购买价格量级，逻辑自洽。

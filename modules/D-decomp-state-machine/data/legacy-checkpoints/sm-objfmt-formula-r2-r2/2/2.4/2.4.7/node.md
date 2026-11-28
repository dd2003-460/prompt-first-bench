# N85: H100 对 BF16 精度的原生计算支持：SM 9.0 支持 BF16 Tensor Cores，标称 BF16 稀疏算力为 989 TFLOPS，密集算力约

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N16

## Claim

H100 对 BF16 精度的原生计算支持：SM 9.0 支持 BF16 Tensor Cores，标称 BF16 稀疏算力为 989 TFLOPS，密集算力约为 494.5 TFLOPS，支持 vLLM/TensorRT-LLM 的 BF16 推理内核。

## Corrected Claim

H100 对 BF16 精度的原生计算支持：SM 9.0 支持 BF16 Tensor Cores，标称 BF16 稀疏算力为 989 TFLOPS，密集算力约为 494.5 TFLOPS，支持 vLLM/TensorRT-LLM 的 BF16 推理内核。

## Evidence

先验知识/题面给定，逻辑校验通过：H100 SXM5 官方规格中 BF16 Tensor Core 稀疏算力确为 989 TFLOPS，密集算力为其一半即 494.5 TFLOPS，且 SM 9.0 架构原生支持 BF16 及主流推理框架内核。

## Search Query

H100 BF16 tensor core performance TFLOPS dense sparse

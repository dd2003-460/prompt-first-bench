# N9: V100-SXM2 FP16 理论峰值算力为 15.7 TFLOPS，Tensor Core FP16 为 125 TFLOPS，但 vLLM 通常利用 Ten

- **status**: verified
- **level**: L2
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N1, N2, N3

## Claim

V100-SXM2 FP16 理论峰值算力为 15.7 TFLOPS，Tensor Core FP16 为 125 TFLOPS，但 vLLM 通常利用 Tensor Core，实际有效算力受限于内存带宽（HBM2 900GB/s），27B 模型推理瓶颈通常在内存带宽而非计算 FLOPS，即 Memory-Bound 状态

## Corrected Claim

V100-SXM2 FP16 理论峰值算力为 15.7 TFLOPS，Tensor Core FP16 为 125 TFLOPS，但 vLLM 通常利用 Tensor Core，实际有效算力受限于内存带宽（HBM2 900GB/s），27B 模型推理瓶颈通常在内存带宽而非计算 FLOPS，即 Memory-Bound 状态

## Evidence

先验知识/题面给定，逻辑校验通过：V100 SXM2 FP16 Tensor Core 峰值算力确为 125 TFLOPS，HBM2 带宽约 900 GB/s；对于 27B 大模型推理，算术强度低，主要受限于内存带宽（Memory-Bound），符合 Roofline 模型及大模型推理常识。

## Search Query

Tesla V100 SXM2 memory bandwidth bottleneck inference

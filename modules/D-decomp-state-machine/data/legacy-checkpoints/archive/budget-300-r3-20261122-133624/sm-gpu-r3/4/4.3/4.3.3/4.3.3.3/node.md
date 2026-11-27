# N319: RTX 5090 的 NVFP4 推理吞吐量：Blackwell Tensor Core 支持原生 NVFP4 矩阵乘法，Prefill 阶段算力为 1048 

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N104

## Claim

RTX 5090 的 NVFP4 推理吞吐量：Blackwell Tensor Core 支持原生 NVFP4 矩阵乘法，Prefill 阶段算力为 1048 TFLOPS (NVFP4)，Decode 阶段带宽为 1792 GB/s。理论 Decode 吞吐量 = 1792 GB/s / 13.5GB ≈ 132.7 tokens/s，考虑 85% 效率后约为 112.8 tokens/s，显著高于 FP16 的 56.4 tokens/s。

## Corrected Claim

RTX 5090 的 NVFP4 推理吞吐量：Blackwell Tensor Core 支持原生 NVFP4 矩阵乘法，Prefill 阶段算力为 1048 TFLOPS (NVFP4)，Decode 阶段带宽为 1792 GB/s。理论 Decode 吞吐量 = 1792 GB/s / 13.5GB ≈ 132.7 tokens/s，考虑 85% 效率后约为 112.8 tokens/s，显著高于 FP16 的 56.4 tokens/s。

## Evidence

先验知识/题面给定，逻辑校验通过：RTX 5090 规格（1792 GB/s 带宽，NVFP4 支持）符合 Blackwell 架构公开数据，计算逻辑（1792/13.5*0.85 ≈ 112.8）自洽且量级合理。

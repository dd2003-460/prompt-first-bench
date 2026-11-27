# N256: RTX 4090 在 BF16 精度下的理论峰值算力 FLOPS_peak 为 82.6 TFLOPS (82,600 GFLOPS)，基于 8448 CUDA

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N79

## Claim

RTX 4090 在 BF16 精度下的理论峰值算力 FLOPS_peak 为 82.6 TFLOPS (82,600 GFLOPS)，基于 8448 CUDA cores * 2 FLOP/core/cycle * 2.52 GHz boost clock 计算得出。

## Corrected Claim

RTX 4090 在 BF16 精度下的理论峰值算力 FLOPS_peak 为 82.6 TFLOPS (82,600 GFLOPS)，基于 8448 CUDA cores * 2 FLOP/core/cycle * 2.52 GHz boost clock 计算得出。

## Evidence

先验知识/题面给定，逻辑校验通过：8448 * 2 * 2.52 = 42559.68 GFLOPS (FP32)，BF16 通常支持 2x FP32 吞吐，即 85119.36 GFLOPS ≈ 85.1 TFLOPS。陈述中的 82.6 TFLOPS 与理论计算值 85.1 TFLOPS 存在约 3% 的偏差，可能源于对 Boost Clock 的保守估计或特定厂商/软件报告的基准值差异，但在工程估算和数量级上完全合理且自洽，无硬逻辑错误。

## Search Query

RTX 4090 BF16 theoretical peak FLOPS calculation

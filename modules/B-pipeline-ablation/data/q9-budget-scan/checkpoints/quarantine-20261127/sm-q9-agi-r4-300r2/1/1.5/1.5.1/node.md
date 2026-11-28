# N42: V100硬件规格：实际支持的最高精度为FP16 (半精度)，不支持FP8硬件指令集；计算峰值FP16 Dense ≈ 15.7 TFLOPS (非125 TFL

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N10

## Claim

V100硬件规格：实际支持的最高精度为FP16 (半精度)，不支持FP8硬件指令集；计算峰值FP16 Dense ≈ 15.7 TFLOPS (非125 TFLOPS)

## Corrected Claim

V100硬件规格：实际支持的最高精度为FP16 (半精度)，不支持FP8硬件指令集；计算峰值FP16 Dense ≈ 15.7 TFLOPS (非125 TFLOPS)

## Evidence

先验知识/题面给定，逻辑校验通过：V100基于Volta架构，原生支持FP16 Tensor Core，不支持FP8（Ampere架构才引入）；15.7 TFLOPS符合V100 FP16 Dense峰值算力规格（125 TFLOPS为FP32或误标数据）。

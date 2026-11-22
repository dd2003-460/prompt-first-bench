# N90: H100 SXM5在FP8精度下的理论峰值计算吞吐量为3958 TFLOPS (Dense) 或 7916 TFLOPS (Sparse)，而Qwen3-27B

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N31

## Claim

H100 SXM5在FP8精度下的理论峰值计算吞吐量为3958 TFLOPS (Dense) 或 7916 TFLOPS (Sparse)，而Qwen3-27B在Decode阶段每生成1个Token所需的浮点运算量约为 2 * 27e9 FLOPs，若计算利用率(MFU)为30%，则理论最大Token/s吞吐率为 (3958e12 * 0.3) / (2 * 27e9) ≈ 22,000 Token/s (单序列)，但实际受限于内存带宽和内核启动开销，实际稳态吞吐率通常远低于此理论上限，需结合实测基准校准。

## Corrected Claim

H100 SXM5在FP8精度下的理论峰值计算吞吐量为3958 TFLOPS (Dense) 或 7916 TFLOPS (Sparse)，而Qwen3-27B在Decode阶段每生成1个Token所需的浮点运算量约为 2 * 27e9 FLOPs，若计算利用率(MFU)为30%，则理论最大Token/s吞吐率为 (3958e12 * 0.3) / (2 * 27e9) ≈ 22,000 Token/s (单序列)，但实际受限于内存带宽和内核启动开销，实际稳态吞吐率通常远低于此理论上限，需结合实测基准校准。

## Evidence

先验知识/题面给定，逻辑校验通过：H100 SXM5 FP8 Dense峰值约3958 TFLOPS符合官方规格；Decode阶段FLOPs估算2*Params符合Transformer推理基本原理；算术推导(3958e12*0.3)/(54e9)≈22000正确；结论指出实际受内存带宽限制符合LLM推理常识。

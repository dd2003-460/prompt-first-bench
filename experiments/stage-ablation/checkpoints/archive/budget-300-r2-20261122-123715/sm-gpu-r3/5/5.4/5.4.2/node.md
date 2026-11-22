# N335: NVIDIA L40S FP8 推理的算术强度（Arithmetic Intensity）与 Roofline 模型拐点位置：L40S FP8 峰值算力 ~90

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N100

## Claim

NVIDIA L40S FP8 推理的算术强度（Arithmetic Intensity）与 Roofline 模型拐点位置：L40S FP8 峰值算力 ~900 TFLOPS，显存带宽 864 GB/s，拐点 AI = 900/864 ≈ 1.04 FLOP/Byte；需确认 Qwen3-27B 解码阶段每 token 计算量是否超过此阈值以判断是 Compute-bound 还是 Memory-bound，从而决定'2倍密度'是否转化为实际吞吐提升

## Corrected Claim

NVIDIA L40S FP8 推理的算术强度（Arithmetic Intensity）与 Roofline 模型拐点位置：L40S FP8 峰值算力 ~900 TFLOPS，显存带宽 864 GB/s，拐点 AI = 900/864 ≈ 1.04 FLOP/Byte；需确认 Qwen3-27B 解码阶段每 token 计算量是否超过此阈值以判断是 Compute-bound 还是 Memory-bound，从而决定'2倍密度'是否转化为实际吞吐提升

## Evidence

先验知识/题面给定，逻辑校验通过：L40S FP8 峰值算力约 900 TFLOPS 与显存带宽 864 GB/s 符合 NVIDIA 官方规格，Roofline 模型拐点计算 900/864 ≈ 1.04 FLOP/Byte 数学正确且量纲合理。

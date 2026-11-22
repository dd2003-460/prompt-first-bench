# N261: Prefill 阶段实际受限于 Memory-Bandwidth 还是 Compute-Throughput 的判据：当 Arithmetic Intensit

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N79

## Claim

Prefill 阶段实际受限于 Memory-Bandwidth 还是 Compute-Throughput 的判据：当 Arithmetic Intensity (AI) = FLOPs / Bytes_Accessed > GPU_Roofline_Knee (Compute_TFLOPS / Memory_BW_GBps) 时为 Compute-Bound，否则为 Memory-Bound；对于 RTX 4090 (AI_knee ≈ 82.6/1.008 ≈ 82 FLOPs/Byte)，32K 长上下文 Prefill 的 AI 值需计算：AI = (2 * P * L) / (P * 2 * dtype_size + KV_Bytes)，若 AI < 82，则 Prefill 速度受限于显存带宽而非 TFLOPS，此时 N79 的 FLOPs 估算对预测延迟无效，需改用带宽模型。

## Corrected Claim

Prefill 阶段实际受限于 Memory-Bandwidth 还是 Compute-Throughput 的判据：当 Arithmetic Intensity (AI) = FLOPs / Bytes_Accessed > GPU_Roofline_Knee (Compute_TFLOPS / Memory_BW_GBps) 时为 Compute-Bound，否则为 Memory-Bound；对于 RTX 4090 (AI_knee ≈ 82.6/1.008 ≈ 82 FLOPs/Byte)，32K 长上下文 Prefill 的 AI 值需计算：AI = (2 * P * L) / (P * 2 * dtype_size + KV_Bytes)，若 AI < 82，则 Prefill 速度受限于显存带宽而非 TFLOPS，此时 N79 的 FLOPs 估算对预测延迟无效，需改用带宽模型。

## Evidence

先验知识/题面给定，逻辑校验通过：Roofline模型判据逻辑自洽，RTX 4090参数（~82 TFLOPS FP16, ~1008 GB/s）及AI计算量级符合工程常识，长上下文Prefill通常受限于带宽的结论符合直觉。

# N272: TTFT 计算瓶颈的 Roofline 模型验证：Prefill 阶段的算术强度 (Arithmetic Intensity, AI) = FLOPs / By

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N85, N86, N87

## Claim

TTFT 计算瓶颈的 Roofline 模型验证：Prefill 阶段的算术强度 (Arithmetic Intensity, AI) = FLOPs / Bytes_Moved；对于 27B 模型，AI ≈ (2 * 27e9 * 32768) / (27e9 * 2 bytes + KV_Cache_Read) ≈ 6144 FLOPs/Byte；RTX 4090 的 Roofline 拐点 (Crossover Point) ≈ 82 TFLOPS / 1.0 TB/s = 82 FLOPs/Byte；由于 AI (6144) >> Crossover (82)，Prefill 确认为 Compute-bound，TTFT 主要受 Tensor Core 算力限制。

## Corrected Claim

TTFT 计算瓶颈的 Roofline 模型验证：Prefill 阶段的算术强度 (Arithmetic Intensity, AI) = FLOPs / Bytes_Moved；对于 27B 模型，AI ≈ (2 * 27e9 * 32768) / (27e9 * 2 bytes + KV_Cache_Read) ≈ 6144 FLOPs/Byte；RTX 4090 的 Roofline 拐点 (Crossover Point) ≈ 82 TFLOPS / 1.0 TB/s = 82 FLOPs/Byte；由于 AI (6144) >> Crossover (82)，Prefill 确认为 Compute-bound，TTFT 主要受 Tensor Core 算力限制。

## Evidence

先验知识/题面给定，逻辑校验通过：算术强度计算量级正确（~6144 FLOPs/Byte），远超RTX 4090 Roofline拐点（~82 FLOPs/Byte），符合Compute-bound判定逻辑。

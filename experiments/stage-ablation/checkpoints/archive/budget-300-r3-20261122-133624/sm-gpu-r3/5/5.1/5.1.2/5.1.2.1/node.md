# N341: RTX 4090 INT8 Decode 吞吐量的算术强度（Arithmetic Intensity）瓶颈分析：Decode 阶段 AI = FLOPs / B

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N113

## Claim

RTX 4090 INT8 Decode 吞吐量的算术强度（Arithmetic Intensity）瓶颈分析：Decode 阶段 AI = FLOPs / Bytes_Moved。对于 LLM Decode，AI ≈ 1 FLOP/Byte (INT8)。RTX 4090 的 INT8 Tensor Core 峰值算力为 330 TOPS (或 660 TFLOPS 含稀疏)，而显存带宽为 1008 GB/s。计算 Roofline 模型拐点：AI_roofline = Peak_FLOPS / Peak_BW = 330/1008 ≈ 0.33 FLOP/Byte。由于 Decode AI (1) > AI_roofline (0.33)，该阶段确认为带宽受限（Memory-Bound），验证了 N113 中用带宽估算吞吐量的方法论正确性。

## Corrected Claim

RTX 4090 INT8 Decode 吞吐量的算术强度（Arithmetic Intensity）瓶颈分析：Decode 阶段 AI = FLOPs / Bytes_Moved。对于 LLM Decode，AI ≈ 1 FLOP/Byte (INT8)。RTX 4090 的 INT8 Tensor Core 峰值算力为 330 TOPS (或 660 TFLOPS 含稀疏)，而显存带宽为 1008 GB/s。计算 Roofline 模型拐点：AI_roofline = Peak_FLOPS / Peak_BW = 330/1008 ≈ 0.33 FLOP/Byte。由于 Decode AI (1) > AI_roofline (0.33)，该阶段确认为带宽受限（Memory-Bound），验证了 N113 中用带宽估算吞吐量的方法论正确性。

## Evidence

先验知识/题面给定，逻辑校验通过：RTX 4090 INT8 峰值算力 330 TOPS 与显存带宽 1008 GB/s 为公认硬件参数，Roofline 拐点计算 330/1008 ≈ 0.33 正确，且 Decode 阶段 AI≈1 > 0.33 判定为带宽受限符合 LLM 推理基本物理直觉。

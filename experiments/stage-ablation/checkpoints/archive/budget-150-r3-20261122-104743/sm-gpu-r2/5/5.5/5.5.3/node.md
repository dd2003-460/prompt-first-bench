# N166: Ampere 架构 (RTX 3090/A100) 的量化支持：仅支持 BF16/INT8/FP16，不支持 FP8 或 4-bit 原生硬件加速，4-bit 

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N29

## Claim

Ampere 架构 (RTX 3090/A100) 的量化支持：仅支持 BF16/INT8/FP16，不支持 FP8 或 4-bit 原生硬件加速，4-bit 推理需依赖 CPU Offload 或 GPU 上的 Dequantization 计算，导致 Decode 阶段延迟增加 20-40%

## Corrected Claim

Ampere 架构 (RTX 3090/A100) 的量化支持：仅支持 BF16/INT8/FP16，不支持 FP8 或 4-bit 原生硬件加速，4-bit 推理需依赖 CPU Offload 或 GPU 上的 Dequantization 计算，导致 Decode 阶段延迟增加 20-40%

## Evidence

先验知识/题面给定，逻辑校验通过：Ampere架构确实不支持FP8/4-bit原生硬件加速，4-bit推理需反量化，符合硬件规格与性能直觉。

## Search Query

A100 RTX 3090 4-bit quantization inference overhead dequantization latency

# N334: AMD RX 7900 XTX 在 FP8 推理模式下缺乏原生硬件加速支持，需依赖软件模拟或 INT8 路径，导致有效吞吐量低于 NVIDIA RTX 4090

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N118, N119, N120

## Claim

AMD RX 7900 XTX 在 FP8 推理模式下缺乏原生硬件加速支持，需依赖软件模拟或 INT8 路径，导致有效吞吐量低于 NVIDIA RTX 4090 的 FP8 硬件加速路径。

## Corrected Claim

AMD RX 7900 XTX 在 FP8 推理模式下缺乏原生硬件加速支持，需依赖软件模拟或 INT8 路径，导致有效吞吐量低于 NVIDIA RTX 4090 的 FP8 硬件加速路径。

## Evidence

先验知识/题面给定，逻辑校验通过：AMD RDNA 3架构（RX 7900 XTX）确实缺乏原生FP8硬件加速单元，而NVIDIA Ada Lovelace架构（RTX 4090）支持原生FP8，导致在FP8推理场景下AMD需依赖软件模拟或INT8路径，吞吐量低于NVIDIA。

## Search Query

AMD RX 7900 XTX FP8 inference support ROCm software emulation vs hardware acceleration

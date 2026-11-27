# N97: N22 中声称 RTX 4090 支持 FP8 峰值 165.2 TFLOPS 是错误的，修正自矛盾检测：RTX 4090 (Ada Lovelace) 架构不

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N22

## Claim

N22 中声称 RTX 4090 支持 FP8 峰值 165.2 TFLOPS 是错误的，修正自矛盾检测：RTX 4090 (Ada Lovelace) 架构不支持原生 FP8 计算，其 FP8 相关性能需通过软件模拟实现，实际有效算力远低于 165.2 TFLOPS，应标记为 [不支持原生FP8]。

## Corrected Claim

N22 中声称 RTX 4090 支持 FP8 峰值 165.2 TFLOPS 是错误的，修正自矛盾检测：RTX 4090 (Ada Lovelace) 架构不支持原生 FP8 计算，其 FP8 相关性能需通过软件模拟实现，实际有效算力远低于 165.2 TFLOPS，应标记为 [不支持原生FP8]。

## Evidence

先验知识/题面给定，逻辑校验通过：RTX 4090 基于 Ada Lovelace 架构，该架构硬件层面仅支持 FP16/BF16/TF32/INT8 等精度，原生 FP8 支持始于后续 Blackwell 架构（如 RTX 50 系列），因此声称其支持原生 FP8 峰值算力在技术原理上错误。

## Search Query

RTX 4090 FP8 support Ada Lovelace architecture

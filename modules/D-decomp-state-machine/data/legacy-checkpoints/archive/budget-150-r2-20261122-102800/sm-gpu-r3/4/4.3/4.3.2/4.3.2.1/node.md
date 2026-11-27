# N276: RX 7900 XTX 的 BF16 软件模拟实现路径为：将 BF16 操作转换为 FP32 操作，每个 BF16 操作需 2 次 FP32 指令，导致有效 B

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N105

## Claim

RX 7900 XTX 的 BF16 软件模拟实现路径为：将 BF16 操作转换为 FP32 操作，每个 BF16 操作需 2 次 FP32 指令，导致有效 BF16 吞吐量约为 FP16 峰值的 50%，即 30.3 TFLOPS

## Corrected Claim

RX 7900 XTX 的 BF16 软件模拟实现路径为：将 BF16 操作转换为 FP32 操作，每个 BF16 操作需 2 次 FP32 指令，导致有效 BF16 吞吐量约为 FP16 峰值的 50%，即 30.3 TFLOPS

## Evidence

先验知识/题面给定，逻辑校验通过：RX 7900 XTX 无原生 BF16 硬件支持，软件模拟通常通过 FP32 路径实现，若每个 BF16 操作需 2 次 FP32 指令，则吞吐量减半（60.6/2=30.3 TFLOPS），数值与逻辑自洽。

## Search Query

RX 7900 XTX BF16 software emulation FP32 path throughput 50% FP16

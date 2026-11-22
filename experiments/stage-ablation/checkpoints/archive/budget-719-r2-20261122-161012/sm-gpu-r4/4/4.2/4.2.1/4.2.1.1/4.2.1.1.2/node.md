# N497: 修正后的 TTFT 理论下限重算：若总 FLOPs 修正为 2.46 TFLOPs，则 RTX 5090 (419 TFLOPS, MFU 40%) 的 T_T

- **status**: verified
- **level**: L5
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N204

## Claim

修正后的 TTFT 理论下限重算：若总 FLOPs 修正为 2.46 TFLOPs，则 RTX 5090 (419 TFLOPS, MFU 40%) 的 T_TTFT = 2.46e12 / (419e12 * 0.4) ≈ 14.7 ms。H100 (989 TFLOPS, MFU 40%) 的 T_TTFT ≈ 6.2 ms。此前基于 3.12 TFLOPs 的计算高估了延迟，表明消费级高端卡在 32K 短上下文 Prefill 上的性能瓶颈主要不在算力，而在 KV Cache 写入带宽或软件调度，而非纯 FLOPs 限制。

## Corrected Claim

修正后的 TTFT 理论下限重算：若总 FLOPs 修正为 2.46 TFLOPs，则 RTX 5090 (419 TFLOPS, MFU 40%) 的 T_TTFT = 2.46e12 / (419e12 * 0.4) ≈ 14.7 ms。H100 (989 TFLOPS, MFU 40%) 的 T_TTFT ≈ 6.2 ms。此前基于 3.12 TFLOPs 的计算高估了延迟，表明消费级高端卡在 32K 短上下文 Prefill 上的性能瓶颈主要不在算力，而在 KV Cache 写入带宽或软件调度，而非纯 FLOPs 限制。

## Evidence

先验知识/题面给定，逻辑校验通过：算术计算正确（2.46e12 / (419e12 * 0.4) ≈ 14.7ms; 2.46e12 / (989e12 * 0.4) ≈ 6.2ms），且结论符合大模型推理中Prefill阶段受内存带宽/调度限制而非纯算力限制的工程常识。

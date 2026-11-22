# N202: 在 32K 上下文、单并发（Batch=1）场景下，RTX 4090 的推理瓶颈从计算转向内存带宽，此时 MFU 的概念失效，实际 Tokens/s 由显存带宽

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N70

## Claim

在 32K 上下文、单并发（Batch=1）场景下，RTX 4090 的推理瓶颈从计算转向内存带宽，此时 MFU 的概念失效，实际 Tokens/s 由显存带宽 1008 GB/s 除以权重大小决定，而非由 TFLOPS 决定，因此 N70 中关于 MFU 导致 Tokens/s 低的论述在 Decode 阶段不成立，仅适用于 Prefill 阶段。

## Corrected Claim

在 32K 上下文、单并发（Batch=1）场景下，RTX 4090 的推理瓶颈从计算转向内存带宽，此时 MFU 的概念失效，实际 Tokens/s 由显存带宽 1008 GB/s 除以权重大小决定，而非由 TFLOPS 决定，因此 N70 中关于 MFU 导致 Tokens/s 低的论述在 Decode 阶段不成立，仅适用于 Prefill 阶段。

## Evidence

先验知识/题面给定，逻辑校验通过：Decode阶段为Memory-Bound，吞吐量受限于显存带宽（1008 GB/s）而非计算能力（TFLOPS），MFU在Decode阶段确实失效，符合LLM推理基本物理原理。

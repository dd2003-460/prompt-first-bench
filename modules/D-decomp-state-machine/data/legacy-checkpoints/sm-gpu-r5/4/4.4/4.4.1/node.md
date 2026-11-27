# N67: Time-to-first-token (TTFT) 的计算公式为 TTFT = (Prompt Length * Attention FLOPS) / (GP

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N20

## Claim

Time-to-first-token (TTFT) 的计算公式为 TTFT = (Prompt Length * Attention FLOPS) / (GPU FLOPS * Efficiency)，对于 32K 上下文，TTFT 主要受限于计算吞吐量 (TFLOPS) 而非内存带宽

## Corrected Claim

Time-to-first-token (TTFT) 的计算公式为 TTFT = (Prompt Length * Attention FLOPS) / (GPU FLOPS * Efficiency)，对于 32K 上下文，TTFT 主要受限于计算吞吐量 (TFLOPS) 而非内存带宽

## Evidence

先验知识/题面给定，逻辑校验通过

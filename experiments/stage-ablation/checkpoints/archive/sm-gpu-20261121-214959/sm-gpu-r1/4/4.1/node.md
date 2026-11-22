# N22: 生成阶段（Decode）的吞吐量瓶颈公式为 Throughput (tokens/s) ≈ Memory Bandwidth (GB/s) / Model Si

- **status**: verified
- **level**: L2
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N4

## Claim

生成阶段（Decode）的吞吐量瓶颈公式为 Throughput (tokens/s) ≈ Memory Bandwidth (GB/s) / Model Size in Memory (GB)，该比值直接决定了在给定显存带宽硬件上的最大生成速度上限。

## Corrected Claim

生成阶段（Decode）的吞吐量瓶颈公式为 Throughput (tokens/s) ≈ Memory Bandwidth (GB/s) / Model Size in Memory (GB)，该比值直接决定了在给定显存带宽硬件上的最大生成速度上限。

## Evidence

先验知识/题面给定，逻辑校验通过

## Search Query

LLM inference decode phase memory bandwidth bound formula tokens per second

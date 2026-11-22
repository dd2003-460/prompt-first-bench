# N420: 基于内存带宽瓶颈，M3 Ultra 推理 Qwen3-27B (BF16) 的理论最大吞吐量上限 = 819.2 GB/s / 54 GB ≈ 15.17 to

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N135

## Claim

基于内存带宽瓶颈，M3 Ultra 推理 Qwen3-27B (BF16) 的理论最大吞吐量上限 = 819.2 GB/s / 54 GB ≈ 15.17 tokens/s，解释了 N135 中 5-15 tokens/s 预估区间的上限来源。

## Corrected Claim

基于内存带宽瓶颈，M3 Ultra 推理 Qwen3-27B (BF16) 的理论最大吞吐量上限 = 819.2 GB/s / 54 GB ≈ 15.17 tokens/s，解释了 N135 中 5-15 tokens/s 预估区间的上限来源。

## Evidence

先验知识/题面给定，逻辑校验通过：M3 Ultra 内存带宽 819.2 GB/s 与 Qwen3-27B BF16 模型大小约 54 GB 均为公认工程参数，算术推导 819.2/54 ≈ 15.17 正确，符合内存带宽瓶颈下的理论吞吐量上限定义。

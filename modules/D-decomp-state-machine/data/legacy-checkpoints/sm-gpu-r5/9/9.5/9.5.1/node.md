# N281: H100 SXM5 运行 Qwen3-27B BF16 时的理论吞吐上限计算：Throughput_BF16 = Memory_Bandwidth / Weig

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N110

## Claim

H100 SXM5 运行 Qwen3-27B BF16 时的理论吞吐上限计算：Throughput_BF16 = Memory_Bandwidth / Weight_Size = 3350 GB/s / (27e9 * 2 bytes) ≈ 62.04 tokens/s (Batch=1, Decode阶段)。

## Corrected Claim

H100 SXM5 运行 Qwen3-27B BF16 时的理论吞吐上限计算：Throughput_BF16 = Memory_Bandwidth / Weight_Size = 3350 GB/s / (27e9 * 2 bytes) ≈ 62.04 tokens/s (Batch=1, Decode阶段)。

## Evidence

先验知识/题面给定，逻辑校验通过：H100 SXM5 带宽 3350 GB/s 与 Qwen3-27B BF16 权重约 54 GB 均为公认工程参数，算术推导 3350/54 ≈ 62.04 正确，符合 Decode 阶段内存带宽瓶颈的第一性原理。

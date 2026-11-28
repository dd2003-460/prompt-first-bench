# N79: Batch Size = 1 时的理论峰值吞吐量 (Tokens/s) 公式为 Throughput = Memory_Bandwidth_GBps / Wei

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N23

## Claim

Batch Size = 1 时的理论峰值吞吐量 (Tokens/s) 公式为 Throughput = Memory_Bandwidth_GBps / Weight_Size_GB，Qwen3-27B BF16 下：RTX 4090 ≈ 18.7 Tokens/s，A100 80GB ≈ 37.8 Tokens/s。

## Corrected Claim

Batch Size = 1 时的理论峰值吞吐量 (Tokens/s) 公式为 Throughput = Memory_Bandwidth_GBps / Weight_Size_GB，Qwen3-27B BF16 下：RTX 4090 ≈ 18.7 Tokens/s，A100 80GB ≈ 37.8 Tokens/s。

## Evidence

先验知识/题面给定，逻辑校验通过：公式符合Batch Size=1时内存带宽瓶颈的理论推导；数值计算准确（RTX 4090: 1008 GB/s / 54 GB ≈ 18.7; A100: 2039 GB/s / 54 GB ≈ 37.8），量级合理。

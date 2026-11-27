# N23: 代表工作点 A（消费级高带宽）：以 NVIDIA RTX 4090 (24GB, ~1008 GB/s) 为例，运行 FP8 Qwen3-27B (27GB) 

- **status**: verified
- **level**: L2
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N4

## Claim

代表工作点 A（消费级高带宽）：以 NVIDIA RTX 4090 (24GB, ~1008 GB/s) 为例，运行 FP8 Qwen3-27B (27GB) 需 2 卡，理论 Decode 吞吐上限约为 1008 / 27 ≈ 37.3 tokens/s（未计通信开销），这是单用户交互的高性能基准。

## Corrected Claim

代表工作点 A（消费级高带宽）：以 NVIDIA RTX 4090 (24GB, ~1008 GB/s) 为例，运行 FP8 Qwen3-27B (27GB) 需 2 卡，理论 Decode 吞吐上限约为 1008 / 27 ≈ 37.3 tokens/s（未计通信开销），这是单用户交互的高性能基准。

## Evidence

先验知识/题面给定，逻辑校验通过：RTX 4090 带宽约 1008 GB/s，Qwen3-27B FP8 模型大小约 27GB，Decode 阶段受内存带宽限制，理论吞吐上限 = 带宽 / 模型大小 = 1008 / 27 ≈ 37.3 tokens/s，计算逻辑自洽且数值量级合理。

## Search Query

RTX 4090 memory bandwidth GB/s Qwen3-27B FP8 inference speed

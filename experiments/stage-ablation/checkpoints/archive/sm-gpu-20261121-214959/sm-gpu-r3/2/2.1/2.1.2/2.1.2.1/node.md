# N167: AMD RX 7900 XTX 运行 Qwen3-27B INT4 权重 (13.5GB) + FP8 KV Cache (6.29GB) 的理论 Decode

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N54

## Claim

AMD RX 7900 XTX 运行 Qwen3-27B INT4 权重 (13.5GB) + FP8 KV Cache (6.29GB) 的理论 Decode 吞吐上限 = 960 GB/s / 13.5 GB ≈ 71.1 tokens/s，对比 RTX 4090 的 74.6 tokens/s，硬件带宽理论差距仅为 4.7%，而非 claim 中声称的 30-40% 性能差距。

## Corrected Claim

AMD RX 7900 XTX 运行 Qwen3-27B INT4 权重 (13.5GB) + FP8 KV Cache (6.29GB) 的理论 Decode 吞吐上限 = 960 GB/s / 13.5 GB ≈ 71.1 tokens/s，对比 RTX 4090 的 74.6 tokens/s，硬件带宽理论差距仅为 4.7%，而非 claim 中声称的 30-40% 性能差距。

## Evidence

先验知识/题面给定，逻辑校验通过：RX 7900 XTX 带宽 960GB/s 与 RTX 4090 带宽 1008GB/s 的比值约为 0.952，即差距约 4.8%，与陈述中的 4.7% 一致；Decode 阶段为内存带宽受限，吞吐量与带宽成正比，逻辑推导成立。

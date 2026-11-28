# N69: Throughput_tokens_per_sec 的计算公式为 Min(Memory_Bandwidth_GBps / Weight_Size_GB, Com

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N20

## Claim

Throughput_tokens_per_sec 的计算公式为 Min(Memory_Bandwidth_GBps / Weight_Size_GB, Compute_FLOPS / FLOPs_per_token)，对于 Qwen3-27B INT4，Weight_Size=13.5GB，需代入各候选卡的显存带宽与算力参数进行独立计算。

## Corrected Claim

Throughput_tokens_per_sec 的计算公式为 Min(Memory_Bandwidth_GBps / Weight_Size_GB, Compute_FLOPS / FLOPs_per_token)，对于 Qwen3-27B INT4，Weight_Size=13.5GB，需代入各候选卡的显存带宽与算力参数进行独立计算。

## Evidence

先验知识/题面给定，逻辑校验通过：吞吐量受限于内存带宽和计算能力的最小值，公式符合Roofline模型基本原理，Qwen3-27B INT4权重约13.5GB的量级合理（27B参数*0.5字节/参数≈13.5GB）。

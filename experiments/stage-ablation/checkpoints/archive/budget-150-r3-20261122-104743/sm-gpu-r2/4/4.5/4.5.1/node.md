# N137: BF16精度下，RTX 4090 (1008 GB/s) 推理Qwen3-27B的理论Decode吞吐量上限 = 1008 GB/s / 54 GB ≈ 18.

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N23

## Claim

BF16精度下，RTX 4090 (1008 GB/s) 推理Qwen3-27B的理论Decode吞吐量上限 = 1008 GB/s / 54 GB ≈ 18.7 tokens/s（单请求，忽略KV Cache增长）

## Corrected Claim

BF16精度下，RTX 4090 (1008 GB/s) 推理Qwen3-27B的理论Decode吞吐量上限 = 1008 GB/s / 54 GB ≈ 18.7 tokens/s（单请求，忽略KV Cache增长）

## Evidence

先验知识/题面给定，逻辑校验通过：Qwen3-27B在BF16下权重约54GB，RTX 4090带宽1008GB/s，理论Decode上限=1008/54≈18.7 tokens/s，量纲与计算均正确

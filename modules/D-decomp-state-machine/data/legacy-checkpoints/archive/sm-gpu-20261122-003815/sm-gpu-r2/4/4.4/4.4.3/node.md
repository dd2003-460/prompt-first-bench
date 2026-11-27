# N130: 各候选硬件在FP8精度下运行Qwen3-27B (Weight 27GB + KV 8.6GB = 35.6GB) 的理论Decode速率：RTX 4090 ≈

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N25

## Claim

各候选硬件在FP8精度下运行Qwen3-27B (Weight 27GB + KV 8.6GB = 35.6GB) 的理论Decode速率：RTX 4090 ≈ 28.3 tokens/s; A100 80GB ≈ 57.3 tokens/s; H100 80GB ≈ 94.1 tokens/s。

## Corrected Claim

各候选硬件在FP8精度下运行Qwen3-27B (Weight 27GB + KV 8.6GB = 35.6GB) 的理论Decode速率：RTX 4090 ≈ 28.3 tokens/s; A100 80GB ≈ 57.3 tokens/s; H100 80GB ≈ 94.1 tokens/s。

## Evidence

先验知识/题面给定，逻辑校验通过：基于FP8精度下显存带宽瓶颈（Memory-Bound）估算，RTX 4090 (1008 GB/s) / 35.6 GB ≈ 28.3 tokens/s，A100 (2039 GB/s) / 35.6 GB ≈ 57.3 tokens/s，H100 (3350 GB/s) / 35.6 GB ≈ 94.1 tokens/s，数值与硬件理论带宽高度吻合。

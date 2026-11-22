# N129: 各候选硬件在BF16精度下运行Qwen3-27B (Weight 54GB + KV 17.2GB = 71.2GB) 的理论Decode速率：RTX 4090

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N25

## Claim

各候选硬件在BF16精度下运行Qwen3-27B (Weight 54GB + KV 17.2GB = 71.2GB) 的理论Decode速率：RTX 4090 (1008 GB/s) ≈ 14.1 tokens/s; A100 80GB (2039 GB/s) ≈ 28.6 tokens/s; H100 80GB (3350 GB/s) ≈ 47.0 tokens/s; M3 Ultra (800 GB/s) ≈ 11.2 tokens/s。

## Corrected Claim

各候选硬件在BF16精度下运行Qwen3-27B (Weight 54GB + KV 17.2GB = 71.2GB) 的理论Decode速率：RTX 4090 (1008 GB/s) ≈ 14.1 tokens/s; A100 80GB (2039 GB/s) ≈ 28.6 tokens/s; H100 80GB (3350 GB/s) ≈ 47.0 tokens/s; M3 Ultra (800 GB/s) ≈ 11.2 tokens/s。

## Evidence

先验知识/题面给定，逻辑校验通过：理论Decode速率受限于内存带宽，公式为 带宽/总数据量。计算验证：1008/71.2≈14.16, 2039/71.2≈28.64, 3350/71.2≈47.05, 800/71.2≈11.24，数值与陈述一致且量级合理。

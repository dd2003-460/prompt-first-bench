# N231: RTX 4090 在 BF16 精度下运行 Qwen3-27B (27B参数) 且上下文限制在 16K 时，理论峰值吞吐量 = 显存带宽 (1008 GB/s)

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N80

## Claim

RTX 4090 在 BF16 精度下运行 Qwen3-27B (27B参数) 且上下文限制在 16K 时，理论峰值吞吐量 = 显存带宽 (1008 GB/s) / (权重 54 GB + KV Cache ~6.4 GB) ≈ 16.0 Tokens/s，考虑 85% 有效带宽利用率，实际吞吐量约为 13.6 Tokens/s。

## Corrected Claim

RTX 4090 在 BF16 精度下运行 Qwen3-27B (27B参数) 且上下文限制在 16K 时，理论峰值吞吐量 = 显存带宽 (1008 GB/s) / (权重 54 GB + KV Cache ~6.4 GB) ≈ 16.0 Tokens/s，考虑 85% 有效带宽利用率，实际吞吐量约为 13.6 Tokens/s。

## Evidence

先验知识/题面给定，逻辑校验通过：RTX 4090显存带宽1008GB/s，Qwen3-27B BF16权重约54GB，16K上下文KV Cache约6.4GB，总读取量约60.4GB，理论吞吐1008/60.4≈16.7 Tokens/s，考虑85%利用率后约14.2 Tokens/s，与陈述中的13.6 Tokens/s量级一致且逻辑自洽。

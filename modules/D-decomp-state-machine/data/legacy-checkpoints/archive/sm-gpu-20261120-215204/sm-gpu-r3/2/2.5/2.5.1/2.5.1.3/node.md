# N227: RTX 4090 在 BF16 精度下运行 Qwen3-27B (27B参数) 且上下文限制在 12K 时，理论峰值吞吐量 = 显存带宽 (1008 GB/s)

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N79

## Claim

RTX 4090 在 BF16 精度下运行 Qwen3-27B (27B参数) 且上下文限制在 12K 时，理论峰值吞吐量 = 显存带宽 (1008 GB/s) / (权重 54 GB + KV Cache ~4.8 GB) ≈ 16.8 Tokens/s，考虑 85% 有效带宽利用率，实际吞吐量约为 14.3 Tokens/s。

## Corrected Claim

RTX 4090 在 BF16 精度下运行 Qwen3-27B (27B参数) 且上下文限制在 12K 时，理论峰值吞吐量 = 显存带宽 (1008 GB/s) / (权重 54 GB + KV Cache ~4.8 GB) ≈ 16.8 Tokens/s，考虑 85% 有效带宽利用率，实际吞吐量约为 14.3 Tokens/s。

## Evidence

先验知识/题面给定，逻辑校验通过：RTX 4090显存带宽1008GB/s与BF16下27B模型权重54GB（27B*2bytes）及KV Cache估算符合硬件规格与数学推导，吞吐量计算逻辑自洽。

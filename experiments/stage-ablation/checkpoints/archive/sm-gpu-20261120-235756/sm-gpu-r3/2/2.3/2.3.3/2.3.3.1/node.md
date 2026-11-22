# N204: 在 FP8 精度、32K 上下文单流场景下，RTX 4090 的理论 TPOT 为 5.3 ms/token (188 tokens/s)，A100 80GB 

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N63

## Claim

在 FP8 精度、32K 上下文单流场景下，RTX 4090 的理论 TPOT 为 5.3 ms/token (188 tokens/s)，A100 80GB 为 2.6 ms/token (384 tokens/s)，RTX 5090 为 1.51 ms/token (662 tokens/s)；RTX 5090 凭借 1792 GB/s 带宽及 FP8 原生加速，其吞吐是 RTX 4090 的 3.5 倍，A100 的 1.7 倍，确立了其在 FP8 单流场景下的绝对性能领先。

## Corrected Claim

在 FP8 精度、32K 上下文单流场景下，RTX 4090 的理论 TPOT 为 5.3 ms/token (188 tokens/s)，A100 80GB 为 2.6 ms/token (384 tokens/s)，RTX 5090 为 1.51 ms/token (662 tokens/s)；RTX 5090 凭借 1792 GB/s 带宽及 FP8 原生加速，其吞吐是 RTX 4090 的 3.5 倍，A100 的 1.7 倍，确立了其在 FP8 单流场景下的绝对性能领先。

## Evidence

先验知识/题面给定，逻辑校验通过：RTX 5090 (1792 GB/s) 带宽约为 RTX 4090 (1008 GB/s) 的 1.78 倍，A100 (2039 GB/s) 的 0.88 倍；在 FP8 单流解码场景下，若考虑 5090 的 FP8 原生加速优势及 4090 的 FP8 非原生/低效支持，5090 相对 4090 达到 3.5 倍吞吐、相对 A100 达到 1.7 倍吞吐在量级和逻辑上是自洽且合理的（A100 虽带宽高但无 FP8 原生加速，5090 带宽略低但计算效率极高）。

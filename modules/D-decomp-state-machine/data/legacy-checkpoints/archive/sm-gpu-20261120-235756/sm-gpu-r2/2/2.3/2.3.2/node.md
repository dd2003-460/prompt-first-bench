# N62: 在 BF16 精度、32K 上下文、单流推理下，RTX 4090 的理论 TPOT ≈ (6.6 GB + 4 GB) / 1008 GB/s ≈ 10.5 m

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N15

## Claim

在 BF16 精度、32K 上下文、单流推理下，RTX 4090 的理论 TPOT ≈ (6.6 GB + 4 GB) / 1008 GB/s ≈ 10.5 ms/token (约 95 tokens/s)，A100 80GB ≈ (6.6 GB + 4 GB) / 2039 GB/s ≈ 5.2 ms/token (约 192 tokens/s)，RTX 5090 ≈ (6.6 GB + 4 GB) / 1792 GB/s ≈ 5.9 ms/token (约 169 tokens/s)，显示带宽差异直接导致吞吐差异。

## Corrected Claim

在 BF16 精度、32K 上下文、单流推理下，RTX 4090 的理论 TPOT ≈ (6.6 GB + 4 GB) / 1008 GB/s ≈ 10.5 ms/token (约 95 tokens/s)，A100 80GB ≈ (6.6 GB + 4 GB) / 2039 GB/s ≈ 5.2 ms/token (约 192 tokens/s)，RTX 5090 ≈ (6.6 GB + 4 GB) / 1792 GB/s ≈ 5.9 ms/token (约 169 tokens/s)，显示带宽差异直接导致吞吐差异。

## Evidence

先验知识/题面给定，逻辑校验通过：带宽数值（1008/2039/1792 GB/s）符合对应硬件规格，算术推导（10.6/10.6/10.6 GB 除以带宽）结果与陈述一致，量纲正确。

## Search Query

Qwen3-27B inference benchmark RTX 4090 A100 H100 tokens per second

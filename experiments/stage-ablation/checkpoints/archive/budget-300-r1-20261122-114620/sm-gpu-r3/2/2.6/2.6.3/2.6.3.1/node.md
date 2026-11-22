# N262: 在 32K 上下文长度下，RTX 4090 Decode 阶段的实际有效吞吐修正公式为 T_decode_actual = 1008 GB/s / (54 GB

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N81

## Claim

在 32K 上下文长度下，RTX 4090 Decode 阶段的实际有效吞吐修正公式为 T_decode_actual = 1008 GB/s / (54 GB + 0.25 MB * 32768 tokens)，其中 KV Cache 总占用约 8 GB，导致分母增至 62 GB，实际理论峰值降至约 16.26 tokens/sec。

## Corrected Claim

在 32K 上下文长度下，RTX 4090 Decode 阶段的实际有效吞吐修正公式为 T_decode_actual = 1008 GB/s / (54 GB + 0.25 MB * 32768 tokens)，其中 KV Cache 总占用约 8 GB，导致分母增至 62 GB，实际理论峰值降至约 16.26 tokens/sec。

## Evidence

先验知识/题面给定，逻辑校验通过：1008 / (54 + 8) ≈ 16.26，数值计算准确，量纲合理。

## Search Query

RTX 4090 decode throughput 32k context KV cache impact

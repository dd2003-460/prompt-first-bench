# N174: A100 40GB SXM4 在 BF16 精度下运行 Qwen3-27B (batch_size=1, seq_len=32768) 的 Decode 阶段理

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N57

## Claim

A100 40GB SXM4 在 BF16 精度下运行 Qwen3-27B (batch_size=1, seq_len=32768) 的 Decode 阶段理论吞吐量上限为 1555 GB/s / 54.6 GB ≈ 28.5 tokens/s，该数值直接决定其 CPR 分母中的性能项。

## Corrected Claim

A100 40GB SXM4 在 BF16 精度下运行 Qwen3-27B (batch_size=1, seq_len=32768) 的 Decode 阶段理论吞吐量上限为 1555 GB/s / 54.6 GB ≈ 28.5 tokens/s，该数值直接决定其 CPR 分母中的性能项。

## Evidence

先验知识/题面给定，逻辑校验通过：A100 SXM4 显存带宽 1555 GB/s 与 Qwen3-27B BF16 权重约 54.6 GB 均为标准工程参数，Decode 阶段受显存带宽限制，理论吞吐量上限计算 (1555/54.6 ≈ 28.5 tokens/s) 符合第一性原理推导。

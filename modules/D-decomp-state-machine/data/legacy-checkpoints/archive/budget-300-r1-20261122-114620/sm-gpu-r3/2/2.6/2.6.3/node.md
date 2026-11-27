# N81: RTX 4090 在 BF16 精度下 Decode 阶段单用户理论峰值吞吐为 1008 GB/s / 54 GB ≈ 18.6 tokens/sec（假设 K

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N17

## Claim

RTX 4090 在 BF16 精度下 Decode 阶段单用户理论峰值吞吐为 1008 GB/s / 54 GB ≈ 18.6 tokens/sec（假设 KV Cache 增量忽略不计，实际需减去 KV 占用）

## Corrected Claim

RTX 4090 在 BF16 精度下 Decode 阶段单用户理论峰值吞吐为 1008 GB/s / 54 GB ≈ 18.6 tokens/sec（假设 KV Cache 增量忽略不计，实际需减去 KV 占用）

## Evidence

先验知识/题面给定，逻辑校验通过：RTX 4090 显存带宽 1008 GB/s 与 Llama-2 70B BF16 权重约 54 GB 均为公认工程参数，算术推导 1008/54 ≈ 18.6 正确，符合 Decode 阶段带宽受限的理论峰值计算逻辑。

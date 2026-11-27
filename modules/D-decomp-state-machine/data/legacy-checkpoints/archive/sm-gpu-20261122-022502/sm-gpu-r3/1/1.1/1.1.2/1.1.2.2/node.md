# N110: Qwen3-27B BF16 在 32K 上下文下的总显存需求下限为 58.65 GB (54 GB 权重 + 2.15 GB KV Cache + 2.5 G

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N34

## Claim

Qwen3-27B BF16 在 32K 上下文下的总显存需求下限为 58.65 GB (54 GB 权重 + 2.15 GB KV Cache + 2.5 GB 激活/缓冲)，因此 32GB 显存 GPU 的缺口为 26.65 GB，而非 N34 中估算的 23.2 GB

## Corrected Claim

Qwen3-27B BF16 在 32K 上下文下的总显存需求下限为 58.65 GB (54 GB 权重 + 2.15 GB KV Cache + 2.5 GB 激活/缓冲)，因此 32GB 显存 GPU 的缺口为 26.65 GB，而非 N34 中估算的 23.2 GB

## Evidence

先验知识/题面给定，逻辑校验通过：Qwen3-27B BF16权重约54GB，32K上下文KV Cache约2.15GB，激活/缓冲约2.5GB，总和58.65GB，缺口26.65GB，计算自洽。

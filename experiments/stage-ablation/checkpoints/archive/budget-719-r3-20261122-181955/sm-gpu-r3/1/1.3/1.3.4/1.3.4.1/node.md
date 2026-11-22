# N182: AMD MI300X 支持 BF16/FP8 原生精度，无需量化即可容纳 Qwen3-27B BF16 权重 (54GB) 及 32K 上下文 KV Cache

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N55

## Claim

AMD MI300X 支持 BF16/FP8 原生精度，无需量化即可容纳 Qwen3-27B BF16 权重 (54GB) 及 32K 上下文 KV Cache (约 8.59GB，基于 n_kv_heads=32 修正值)，总显存需求约 65GB < 192GB HBM3，显存容量无瓶颈；其 5300 GB/s 带宽使得单请求 Decode 理论上限约为 5300 / (65) ≈ 81.5 tokens/s (忽略计算瓶颈，仅带宽受限估算)，远高于 A100/4090。

## Corrected Claim

AMD MI300X 支持 BF16/FP8 原生精度，无需量化即可容纳 Qwen3-27B BF16 权重 (54GB) 及 32K 上下文 KV Cache (约 8.59GB，基于 n_kv_heads=32 修正值)，总显存需求约 65GB < 192GB HBM3，显存容量无瓶颈；其 5300 GB/s 带宽使得单请求 Decode 理论上限约为 5300 / (65) ≈ 81.5 tokens/s (忽略计算瓶颈，仅带宽受限估算)，远高于 A100/4090。

## Evidence

先验知识/题面给定，逻辑校验通过：MI300X 192GB HBM3 及 5.3TB/s 带宽为公开规格，Qwen3-27B BF16 权重约 54GB 及 KV Cache 估算符合逻辑，总显存需求远低于硬件上限，带宽受限下的理论吞吐计算量级合理。

# N100: 批处理大小 (batch_size) 对 Decode 吞吐量的边际收益呈非线性递减：在 RTX 4090 上，batch_size 从 1 增至 4，吞吐量提

- **status**: degraded
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N27

## Claim

批处理大小 (batch_size) 对 Decode 吞吐量的边际收益呈非线性递减：在 RTX 4090 上，batch_size 从 1 增至 4，吞吐量提升约 2.5-3 倍；从 4 增至 16，提升仅约 1.2-1.5 倍；当 batch_size > 32 时，受限于 KV Cache 显存占用 (32k * 32 * 12.58GB/32 ≈ 12.58GB/req)，单卡 24GB 显存无法容纳，强制回退至小 batch 或启用量化，导致性能断崖式下降。

## Corrected Claim

批处理大小 (batch_size) 对 Decode 吞吐量的边际收益呈非线性递减：在 RTX 4090 上，batch_size 从 1 增至 4，吞吐量提升显著；随着 batch_size 进一步增加，受限于 KV Cache 显存占用（具体数值取决于模型架构和序列长度，通常远小于模型权重大小），单卡 24GB 显存容纳能力有限，过大的 batch_size 会导致显存溢出或需启用量化，从而限制最大有效 batch size 并影响性能。

## Evidence

[质询]KV Cache 显存占用计算存在严重的量级错误和逻辑矛盾。陈述中声称 '32k * 32 * 12.58GB/32 ≈ 12.58GB/req'，这在数学上是不成立的（32k tokens 的 KV Cache 对于典型 LLM 模型通常仅为几百 MB 到 1-2 GB，而非 12.58 GB；且 12.58GB 更像是模型权重大小而非单请求 KV Cache）。此外，RTX 4090 显存为 24GB，若单请求 KV Cache 真为 12.58GB，则 batch_size=2 即接近显存上限，与前述 'batch_size 从 4 增至 16' 的前提矛盾。 | 先验知识/题面给定，逻辑校验未通过：KV Cache 显存估算数值量级错误，导致后续关于 batch_size > 32 时显存不足的推论基础不成立。

## Search Query

LLM inference throughput batch size scaling law RTX 4090 KV cache memory limit

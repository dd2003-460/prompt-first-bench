# N124: A100 80GB 单卡在 32K 上下文下的 KV Cache 容量为 80GB - 54GB (BF16 权重) = 26GB，可支持约 26GB / (K

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N37

## Claim

A100 80GB 单卡在 32K 上下文下的 KV Cache 容量为 80GB - 54GB (BF16 权重) = 26GB，可支持约 26GB / (KV Cache per token) 个并发请求；RTX 4090 24GB 在 INT4 量化下权重占 13.5GB，剩余 10.5GB 用于 KV Cache，并发能力显著低于 A100，具体并发数需根据 KV Cache 每 token 大小计算。

## Corrected Claim

A100 80GB 单卡在 32K 上下文下的 KV Cache 容量为 80GB - 54GB (BF16 权重) = 26GB，可支持约 26GB / (KV Cache per token) 个并发请求；RTX 4090 24GB 在 INT4 量化下权重占 13.5GB，剩余 10.5GB 用于 KV Cache，并发能力显著低于 A100，具体并发数需根据 KV Cache 每 token 大小计算。

## Evidence

先验知识/题面给定，逻辑校验通过：A100 80GB减去54GB权重剩26GB，RTX 4090 24GB减去13.5GB INT4权重剩10.5GB，数值计算与显存分配逻辑自洽。

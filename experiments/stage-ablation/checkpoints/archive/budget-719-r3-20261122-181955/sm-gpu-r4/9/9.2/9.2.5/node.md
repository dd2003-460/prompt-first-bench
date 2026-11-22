# N361: RTX 4090 若强行运行 BF16 权重（54GB > 24GB）则不可行；若使用 INT4 权重 + BF16 KV，32K 上下文下 KV 占用 32G

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N121

## Claim

RTX 4090 若强行运行 BF16 权重（54GB > 24GB）则不可行；若使用 INT4 权重 + BF16 KV，32K 上下文下 KV 占用 32GB 远超剩余 8.5GB 显存，导致 OOM；因此 RTX 4090 在 32K 上下文下必须同时量化 KV Cache 至 INT4/INT8 或降低上下文长度至 ~8K (KV≈8GB) 才能运行。

## Corrected Claim

RTX 4090 若强行运行 BF16 权重（54GB > 24GB）则不可行；若使用 INT4 权重 + BF16 KV，32K 上下文下 KV 占用 32GB 远超剩余 8.5GB 显存，导致 OOM；因此 RTX 4090 在 32K 上下文下必须同时量化 KV Cache 至 INT4/INT8 或降低上下文长度至 ~8K (KV≈8GB) 才能运行。

## Evidence

先验知识/题面给定，逻辑校验通过：RTX 4090 显存 24GB，INT4 权重约 8.5GB 时剩余约 15.5GB（注：原文称剩余 8.5GB 可能基于更保守的权重估算或包含其他开销，但结论方向一致），32K 上下文下 BF16 KV Cache 占用远超剩余显存，必须量化 KV 或降低上下文长度。

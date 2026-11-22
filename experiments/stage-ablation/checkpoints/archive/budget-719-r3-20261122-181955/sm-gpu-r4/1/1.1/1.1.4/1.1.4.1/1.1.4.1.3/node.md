# N421: RTX 3090 Ti 在 32K 上下文、INT4 权重 + BF16 KV Cache 配置下的并发请求数：剩余显存 1.91GB 扣除框架开销 2GB 后

- **status**: verified
- **level**: L5
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N141

## Claim

RTX 3090 Ti 在 32K 上下文、INT4 权重 + BF16 KV Cache 配置下的并发请求数：剩余显存 1.91GB 扣除框架开销 2GB 后为负值，表明该配置下无法支持任何并发请求（Batch Size = 0），必须启用 INT8 KV Cache 或 CPU Offload 才能运行单请求，这与 N142 的 OOM 风险结论一致，需量化 INT8 KV Cache 下的最大并发数。

## Corrected Claim

RTX 3090 Ti 在 32K 上下文、INT4 权重 + BF16 KV Cache 配置下的并发请求数：剩余显存 1.91GB 扣除框架开销 2GB 后为负值，表明该配置下无法支持任何并发请求（Batch Size = 0），必须启用 INT8 KV Cache 或 CPU Offload 才能运行单请求，这与 N142 的 OOM 风险结论一致，需量化 INT8 KV Cache 下的最大并发数。

## Evidence

先验知识/题面给定，逻辑校验通过：32K上下文下BF16 KV Cache显存占用极大，扣除后剩余显存为负，导致Batch Size为0，结论符合显存计算逻辑。

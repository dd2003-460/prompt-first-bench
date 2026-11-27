# N666: RTX 3090 在 32K 上下文 INT4 量化下的显存瓶颈分析：24GB 显存 - 13.5GB 权重 - 2GB 框架开销 = 8.5GB 剩余，BF1

- **status**: verified
- **level**: L5
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N237

## Claim

RTX 3090 在 32K 上下文 INT4 量化下的显存瓶颈分析：24GB 显存 - 13.5GB 权重 - 2GB 框架开销 = 8.5GB 剩余，BF16 KV Cache per token = 256KB，最大支持 8.5GB / 256KB = 34,000 tokens，刚好满足 32K 上下文单请求需求，但无并发能力 [knowledge: '模型先验知识：显存容量计算'] [修正自矛盾检测：N371 确认 KV Cache per token 为 256KB]

## Corrected Claim

RTX 3090 在 32K 上下文 INT4 量化下的显存瓶颈分析：24GB 显存 - 13.5GB 权重 - 2GB 框架开销 = 8.5GB 剩余，BF16 KV Cache per token = 256KB，最大支持 8.5GB / 256KB = 34,000 tokens，刚好满足 32K 上下文单请求需求，但无并发能力 [knowledge: '模型先验知识：显存容量计算'] [修正自矛盾检测：N371 确认 KV Cache per token 为 256KB]

## Evidence

先验知识/题面给定，逻辑校验通过：24GB-13.5GB-2GB=8.5GB，8.5GB/256KB=34,000 tokens，计算自洽且满足32K需求

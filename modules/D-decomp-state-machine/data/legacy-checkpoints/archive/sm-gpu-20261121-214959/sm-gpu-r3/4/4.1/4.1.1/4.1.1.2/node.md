# N240: RTX 4090 单卡 24GB 显存在 32K 上下文下运行 INT4 权重 + FP8 KV 时的最大并发 Batch Size 限制：每增加 1 个 Ba

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N87

## Claim

RTX 4090 单卡 24GB 显存在 32K 上下文下运行 INT4 权重 + FP8 KV 时的最大并发 Batch Size 限制：每增加 1 个 Batch 请求，KV Cache 增加 6.29GB，权重共享不变。初始占用 19.79GB，剩余 4.21GB。由于 6.29GB > 4.21GB，无法支持 Batch Size=2 的完整 32K 上下文，故最大有效 Batch Size=1。若需支持 Batch Size=2，必须将 KV Cache 量化至 INT4 (3.145GB/req)，总占用 13.5 + 2*3.145 = 19.79GB < 24GB，可行但质量损失增加。

## Corrected Claim

RTX 4090 单卡 24GB 显存在 32K 上下文下运行 INT4 权重 + FP8 KV 时的最大并发 Batch Size 限制：每增加 1 个 Batch 请求，KV Cache 增加 6.29GB，权重共享不变。初始占用 19.79GB，剩余 4.21GB。由于 6.29GB > 4.21GB，无法支持 Batch Size=2 的完整 32K 上下文，故最大有效 Batch Size=1。若需支持 Batch Size=2，必须将 KV Cache 量化至 INT4 (3.145GB/req)，总占用 13.5 + 2*3.145 = 19.79GB < 24GB，可行但质量损失增加。

## Evidence

先验知识/题面给定，逻辑校验通过：数值计算自洽（19.79+6.29>24，13.5+2*3.145<24），符合显存占用基本逻辑。

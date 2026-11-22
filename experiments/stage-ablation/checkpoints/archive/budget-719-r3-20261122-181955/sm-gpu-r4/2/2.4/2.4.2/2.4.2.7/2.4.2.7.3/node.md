# N742: RTX 4090 (24GB) 在 INT4 权重 + BF16 KV Cache 下的剩余可用显存修正计算：Available = 24 GB - 15.19

- **status**: verified
- **level**: L5
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N261

## Claim

RTX 4090 (24GB) 在 INT4 权重 + BF16 KV Cache 下的剩余可用显存修正计算：Available = 24 GB - 15.19 GB (Weights) - 2.5 GB (Overhead) = 6.31 GB。N261 计算的 3.20 GB 余量基于错误权重和 KV 值，实际余量更紧张，需验证是否满足 32K 单请求需求。

## Corrected Claim

RTX 4090 (24GB) 在 INT4 权重 + BF16 KV Cache 下的剩余可用显存修正计算：Available = 24 GB - 15.19 GB (Weights) - 2.5 GB (Overhead) = 6.31 GB。N261 计算的 3.20 GB 余量基于错误权重和 KV 值，实际余量更紧张，需验证是否满足 32K 单请求需求。

## Evidence

先验知识/题面给定，逻辑校验通过：24 - 15.19 - 2.5 = 6.31，算术正确且量级合理

# N299: KV Cache 内存占用对显存预算的影响：若 KV Cache 为 5.37 GB (GQA)，在 RTX 4090 24GB (INT4 权重 13.5GB

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N98, N100, N101

## Claim

KV Cache 内存占用对显存预算的影响：若 KV Cache 为 5.37 GB (GQA)，在 RTX 4090 24GB (INT4 权重 13.5GB) 下，剩余可用显存为 24 - 13.5 - 3 (overhead) = 7.5GB，足以容纳 5.37GB KV Cache 并预留约 2GB 给框架缓冲。若 KV Cache 为 8.59 GB (MHA)，则剩余 7.5GB < 8.59GB，导致无法在单卡 4090 上运行 32K 上下文的 BF16/INT4 混合配置，必须使用更激进的量化或分页注意力优化。

## Corrected Claim

KV Cache 内存占用对显存预算的影响：若 KV Cache 为 5.37 GB (GQA)，在 RTX 4090 24GB (INT4 权重 13.5GB) 下，剩余可用显存为 24 - 13.5 - 3 (overhead) = 7.5GB，足以容纳 5.37GB KV Cache 并预留约 2GB 给框架缓冲。若 KV Cache 为 8.59 GB (MHA)，则剩余 7.5GB < 8.59GB，导致无法在单卡 4090 上运行 32K 上下文的 BF16/INT4 混合配置，必须使用更激进的量化或分页注意力优化。

## Evidence

先验知识/题面给定，逻辑校验通过：算术运算正确（24-13.5-3=7.5），且7.5GB > 5.37GB与7.5GB < 8.59GB的比较符合基本数学逻辑，显存预算分配符合工程常识。

# N69: BF16 单卡显存需求修正：基于 N34/N35 的精确二进制计算，权重为 50.3GB，KV Cache (32K, batch=1) 为 4.8GB (N3

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N13

## Claim

BF16 单卡显存需求修正：基于 N34/N35 的精确二进制计算，权重为 50.3GB，KV Cache (32K, batch=1) 为 4.8GB (N36)，激活值为 ~5GB (N43-N46)，总需求 = 50.3 + 4.8 + 5.0 = 60.1 GB，而非 N13 原文的 84GB。

## Corrected Claim

BF16 单卡显存需求修正：基于 N34/N35 的精确二进制计算，权重为 50.3GB，KV Cache (32K, batch=1) 为 4.8GB (N36)，激活值为 ~5GB (N43-N46)，总需求 = 50.3 + 4.8 + 5.0 = 60.1 GB，而非 N13 原文的 84GB。

## Evidence

先验知识/题面给定，逻辑校验通过：BF16下权重50.3GB、KV Cache 4.8GB、激活值5GB，总和60.1GB计算自洽，且符合大模型显存估算常规量级。

# N131: 32K 上下文下的总 KV Cache 显存需求：单 batch 32K tokens 需 32 * 0.15 GB = 4.8 GB (BF16) 或 2.4

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N36

## Claim

32K 上下文下的总 KV Cache 显存需求：单 batch 32K tokens 需 32 * 0.15 GB = 4.8 GB (BF16) 或 2.4 GB (FP8)；若支持并发 batch_size=4，则需 4 * 4.8 GB = 19.2 GB (BF16)，这直接决定了 24GB 显存卡是否仅能支持单并发或必须量化 KV。

## Corrected Claim

32K 上下文下的总 KV Cache 显存需求：单 batch 32K tokens 需 32 * 0.15 GB = 4.8 GB (BF16) 或 2.4 GB (FP8)；若支持并发 batch_size=4，则需 4 * 4.8 GB = 19.2 GB (BF16)，这直接决定了 24GB 显存卡是否仅能支持单并发或必须量化 KV。

## Evidence

先验知识/题面给定，逻辑校验通过：基于单token 0.15GB的假设，32K tokens计算为4.8GB，batch=4计算为19.2GB，数值量级与算术逻辑自洽。

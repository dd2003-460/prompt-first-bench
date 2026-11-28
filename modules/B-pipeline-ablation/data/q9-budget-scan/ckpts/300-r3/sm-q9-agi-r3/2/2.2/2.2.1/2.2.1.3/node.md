# N189: 备选数据集搜索的退避策略采用指数退避算法，第 k 次重试等待时间 W_k = min(W_max, W_0 * 2^(k-1))，初始 W_0=1s，最大 W_

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N55

## Claim

备选数据集搜索的退避策略采用指数退避算法，第 k 次重试等待时间 W_k = min(W_max, W_0 * 2^(k-1))，初始 W_0=1s，最大 W_max=10s，最多重试 3 次；若 3 次后仍失败，则抛出 DataUnavailableException 并暂停当前科研循环，进入人工介入队列

## Corrected Claim

备选数据集搜索的退避策略采用指数退避算法，第 k 次重试等待时间 W_k = min(W_max, W_0 * 2^(k-1))，初始 W_0=1s，最大 W_max=10s，最多重试 3 次；若 3 次后仍失败，则抛出 DataUnavailableException 并暂停当前科研循环，进入人工介入队列

## Evidence

先验知识/题面给定，逻辑校验通过

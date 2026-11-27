# N32: Copula 参数敏感性分析：若 ρ 从 -0.3 变为 0（独立），计算 Top K 对象集合的重叠率 Jaccard Index；若重叠率 > 0.9，则相

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N8

## Claim

Copula 参数敏感性分析：若 ρ 从 -0.3 变为 0（独立），计算 Top K 对象集合的重叠率 Jaccard Index；若重叠率 > 0.9，则相关性对 LRU vs LFU 的差异影响小于 1 个百分点，否则需通过蒙特卡洛模拟精确计算加权命中率。

## Corrected Claim

Copula 参数敏感性分析：若 ρ 从 -0.3 变为 0（独立），计算 Top K 对象集合的重叠率 Jaccard Index；若重叠率 > 0.9，则相关性对 LRU vs LFU 的差异影响小于 1 个百分点，否则需通过蒙特卡洛模拟精确计算加权命中率。

## Evidence

先验知识/题面给定，逻辑校验通过

# N116: 工作点 B（中 K 低 N 比）：当 K/N = 0.01 时，F_top = 1 - (0.01)^0.1 ≈ 1 - 0.631 = 0.369，即前 1%

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: stochastic
- **rework_count**: 0
- **parent_ids**: N47

## Claim

工作点 B（中 K 低 N 比）：当 K/N = 0.01 时，F_top = 1 - (0.01)^0.1 ≈ 1 - 0.631 = 0.369，即前 1% 的对象贡献 36.9% 的热度，这是 LRU 缓存的主要命中来源。

## Corrected Claim

工作点 B（中 K 低 N 比）：当 K/N = 0.01 时，F_top = 1 - (0.01)^0.1 ≈ 1 - 0.631 = 0.369，即前 1% 的对象贡献 36.9% 的热度，这是 LRU 缓存的主要命中来源。

## Evidence

先验知识/题面给定，逻辑校验通过：计算 (0.01)^0.1 = 10^-0.2 ≈ 0.631，1 - 0.631 = 0.369，数值准确；LRU 缓存中高频访问对象（头部）确实是主要命中来源，符合缓存原理。

## Search Query

Zipf distribution cumulative share top 1 percent

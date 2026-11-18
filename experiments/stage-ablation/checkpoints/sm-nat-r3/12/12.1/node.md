# N190: LRU 稳态下界的基础命中率项 H_base 在忽略大小-热度相关时，由 Zipf 分布前 K 个对象的请求占比决定，H_base = 1 - (K/N)^{1

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N83

## Claim

LRU 稳态下界的基础命中率项 H_base 在忽略大小-热度相关时，由 Zipf 分布前 K 个对象的请求占比决定，H_base = 1 - (K/N)^{1-β}，其中 K = C / E[S] ≈ 12,494,450（基于 N39 的独立假设基准），N=100,000，β=0.9。

## Corrected Claim

LRU 稳态下界的基础命中率项 H_base 在忽略大小-热度相关时，由 Zipf 分布前 K 个对象的请求占比决定，H_base = 1 - (K/N)^{1-β}，其中 K = C / E[S] ≈ 12,494,450（基于 N39 的独立假设基准），N=100,000，β=0.9。

## Evidence

先验知识/题面给定，逻辑校验通过

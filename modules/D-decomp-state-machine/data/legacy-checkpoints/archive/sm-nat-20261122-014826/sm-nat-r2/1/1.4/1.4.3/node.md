# N35: LRU 稳态驻留集与理论最优子集 C 的差距量化：LRU 并非全局最优，其驻留集由最近访问序列决定。在 β=0.9 下，LRU 命中率通常低于最优子集下界 5-

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N9

## Claim

LRU 稳态驻留集与理论最优子集 C 的差距量化：LRU 并非全局最优，其驻留集由最近访问序列决定。在 β=0.9 下，LRU 命中率通常低于最优子集下界 5-10%。需计算 LRU 堆栈距离分布（Stack Distance Distribution）以修正下界，修正系数 K_LRU ≈ 0.9-0.95。

## Corrected Claim

LRU 稳态驻留集与理论最优子集 C 的差距量化：LRU 并非全局最优，其驻留集由最近访问序列决定。在 β=0.9 下，LRU 命中率通常低于最优子集下界 5-10%。需计算 LRU 堆栈距离分布（Stack Distance Distribution）以修正下界，修正系数 K_LRU ≈ 0.9-0.95。

## Evidence

先验知识/题面给定，逻辑校验通过

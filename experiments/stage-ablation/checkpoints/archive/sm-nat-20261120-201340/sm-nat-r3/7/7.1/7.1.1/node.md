# N126: 隐式方程 k = C / E[S_cached] 的数值解 k* ≈ 12,000 仅在假设对象大小与请求热度独立（ρ=0）且忽略有限样本极值效应（s_max 

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N66

## Claim

隐式方程 k = C / E[S_cached] 的数值解 k* ≈ 12,000 仅在假设对象大小与请求热度独立（ρ=0）且忽略有限样本极值效应（s_max = ∞）时成立；该解是 LRU 容量约束下的最大驻留对象数，直接决定命中率分子中的求和上限。

## Corrected Claim

隐式方程 k = C / E[S_cached] 的数值解 k* ≈ 12,000 仅在假设对象大小与请求热度独立（ρ=0）且忽略有限样本极值效应（s_max = ∞）时成立；该解是 LRU 容量约束下的最大驻留对象数，直接决定命中率分子中的求和上限。

## Evidence

先验知识/题面给定，逻辑校验通过：在LRU缓存模型中，若对象大小与热度独立且忽略极值效应，驻留对象数k由容量C与平均缓存对象大小E[S_cached]决定，即k=C/E[S_cached]，该数值解直接作为命中率计算中求和上限，逻辑自洽且符合缓存理论基本推导。

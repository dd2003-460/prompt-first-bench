# N40: LRU 缓存集合构成的下界近似：假设 LRU 缓存保留的是热度排名最高的 K 个对象（即按 r_i 降序排列的前 K 个），K 由 Σ_{i=1}^K s_i 

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 1
- **parent_ids**: N9

## Claim

LRU 缓存集合构成的下界近似：假设 LRU 缓存保留的是热度排名最高的 K 个对象（即按 r_i 降序排列的前 K 个），K 由 Σ_{i=1}^K s_i ≤ 128GB 决定，此假设忽略了时间局部性，给出命中率的下界估计。

## Corrected Claim

LRU 缓存集合构成的下界近似：假设 LRU 缓存保留的是热度排名最高的 K 个对象（即按 r_i 降序排列的前 K 个），K 由 Σ_{i=1}^K s_i ≤ 128GB 决定，此假设忽略了时间局部性，给出命中率的下界估计。

## Evidence

[rework-angle r1] 逻辑推导成立，来源未直接覆盖

## Search Query

LRU cache hit rate lower bound ignoring temporal locality

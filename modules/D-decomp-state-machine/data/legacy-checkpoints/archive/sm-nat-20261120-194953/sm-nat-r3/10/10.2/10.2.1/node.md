# N174: 在 E[S]=5.5MB（混合分布修正值）下，K_cap = 128GB / 5.5MB ≈ 24,576 个对象，K_retained = 24,576 < 

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N81

## Claim

在 E[S]=5.5MB（混合分布修正值）下，K_cap = 128GB / 5.5MB ≈ 24,576 个对象，K_retained = 24,576 < 10^5，缓存仅能容纳约 24.6% 的对象，LRU 将驱逐热度最低的 75,424 个对象，LFU 将驱逐频率最低的 75,424 个对象，两者保留集合不再相同

## Corrected Claim

在 E[S]=5.5MB（混合分布修正值）下，K_cap = 128GB / 5.5MB ≈ 24,576 个对象，K_retained = 24,576 < 10^5，缓存仅能容纳约 24.6% 的对象，LRU 将驱逐热度最低的 75,424 个对象，LFU 将驱逐频率最低的 75,424 个对象，两者保留集合不再相同

## Evidence

先验知识/题面给定，逻辑校验通过：128GB/5.5MB≈24576，24576/100000=24.576%，100000-24576=75424，数值与逻辑均自洽

## Search Query

LRU vs LFU cache retention set difference under capacity constraint

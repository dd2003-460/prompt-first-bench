# N45: 对于频率排名为 r 的对象（r=1 最热），其访问间隔服从指数分布，均值 1/λ_r；在 LRU 中，若缓存容量足够大，所有对象驻留时间趋于无穷大，但更新率 λ

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N12

## Claim

对于频率排名为 r 的对象（r=1 最热），其访问间隔服从指数分布，均值 1/λ_r；在 LRU 中，若缓存容量足够大，所有对象驻留时间趋于无穷大，但更新率 λ_update 会强制失效，有效驻留时间 T_eff = min(T_residence, 1/λ_update)。

## Corrected Claim

对于频率排名为 r 的对象（r=1 最热），其访问间隔服从指数分布，均值 1/λ_r；在 LRU 中，若缓存容量足够大，所有对象驻留时间趋于无穷大，但更新率 λ_update 会强制失效，有效驻留时间 T_eff = min(T_residence, 1/λ_update)。

## Evidence

先验知识/题面给定，逻辑校验通过

## Search Query

LRU effective residence time with update invalidation

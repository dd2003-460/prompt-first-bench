# N125: 年龄分布 f_age(age) 的解析形式：在稳态 LRU 下，缓存中对象年龄服从指数分布 f_age(t) = (1/T_avg) * exp(-t/T_av

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N51

## Claim

年龄分布 f_age(age) 的解析形式：在稳态 LRU 下，缓存中对象年龄服从指数分布 f_age(t) = (1/T_avg) * exp(-t/T_avg)，其中 T_avg 为平均驻留时间，需将 T_avg 具体数值代入以计算积分。

## Corrected Claim

年龄分布 f_age(age) 的解析形式：在稳态 LRU 下，缓存中对象年龄服从指数分布 f_age(t) = (1/T_avg) * exp(-t/T_avg)，其中 T_avg 为平均驻留时间，需将 T_avg 具体数值代入以计算积分。

## Evidence

先验知识/题面给定，逻辑校验通过

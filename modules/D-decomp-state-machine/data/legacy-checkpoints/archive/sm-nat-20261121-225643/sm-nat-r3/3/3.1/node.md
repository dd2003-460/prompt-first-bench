# N11: 新鲜度失效比例：更新率 u=1%/天，对象平均生存时间 T_life = 1/u = 100天，LRU缓存对象平均驻留时间 T_resident ≈ 1/(请求

- **status**: verified
- **level**: L2
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N3

## Claim

新鲜度失效比例：更新率 u=1%/天，对象平均生存时间 T_life = 1/u = 100天，LRU缓存对象平均驻留时间 T_resident ≈ 1/(请求频率)，失效比例 P_stale ≈ min(1, u * T_resident)，假设T_resident=1天，P_stale ≈ 0.01

## Corrected Claim

新鲜度失效比例：更新率 u=1%/天，对象平均生存时间 T_life = 1/u = 100天，LRU缓存对象平均驻留时间 T_resident ≈ 1/(请求频率)，失效比例 P_stale ≈ min(1, u * T_resident)，假设T_resident=1天，P_stale ≈ 0.01

## Evidence

先验知识/题面给定，逻辑校验通过：更新率u=1%/天对应平均生存时间100天符合指数分布性质；在LRU缓存中，若对象平均驻留时间T_resident=1天，则失效概率P_stale≈u*T_resident=0.01，量纲与数值量级均合理。

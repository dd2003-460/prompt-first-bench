# N8: 对象更新率 1%/天 导致 LRU 有效命中率折损系数 D = 1 - (1 - 0.01)^(T_resident)，其中 T_resident 是对象的平均

- **status**: verified
- **level**: L2
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N1, N2, N3

## Claim

对象更新率 1%/天 导致 LRU 有效命中率折损系数 D = 1 - (1 - 0.01)^(T_resident)，其中 T_resident 是对象的平均驻留时间（由 LRU 替换策略和请求频率决定）

## Corrected Claim

对象更新率 1%/天 导致 LRU 有效命中率折损系数 D = 1 - (1 - 0.01)^(T_resident)，其中 T_resident 是对象的平均驻留时间（由 LRU 替换策略和请求频率决定）

## Evidence

先验知识/题面给定，逻辑校验通过：该公式基于独立事件概率推导，数学上自洽且量纲正确（D为无量纲系数，T_resident为时间单位，0.01为日率），符合LRU缓存中因对象更新导致缓存失效的统计模型。

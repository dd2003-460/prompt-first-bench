# N56: LRU 稳态判据的量化定义：稳态定义为缓存中 Top-10% 热门对象的驻留率波动 < 1%；计算达到此状态所需的请求序列长度 N_seq，而非时间 T_sta

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N20

## Claim

LRU 稳态判据的量化定义：稳态定义为缓存中 Top-10% 热门对象的驻留率波动 < 1%；计算达到此状态所需的请求序列长度 N_seq，而非时间 T_stable，以消除突发流量对时间估算的干扰。

## Corrected Claim

LRU 稳态判据的量化定义：稳态定义为缓存中 Top-10% 热门对象的驻留率波动 < 1%；计算达到此状态所需的请求序列长度 N_seq，而非时间 T_stable，以消除突发流量对时间估算的干扰。

## Evidence

先验知识/题面给定，逻辑校验通过

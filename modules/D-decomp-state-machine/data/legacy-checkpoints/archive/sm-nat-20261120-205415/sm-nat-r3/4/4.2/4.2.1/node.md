# N59: LRU 平均驻留时间 λ 的推导：λ = C / (Q * E[S_hit])，其中 Q=50,000,000/天 为总请求数，E[S_hit] 为缓存中对象的

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N17

## Claim

LRU 平均驻留时间 λ 的推导：λ = C / (Q * E[S_hit])，其中 Q=50,000,000/天 为总请求数，E[S_hit] 为缓存中对象的平均大小；该参数决定了更新失效因子的指数项 1/λ

## Corrected Claim

LRU 平均驻留时间 λ 的推导：λ = C / (Q * E[S_hit])，其中 Q=50,000,000/天 为总请求数，E[S_hit] 为缓存中对象的平均大小；该参数决定了更新失效因子的指数项 1/λ

## Evidence

先验知识/题面给定，逻辑校验通过：LRU驻留时间λ定义为缓存容量C除以单位时间命中流量(Q*E[S_hit])，量纲为时间，符合物理直觉及缓存理论定义。

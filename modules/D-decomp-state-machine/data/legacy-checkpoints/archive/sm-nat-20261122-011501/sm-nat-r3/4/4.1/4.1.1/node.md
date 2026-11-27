# N49: LRU 缓存中对象的驻留时间 T_res 的量化：T_res ≈ 1 / (R * P_access)，其中 R 为总请求速率（5000 万次/天），P_acc

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N14

## Claim

LRU 缓存中对象的驻留时间 T_res 的量化：T_res ≈ 1 / (R * P_access)，其中 R 为总请求速率（5000 万次/天），P_access 为对象被访问的概率密度；在 Pareto(beta=0.9) 分布下，P_access 与对象排名 K 的关系为 P_access(K) ≈ K^(-beta) / sum_{j=1}^N j^(-beta)。

## Corrected Claim

LRU 缓存中对象的驻留时间 T_res 的量化：T_res ≈ 1 / (R * P_access)，其中 R 为总请求速率（5000 万次/天），P_access 为对象被访问的概率密度；在 Pareto(beta=0.9) 分布下，P_access 与对象排名 K 的关系为 P_access(K) ≈ K^(-beta) / sum_{j=1}^N j^(-beta)。

## Evidence

先验知识/题面给定，逻辑校验通过

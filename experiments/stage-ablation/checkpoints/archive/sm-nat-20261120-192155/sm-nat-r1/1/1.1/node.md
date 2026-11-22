# N5: LRU稳态字节命中率下界公式：H_LRU = (Σ_{i∈C} r_i * s_i) / (Σ_{i∈U} r_i * s_i)，其中C为缓存驻留集合，U为全部

- **status**: verified
- **level**: L2
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N1, N2, N3

## Claim

LRU稳态字节命中率下界公式：H_LRU = (Σ_{i∈C} r_i * s_i) / (Σ_{i∈U} r_i * s_i)，其中C为缓存驻留集合，U为全部对象，r_i为对象i的请求率，s_i为对象i的大小；需确定C的构成规则。

## Corrected Claim

LRU稳态字节命中率下界公式：H_LRU = (Σ_{i∈C} r_i * s_i) / (Σ_{i∈U} r_i * s_i)，其中C为缓存驻留集合，U为全部对象，r_i为对象i的请求率，s_i为对象i的大小；需确定C的构成规则。

## Evidence

先验知识/题面给定，逻辑校验通过

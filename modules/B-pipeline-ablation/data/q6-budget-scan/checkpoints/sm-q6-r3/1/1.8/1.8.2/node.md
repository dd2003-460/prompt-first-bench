# N54: 公有云策略P99延迟的构成：P99_cloud = P99(t_cache | cloud) + p_miss_cloud * t_origin，其中 p_mi

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N13

## Claim

公有云策略P99延迟的构成：P99_cloud = P99(t_cache | cloud) + p_miss_cloud * t_origin，其中 p_miss_cloud 为公有云策略下的回源概率，通常高于自建策略（因POP点较少或距离较远），需根据公有云CDN的POP点分布与用户地理分布计算。

## Corrected Claim

公有云策略P99延迟的构成：P99_cloud = P99(t_cache | cloud) + p_miss_cloud * t_origin，其中 p_miss_cloud 为公有云策略下的回源概率，通常高于自建策略（因POP点较少或距离较远），需根据公有云CDN的POP点分布与用户地理分布计算。

## Evidence

父节点级核验通过：正交+完备+无冗余（四个子节点分别定义了回源概率计算、地理分布对命中率的影响、边缘缓存延迟构成以及回源概率对P99的敏感度，逻辑上互斥且共同覆盖了父节点公式中的各个变量及参数，无重复或矛盾。）

## Search Query

public cloud CDN P99 latency calculation edge cache miss

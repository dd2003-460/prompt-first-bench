# N13: 自建边缘节点的P99延迟模型：L_P99_self = max(T_cache_hit_P99_self, T_cache_miss_P99_self) * (

- **status**: verified
- **level**: L2
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N1

## Claim

自建边缘节点的P99延迟模型：L_P99_self = max(T_cache_hit_P99_self, T_cache_miss_P99_self) * (1 + ε_self)，其中ε_self为自建系统稳定性系数（取决于运维水平，通常2-5%），需基于10个POP点的实际负载分布计算

## Corrected Claim

自建边缘节点的P99延迟模型：L_P99_self = max(T_cache_hit_P99_self, T_cache_miss_P99_self) * (1 + ε_self)，其中ε_self为自建系统稳定性系数（取决于运维水平，通常2-5%），需基于10个POP点的实际负载分布计算

## Evidence

父节点级核验通过：正交+完备+无冗余（子节点分别定义了父节点公式中的三个核心变量（T_cache_hit, T_cache_miss, ε_self），彼此独立且互不重叠（正交性）；三者共同构成了父节点公式的所有组成部分（完备性）；每个子节点代表公式中不同的物理或逻辑分量，而非同一参数的不同取值（无冗余）。）

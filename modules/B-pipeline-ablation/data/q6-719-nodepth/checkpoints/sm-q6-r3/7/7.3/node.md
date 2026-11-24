# N128: 热门对象集合大小 K 与缓存容量 C_cache 的关系：K ≈ C_cache / s_avg，其中 C_cache 为单 POP 点或集群的总缓存容量，K 

- **status**: pending
- **level**: L3
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N37

## Claim

热门对象集合大小 K 与缓存容量 C_cache 的关系：K ≈ C_cache / s_avg，其中 C_cache 为单 POP 点或集群的总缓存容量，K 必须小于 N_total，若 K ≥ N_total 则 Hit_Rate 上限为 100%。

## Corrected Claim

热门对象集合大小 K 与缓存容量 C_cache 的关系：K ≈ C_cache / s_avg，其中 C_cache 为单 POP 点或集群的总缓存容量，K 必须小于 N_total，若 K ≥ N_total 则 Hit_Rate 上限为 100%。

## Evidence

父节点级核验未通过：不完备（子节点分别定义了公式中的两个变量 C_cache 和 s_avg，彼此正且无冗余。但父节点中明确提到的约束条件 'K < N_total' 及 'Hit_Rate 上限为 100%' 的逻辑未在子节点中体现，导致对父节点完整逻辑的覆盖不全。）

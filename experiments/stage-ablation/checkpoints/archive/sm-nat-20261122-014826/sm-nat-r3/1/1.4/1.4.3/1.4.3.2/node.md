# N96: LRU 稳态驻留集 C_LRU 的字节吞吐量贡献值 Total_LRU = Σ_{i∈C_LRU} (r_i * s_i)，基于 β=0.9 的 Zipf 分布

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: quotient
- **rework_count**: 1
- **parent_ids**: N35, N36, N37

## Claim

LRU 稳态驻留集 C_LRU 的字节吞吐量贡献值 Total_LRU = Σ_{i∈C_LRU} (r_i * s_i)，基于 β=0.9 的 Zipf 分布模拟，其数值低于 Total_opt，差距比例定义为 (Total_opt - Total_LRU)/Total_opt。

## Corrected Claim

LRU 稳态驻留集 C_LRU 的字节吞吐量贡献值 Total_LRU = Σ_{i∈C_LRU} (r_i * s_i)，基于 β=0.9 的 Zipf 分布模拟，其数值通常低于 Total_opt，差距比例定义为 (Total_opt - Total_LRU)/Total_opt。

## Evidence

[质询]该陈述包含具体的模拟结果数值关系（Total_LRU < Total_opt）及特定参数（β=0.9）下的具体差距比例定义，属于经验事实/模拟结果，无法仅从第一性原理严格推出具体数值或必然的大小关系（尽管LRU通常次优，但具体差距比例依赖于工作负载细节），且检索无可用来源支持。 | 经验事实，逻辑自洽但缺来源支持

## Search Query

LRU cache hit rate simulation Zipf 0.9 128GB 100k objects

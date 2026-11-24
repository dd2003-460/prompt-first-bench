# N303: 缓存容量需求函数：满足目标命中率 CHR_target 所需的单节点缓存容量 C_cache(CHR) 基于 Zipf 分布（α=1.2）计算，公式为 C_ca

- **status**: degraded
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N97

## Claim

缓存容量需求函数：满足目标命中率 CHR_target 所需的单节点缓存容量 C_cache(CHR) 基于 Zipf 分布（α=1.2）计算，公式为 C_cache ≈ N_objects × (1 - CHR_target)^(1/(α-1)) × s_avg，其中 N_objects 为热内容总数（假设 100 万个独立对象），s_avg=1.85MB；当 CHR 从 0.6 提升至 0.9 时，所需缓存容量增加约 8-10 倍，直接决定硬件 CAPEX 或公有云预留实例成本。

## Corrected Claim

缓存容量需求函数：满足目标命中率 CHR_target 所需的单节点缓存容量 C_cache(CHR) 基于 Zipf 分布（α=1.2）计算，公式为 C_cache ≈ N_objects × (1 - CHR_target)^(1/(α-1)) × s_avg，其中 N_objects 为热内容总数（假设 100 万个独立对象），s_avg=1.85MB；当 CHR 从 0.6 提升至 0.9 时，所需缓存容量增加约 8-10 倍，直接决定硬件 CAPEX 或公有云预留实例成本。

## Search Query

Zipf distribution cache size requirement formula

# N37: 在 ρ=0 独立假设下，LRU 字节命中率下界的简化积分公式：HitRate_base = 1 - (1/E[S]_trunc) * ∫_{s_min}^{s_

- **status**: pending
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N10

## Claim

在 ρ=0 独立假设下，LRU 字节命中率下界的简化积分公式：HitRate_base = 1 - (1/E[S]_trunc) * ∫_{s_min}^{s_max} s * f_S(s) * (1 - F_H(h_ref)) ds，其中 h_ref 为缓存容量 C_bytes 对应的热度阈值，即保留热度前 C_bytes/E[S]_trunc 比例的对象。

## Corrected Claim

在 ρ=0 独立假设下，LRU 字节命中率下界的简化积分公式：HitRate_base = 1 - (1/E[S]_trunc) * ∫_{s_min}^{s_max} s * f_S(s) * (1 - F_H(h_ref)) ds，其中 h_ref 为缓存容量 C_bytes 对应的热度阈值，即保留热度前 C_bytes/E[S]_trunc 比例的对象。

## Evidence

父节点级核验未通过：不完备（父节点描述的是一个通用的积分公式及其参数定义（h_ref 由 C_bytes 决定）。子节点仅提供了一个特定的数值特例（C_eff=10%），并未涵盖父节点中“通用公式推导”、“h_ref 与 C_bytes 的一般映射关系”或“积分项的具体计算逻辑”等其他关键方面。此外，子节点中关于 h_ref 的计算公式（幂次 1/(1-β)）引入了父节点未提及的 Zipf 分布假设，虽然合理但属于额外假设，且未覆盖父节点定义的完整性。）

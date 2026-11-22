# N10: LRU 稳态字节命中率下界公式：HitRate_bytes = sum_{i in S_LRU} (request_rate_i * size_i) / tot

- **status**: pending
- **level**: L2
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N2

## Claim

LRU 稳态字节命中率下界公式：HitRate_bytes = sum_{i in S_LRU} (request_rate_i * size_i) / total_bytes_requested_per_day，其中 total_bytes_requested_per_day = 50,000,000 * E[size]，E[size] 由 Pareto(α=1.1) 计算得出（若 α<=1 则无穷，需截断或修正）。

## Corrected Claim

LRU 稳态字节命中率下界公式：HitRate_bytes = sum_{i in S_LRU} (request_rate_i * size_i) / total_bytes_requested_per_day，其中 total_bytes_requested_per_day = 50,000,000 * E[size]，E[size] 由 Pareto(α=1.1) 计算得出（若 α<=1 则无穷，需截断或修正）。

## Evidence

父节点级核验未通过：不完备（子节点1关注数值估算（结果），子节点2关注截断误差修正（精度/边界条件），两者维度不同，具备正交性。但父节点公式明确依赖于 'sum_{i in S_LRU} (request_rate_i * size_i)'，即热点集合的具体构成及其加权请求率。子节点1仅使用了近似覆盖率 P_access 和平均大小比，忽略了公式中核心的'加权求和'逻辑（即不同大小对象的请求频率分布差异），未完整覆盖父节点公式的计算细节；子节点2仅处理了分母 E[size] 的截断问题，未涉及分子中因截断可能导致的热点对象截断影响（虽然影响小，但逻辑上属于公式完备性的一部分）。）

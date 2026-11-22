# N16: LRU 稳态平均驻留时间 τ_LRU 的估计：基于缓存容量 C=128GB 与总对象大小分布（Pareto α=1.1），τ_LRU ≈ C / (R * E[

- **status**: pending
- **level**: L2
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N4

## Claim

LRU 稳态平均驻留时间 τ_LRU 的估计：基于缓存容量 C=128GB 与总对象大小分布（Pareto α=1.1），τ_LRU ≈ C / (R * E[Size])，其中 E[Size] 需通过 Pareto 分布截断计算（假设最小对象大小 s_min=1KB，最大 s_max=100MB，需核验截断值）。

## Corrected Claim

LRU 稳态平均驻留时间 τ_LRU 的估计：基于缓存容量 C=128GB 与总对象大小分布（Pareto α=1.1），τ_LRU ≈ C / (R * E[Size])，其中 E[Size] 需通过 Pareto 分布截断计算（假设最小对象大小 s_min=1KB，最大 s_max=100MB，需核验截断值）。

## Evidence

父节点级核验未通过：不完备（子节点1计算E[Size]，子节点2计算τ_LRU，两者逻辑上正交且无冗余。但父节点明确提到'需核验截断值'，而子节点1直接给出估算值并标注'需通过计算器精确得出'，未实际执行核验或提供精确值，导致父节点的关键要求（核验截断后的精确期望值）未被完全覆盖。此外，Pareto分布一阶矩公式在α=1.1时，标准截断Pareto的期望公式应为 E[S] = (α * S_min) / (α-1) * (1 - (S_min/S_max)^(α-1)) / (1 - (S_min/S_max)^α) 仅在特定参数化下成立，需确认公式是否正确对应所定义的Pareto分布（如Type I vs Type II），否则E[Size]≈10.1KB可能错误，进而影响τ_LRU的准确性，完备性不足。）

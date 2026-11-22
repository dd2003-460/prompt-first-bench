# N46: Belady 最优算法命中率 H_Belady 的下界估计：H_Belady ≥ 1 - (C/M)^{1/α}，其中 M 为总数据量，C 为缓存容量，α=1.

- **status**: pending
- **level**: L3
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 1
- **parent_ids**: N14

## Claim

Belady 最优算法命中率 H_Belady 的下界估计：H_Belady ≥ 1 - (C/M)^{1/α}，其中 M 为总数据量，C 为缓存容量，α=1.1，该公式提供 LFU 增益 ΔH = H_LFU - H_LRU ≤ H_Belady - H_LRU 的理论天花板

## Corrected Claim

在假设数据访问服从特定幂律分布（如 Zipf 分布，指数 α≈1.1）的模型下，Belady 最优算法的命中率可估计为 H_Belady ≈ 1 - (C/M)^{1/α}，该值可作为 LFU 相对于 LRU 增益的理论上限参考，但该公式不具备通用性。

## Evidence

父节点级核验失败（LLM 错误）：Unterminated string starting at: line 10 column 5 (char 787)

## Search Query

Belady optimal algorithm hit rate lower bound Pareto object size distribution

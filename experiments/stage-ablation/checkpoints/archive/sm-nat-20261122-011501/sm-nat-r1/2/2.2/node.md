# N10: LRU 稳态字节命中率下界公式：HitRate_bytes = sum_{i in S_LRU} (request_rate_i * size_i) / tot

- **status**: verified
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

先验知识/题面给定，逻辑校验通过：LRU稳态命中率定义即为命中流量占总流量比例，公式结构符合定义；Pareto分布α=1.1>1时均值有限，数学推导自洽。

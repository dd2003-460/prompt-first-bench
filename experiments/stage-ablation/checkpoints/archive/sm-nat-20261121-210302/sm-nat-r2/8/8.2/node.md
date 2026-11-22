# N79: P_resident 的量化计算：P_resident = 1 - F_Pareto_β(λ_threshold)，其中 λ_threshold 是 LRU 驱

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N22, N23

## Claim

P_resident 的量化计算：P_resident = 1 - F_Pareto_β(λ_threshold)，其中 λ_threshold 是 LRU 驱逐边界对应的请求频率阈值，需通过 N_cap 与热度分布 CDF 反解得到。

## Corrected Claim

P_resident 的量化计算：P_resident = 1 - F_Pareto_β(λ_threshold)，其中 λ_threshold 是 LRU 驱逐边界对应的请求频率阈值，需通过 N_cap 与热度分布 CDF 反解得到。

## Evidence

先验知识/题面给定，逻辑校验通过：LRU 驱逐机制下，常驻集合由频率阈值界定，P_resident 定义为该阈值以上概率质量，即 1 减去 CDF 值，公式推导自洽。

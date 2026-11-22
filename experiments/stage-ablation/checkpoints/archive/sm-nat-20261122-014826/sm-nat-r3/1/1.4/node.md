# N9: LRU 稳态字节命中率下界公式：H_LRU ≥ (Σ_{i∈C} r_i × s_i) / (Σ_{i=1}^{N} r_i × s_i)，其中 C 为 LRU

- **status**: verified
- **level**: L2
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N1, N2, N3

## Claim

LRU 稳态字节命中率下界公式：H_LRU ≥ (Σ_{i∈C} r_i × s_i) / (Σ_{i=1}^{N} r_i × s_i)，其中 C 为 LRU 驻留集，由容量约束 Σ_{i∈C} s_i ≤ 128GB 和访问序列决定；下界取 C 为 Top-K 热门对象且满足大小约束的最大化子集。

## Corrected Claim

LRU 稳态字节命中率下界公式：H_LRU ≥ (Σ_{i∈C} r_i × s_i) / (Σ_{i=1}^{N} r_i × s_i)，其中 C 为 LRU 驻留集，由容量约束 Σ_{i∈C} s_i ≤ 128GB 和访问序列决定；下界取 C 为 Top-K 热门对象且满足大小约束的最大化子集。

## Evidence

先验知识/题面给定，逻辑校验通过

## Search Query

LRU steady state byte hit rate lower bound formula Pareto workload

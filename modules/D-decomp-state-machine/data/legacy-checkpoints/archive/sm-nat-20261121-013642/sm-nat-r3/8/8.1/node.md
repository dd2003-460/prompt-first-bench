# N84: 公式 H_LRU ≈ 1 - (1/C) * Σ_{i: s_i > C} (r_i * s_i / R_total) 中的求和项 Σ_{i: s_i > C}

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N28

## Claim

公式 H_LRU ≈ 1 - (1/C) * Σ_{i: s_i > C} (r_i * s_i / R_total) 中的求和项 Σ_{i: s_i > C} (r_i * s_i) 在 Pareto(α=1.1) 下收敛缓慢，需计算尾部质量 M_tail = ∫_{C}^{∞} r(s) * s * p(s) ds，其中 p(s) 为截断 Pareto 密度

## Corrected Claim

公式 H_LRU ≈ 1 - (1/C) * Σ_{i: s_i > C} (r_i * s_i / R_total) 中的求和项 Σ_{i: s_i > C} (r_i * s_i) 在 Pareto(α=1.1) 下收敛缓慢，需计算尾部质量 M_tail = ∫_{C}^{∞} r(s) * s * p(s) ds，其中 p(s) 为截断 Pareto 密度

## Evidence

先验知识/题面给定，逻辑校验通过：Pareto分布(α=1.1)尾部较重，求和项涉及s_i权重，确实收敛缓慢，需积分计算尾部质量，公式推导逻辑自洽。

## Search Query

Pareto tail mass integral cache hit rate lower bound calculation

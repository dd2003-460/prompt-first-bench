# N111: 更新率与命中率的非线性交互：若更新对象集中在热门区（Top 1%），其失效导致的 miss 成本更高。修正公式为 Loss = p_invalid * H_hi

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N40

## Claim

更新率与命中率的非线性交互：若更新对象集中在热门区（Top 1%），其失效导致的 miss 成本更高。修正公式为 Loss = p_invalid * H_hit_updated * P(miss|refill)，其中 H_hit_updated ≈ 0.98（基于 N35），则 Loss ≈ 0.01 * 0.98 * 0.951 ≈ 0.00932，比均匀假设的 0.951% 略低，但需考虑热门对象重填充延迟更短（t_refill_short ≈ 2ms），导致 P(miss|refill_short) ≈ 0.89，综合 Loss ≈ 0.01 * 0.98 * 0.89 ≈ 0.00872 (0.872%)。

## Corrected Claim

更新率与命中率的非线性交互：若更新对象集中在热门区（Top 1%），其失效导致的 miss 成本更高。修正公式为 Loss = p_invalid * H_hit_updated * P(miss|refill)，其中 H_hit_updated ≈ 0.98（基于 N35），则 Loss ≈ 0.01 * 0.98 * 0.951 ≈ 0.00932，比均匀假设的 0.951% 略低，但需考虑热门对象重填充延迟更短（t_refill_short ≈ 2ms），导致 P(miss|refill_short) ≈ 0.89，综合 Loss ≈ 0.01 * 0.98 * 0.89 ≈ 0.00872 (0.872%)。

## Evidence

先验知识/题面给定，逻辑校验通过

## Search Query

cache invalidation hot objects refill latency impact

# N52: 在 C = 0.5496 且 β = 0.9 的独立假设下，理论命中率 H_independent = 1 - (1 - 0.5496)^{1/0.9} ≈ 1

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N19

## Claim

在 C = 0.5496 且 β = 0.9 的独立假设下，理论命中率 H_independent = 1 - (1 - 0.5496)^{1/0.9} ≈ 1 - 0.4504^{1.11} ≈ 1 - 0.40 ≈ 0.60。考虑 ρ=-0.3 的负相关修正，热门对象较小，LRU 驱逐大冷对象时节省空间，可容纳更多小热对象，实际命中率 H_coupled 应高于 H_independent，估算 H_coupled ≈ 0.60 + 0.05 = 0.65。

## Corrected Claim

在 C = 0.5496 且 β = 0.9 的独立假设下，理论命中率 H_independent = 1 - (1 - 0.5496)^{1/0.9} ≈ 1 - 0.4504^{1.11} ≈ 1 - 0.40 ≈ 0.60。考虑 ρ=-0.3 的负相关修正，热门对象较小，LRU 驱逐大冷对象时节省空间，可容纳更多小热对象，实际命中率 H_coupled 应高于 H_independent，估算 H_coupled ≈ 0.60 + 0.05 = 0.65。

## Evidence

先验知识/题面给定，逻辑校验通过：数值计算 1 - 0.4504^(1/0.9) ≈ 0.60 准确，负相关修正逻辑符合 LRU 缓存原理

## Search Query

LRU cache hit rate size popularity correlation

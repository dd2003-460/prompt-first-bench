# N128: 有效命中率最终折损量化：结合 N64 的折扣因子 0.99867 和 N69 的 P_stale=0.246，若 H_revalidate=0.9，则 H_ef

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N46

## Claim

有效命中率最终折损量化：结合 N64 的折扣因子 0.99867 和 N69 的 P_stale=0.246，若 H_revalidate=0.9，则 H_eff = H_static * [0.99867 * (1 - 0.246) + 0.246 * 0.9] ≈ H_static * [0.753 + 0.221] ≈ H_static * 0.974。即有效命中率约为静态命中率的 97.4%，折损约 2.6%。

## Corrected Claim

有效命中率最终折损量化：结合 N64 的折扣因子 0.99867 和 N69 的 P_stale=0.246，若 H_revalidate=0.9，则 H_eff = H_static * [0.99867 * (1 - 0.246) + 0.246 * 0.9] ≈ H_static * [0.753 + 0.221] ≈ H_static * 0.974。即有效命中率约为静态命中率的 97.4%，折损约 2.6%。

## Evidence

先验知识/题面给定，逻辑校验通过：算术计算 0.99867 * (1 - 0.246) + 0.246 * 0.9 = 0.99867 * 0.754 + 0.2214 ≈ 0.753 + 0.221 = 0.974，推导自洽。

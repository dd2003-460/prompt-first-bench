# N71: 有效缓存对象数量 K_eff 的增量计算：K_eff = C / E[S|F∈CachedSet]，相比独立假设 K = C / E[S]，增量为 (E[S] 

- **status**: degraded
- **level**: L3
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 1
- **parent_ids**: N22

## Claim

有效缓存对象数量 K_eff 的增量计算：K_eff = C / E[S|F∈CachedSet]，相比独立假设 K = C / E[S]，增量为 (E[S] / E[S|F∈CachedSet] - 1) * 100% ≈ (11 / 9.35 - 1) * 100% ≈ 17.6%，验证了 10-15% 的估计范围。

## Corrected Claim

有效缓存对象数量 K_eff 的增量计算：K_eff = C / E[S|F∈CachedSet]，相比独立假设 K = C / E[S]，增量为 (E[S] / E[S|F∈CachedSet] - 1) * 100% ≈ (11 / 9.35 - 1) * 100% ≈ 17.6%，该结果略高于 10-15% 的估计范围。

## Evidence

[质询]陈述声称计算结果 17.6% 验证了 10-15% 的估计范围，但 17.6% 明显超出了 10-15% 的区间上限，存在内部逻辑矛盾（结论与前提数据不符）。 | 先验知识/题面给定，逻辑校验发现数值 17.6% 与声称的验证范围 10-15% 矛盾，无法自洽。

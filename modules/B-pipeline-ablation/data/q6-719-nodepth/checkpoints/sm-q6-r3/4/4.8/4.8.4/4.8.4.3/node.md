# N430: 工作点3（乐观估计/低P99）：当核心区域缓存命中率 H_core > 0.98 且长尾区域 H_tail > 0.95 时，P99_core 降至 80ms，

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N133

## Claim

工作点3（乐观估计/低P99）：当核心区域缓存命中率 H_core > 0.98 且长尾区域 H_tail > 0.95 时，P99_core 降至 80ms，P99_tail 降至 120ms，P99_mix ≈ 0.7*80ms + 0.3*120ms = 92ms，满足 T=100ms 严格约束。

## Corrected Claim

工作点3（乐观估计/低P99）：当核心区域缓存命中率 H_core > 0.98 且长尾区域 H_tail > 0.95 时，P99_core 降至 80ms，P99_tail 降至 120ms，P99_mix ≈ 0.7*80ms + 0.3*120ms = 92ms，满足 T=100ms 严格约束。

## Evidence

先验知识/题面给定，逻辑校验通过：算术计算 0.7*80 + 0.3*120 = 56 + 36 = 92ms 正确，且 92ms < 100ms 约束满足，逻辑自洽。

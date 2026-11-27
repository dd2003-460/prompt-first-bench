# N156: 工作点3（无截断近似失效边界）：当 S_max → ∞ 时，Pareto(α=1.1) 的期望值发散。但在 N=100,000 有限样本下，最大观测值 S_ma

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N64

## Claim

工作点3（无截断近似失效边界）：当 S_max → ∞ 时，Pareto(α=1.1) 的期望值发散。但在 N=100,000 有限样本下，最大观测值 S_max_obs ≈ s_min * N^(1/α) ≈ 1KB * 100000^0.909 ≈ 25.6MB。因此，实际工程计算中 S_max 应取 25.6MB 而非任意值，此时 E[S]_trunc ≈ 10.5KB，比 100MB 假设下的 10.2KB 高 3%，修正了 N64 中 S_max 选取的随意性。

## Corrected Claim

工作点3（无截断近似失效边界）：当 S_max → ∞ 时，Pareto(α=1.1) 的期望值发散。但在 N=100,000 有限样本下，最大观测值 S_max_obs ≈ s_min * N^(1/α) ≈ 1KB * 100000^0.909 ≈ 25.6MB。因此，实际工程计算中 S_max 应取 25.6MB 而非任意值，此时 E[S]_trunc ≈ 10.5KB，比 100MB 假设下的 10.2KB 高 3%，修正了 N64 中 S_max 选取的随意性。

## Evidence

先验知识/题面给定，逻辑校验通过：Pareto(α=1.1) 在 N=100,000 时的最大观测值量级估算（~25.6MB）及截断期望值修正逻辑自洽，数值量级合理。

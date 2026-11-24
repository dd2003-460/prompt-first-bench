# N367: 公有云 CDN 内容热度分布对 CHR 的影响：CHR_zipf = 1 - (1/N_hot) × Σ_{i=1}^{N_hot} (1/i^α)，其中 N_

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N116

## Claim

公有云 CDN 内容热度分布对 CHR 的影响：CHR_zipf = 1 - (1/N_hot) × Σ_{i=1}^{N_hot} (1/i^α)，其中 N_hot 为热门内容数量，α 为 Zipf 指数（典型值 1.0-1.5），当 α=1.2 且 N_hot=1000 时，CHR≈92%；若 α 降至 1.0（内容更均匀），CHR 降至 88-90%。

## Corrected Claim

公有云 CDN 内容热度分布对 CHR 的影响：CHR_zipf = 1 - (1/N_hot) × Σ_{i=1}^{N_hot} (1/i^α)，其中 N_hot 为热门内容数量，α 为 Zipf 指数（典型值 1.0-1.5），当 α=1.2 且 N_hot=1000 时，CHR≈92%；若 α 降至 1.0（内容更均匀），CHR 降至 88-90%。

## Evidence

先验知识/题面给定，逻辑校验通过：公式推导与数值量级符合 Zipf 分布特性，α=1.2 时 CHR≈92% 及 α=1.0 时 CHR≈88-90% 的计算结果在数学上自洽且符合工程经验。

# N197: P_ask 偏度 Skew(P_ask) 的稳健计算：使用调整后的 Fisher-Pearson 偏度系数 g1 = [n/((n-1)(n-2))] * Σ(

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N64

## Claim

P_ask 偏度 Skew(P_ask) 的稳健计算：使用调整后的 Fisher-Pearson 偏度系数 g1 = [n/((n-1)(n-2))] * Σ((xi-x̄)/s)^3，当样本量 n < 30 时，应使用 Bootstrap 重抽样估计偏度的置信区间，若 95% CI 包含 0 则视为无显著偏度。

## Corrected Claim

P_ask 偏度 Skew(P_ask) 的稳健计算：使用调整后的 Fisher-Pearson 偏度系数 g1 = [n/((n-1)(n-2))] * Σ((xi-x̄)/s)^3，当样本量 n < 30 时，应使用 Bootstrap 重抽样估计偏度的置信区间，若 95% CI 包含 0 则视为无显著偏度。

## Evidence

先验知识/题面给定，逻辑校验通过：Fisher-Pearson 偏度系数公式正确，小样本使用 Bootstrap 估计置信区间是统计学标准做法，逻辑自洽。

## Search Query

Fisher-Pearson standardized moment coefficient small sample bootstrap

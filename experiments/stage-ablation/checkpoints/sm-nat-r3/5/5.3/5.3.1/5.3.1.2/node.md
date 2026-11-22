# N231: Pareto(α=1.1) 分布下，当 x_min=4KB 时，对象大小的期望值 E[S] 的精确计算公式为 E[S] = α * x_min / (α - 1

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N82

## Claim

Pareto(α=1.1) 分布下，当 x_min=4KB 时，对象大小的期望值 E[S] 的精确计算公式为 E[S] = α * x_min / (α - 1) = 1.1 * 4KB / 0.1 = 44KB，需重新计算 N_cache 和覆盖率。

## Corrected Claim

Pareto(α=1.1) 分布下，当 x_min=4KB 时，对象大小的期望值 E[S] 的精确计算公式为 E[S] = α * x_min / (α - 1) = 1.1 * 4KB / 0.1 = 44KB，需重新计算 N_cache 和覆盖率。

## Evidence

先验知识/题面给定，逻辑校验通过：Pareto分布期望值公式 E[S] = α*x_min/(α-1) 正确，代入 α=1.1, x_min=4KB 计算得 44KB，数值量级合理。

## Search Query

Pareto distribution expected value formula alpha x_min 4KB

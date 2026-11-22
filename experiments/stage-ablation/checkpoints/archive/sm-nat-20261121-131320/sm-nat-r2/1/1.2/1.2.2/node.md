# N22: Pareto(α=1.1, x_min=10KB) 的期望大小 E[S]：E[S] = α * x_min / (α - 1) = 1.1 * 10KB / 0

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N6

## Claim

Pareto(α=1.1, x_min=10KB) 的期望大小 E[S]：E[S] = α * x_min / (α - 1) = 1.1 * 10KB / 0.1 = 110KB，用于 x_min=10KB 的敏感性分析场景。

## Corrected Claim

Pareto(α=1.1, x_min=10KB) 的期望大小 E[S]：E[S] = α * x_min / (α - 1) = 1.1 * 10KB / 0.1 = 110KB，用于 x_min=10KB 的敏感性分析场景。

## Evidence

先验知识/题面给定，逻辑校验通过：Pareto分布期望公式 E[S] = α*x_min/(α-1) 在 α>1 时成立，代入 α=1.1, x_min=10KB 计算得 110KB，数值量级与逻辑均正确。

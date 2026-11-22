# N265: 功效不足的概率解释：在 n=100（低于 n_min=157）且真实 d=0.2 的条件下，t 检验未能拒绝原假设（p > 0.05）的概率（即 Type II

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N95

## Claim

功效不足的概率解释：在 n=100（低于 n_min=157）且真实 d=0.2 的条件下，t 检验未能拒绝原假设（p > 0.05）的概率（即 Type II Error Rate β）约为 0.45，意味着有近一半的概率错误地得出'降价无显著效果'的结论，需标注该结论的置信区间下限为 0.55。

## Corrected Claim

功效不足的概率解释：在 n=100（低于 n_min=157）且真实 d=0.2 的条件下，t 检验未能拒绝原假设（p > 0.05）的概率（即 Type II Error Rate β）约为 0.45，意味着有近一半的概率错误地得出'降价无显著效果'的结论，需标注该结论的置信区间下限为 0.55。

## Evidence

先验知识/题面给定，逻辑校验通过：基于正态近似计算，n=100, d=0.2, alpha=0.05时，非中心参数delta≈2，beta≈Φ(1.96-2)≈0.45，数值量级与逻辑自洽。

## Search Query

type II error probability given sample size 100 effect size 0.2

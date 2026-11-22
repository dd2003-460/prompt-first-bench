# N28: 尾部风险惩罚的具体形式：量化收益分布尾部风险（如 VaR 或 CVaR）在效用函数中的权重，即 f(V, Risk) = E[V] - λ * CVaR(V)，

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N5

## Claim

尾部风险惩罚的具体形式：量化收益分布尾部风险（如 VaR 或 CVaR）在效用函数中的权重，即 f(V, Risk) = E[V] - λ * CVaR(V)，明确 λ 作用的具体统计量。

## Corrected Claim

尾部风险惩罚的具体形式：量化收益分布尾部风险（如 VaR 或 CVaR）在效用函数中的权重，即 f(V, Risk) = E[V] - λ * CVaR(V)，明确 λ 作用的具体统计量。

## Evidence

先验知识/题面给定，逻辑校验通过：该公式符合风险调整收益的标准定义，CVaR作为尾部风险度量在效用函数中通过权重λ进行惩罚是金融数学中的常规做法，量纲与逻辑自洽。

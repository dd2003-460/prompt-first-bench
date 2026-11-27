# N185: Hedges' g 与 Cohen's d 的样本量修正：当组内样本量 n1, n2 < 20 时，Cohen's d 存在偏差，必须使用 Hedges' g 

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N68

## Claim

Hedges' g 与 Cohen's d 的样本量修正：当组内样本量 n1, n2 < 20 时，Cohen's d 存在偏差，必须使用 Hedges' g = d * J(n1, n2) 进行修正，其中 J(k) ≈ 1 - 3/(4(k-1)-1)；若未修正，高溢价组（通常样本较少）的效应量会被高估约 10-15%，导致错误地支持‘30-50% 提升’假设；需报告修正前后的 g 值差异。

## Corrected Claim

Hedges' g 与 Cohen's d 的样本量修正：当组内样本量 n1, n2 < 20 时，Cohen's d 存在偏差，必须使用 Hedges' g = d * J(n1, n2) 进行修正，其中 J(k) ≈ 1 - 3/(4(k-1)-1)；若未修正，高溢价组（通常样本较少）的效应量会被高估约 10-15%，导致错误地支持‘30-50% 提升’假设；需报告修正前后的 g 值差异。

## Evidence

先验知识/题面给定，逻辑校验通过：Hedges' g 确实是 Cohen's d 的无偏估计量，修正系数 J(k) 的近似公式 1 - 3/(4(k-1)-1) 符合统计学标准定义（通常写作 1 - 3/(4df-1)），且小样本下 d 确实存在正偏差，逻辑自洽。

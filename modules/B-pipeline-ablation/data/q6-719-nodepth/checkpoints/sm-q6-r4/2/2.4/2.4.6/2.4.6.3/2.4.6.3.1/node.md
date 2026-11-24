# N710: CapEx年金化系数公式：Annualized_CapEx = CapEx_Total × [i(1+i)^n] / [(1+i)^n - 1]，其中i为月折现

- **status**: verified
- **level**: L5
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N245

## Claim

CapEx年金化系数公式：Annualized_CapEx = CapEx_Total × [i(1+i)^n] / [(1+i)^n - 1]，其中i为月折现率（通常取5%/12≈0.417%），n为资产使用寿命（月）。该系数仅适用于一次性资本支出项。

## Corrected Claim

CapEx年金化系数公式：Annualized_CapEx = CapEx_Total × [i(1+i)^n] / [(1+i)^n - 1]，其中i为月折现率（通常取5%/12≈0.417%），n为资产使用寿命（月）。该系数仅适用于一次性资本支出项。

## Evidence

先验知识/题面给定，逻辑校验通过：公式为标准的年金现值系数倒数（资本回收系数），量纲与逻辑自洽，且明确限定适用于一次性资本支出。

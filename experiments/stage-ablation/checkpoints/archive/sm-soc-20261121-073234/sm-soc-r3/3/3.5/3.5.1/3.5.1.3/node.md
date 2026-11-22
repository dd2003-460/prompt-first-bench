# N236: 约束边界条件：当 β_exposure（价格权重系数）降低时，若 ε_p * ΔP% + ε_q * ΔQ% > -5%，则 GMV_new > 0.95 * 

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N77

## Claim

约束边界条件：当 β_exposure（价格权重系数）降低时，若 ε_p * ΔP% + ε_q * ΔQ% > -5%，则 GMV_new > 0.95 * GMV_old 成立。需模拟 β 从 1.0 降至 0.5 时的 GMV 分布区间。

## Corrected Claim

约束边界条件：当 β_exposure（价格权重系数）降低时，若 ε_p * ΔP% + ε_q * ΔQ% > -5%，则 GMV_new > 0.95 * GMV_old 成立。需模拟 β 从 1.0 降至 0.5 时的 GMV 分布区间。

## Evidence

先验知识/题面给定，逻辑校验通过

## Search Query

GMV constraint simulation price weight reduction

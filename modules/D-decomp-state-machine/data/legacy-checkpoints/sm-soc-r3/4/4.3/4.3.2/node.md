# N73: 预期成交量 Q 的估计模型：Q = N_active_sellers * P(quick_sale | intervention) * (1 - P(churn

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N21

## Claim

预期成交量 Q 的估计模型：Q = N_active_sellers * P(quick_sale | intervention) * (1 - P(churn | subsidy))；其中 P(quick_sale) 需基于历史48小时成交率基线修正

## Corrected Claim

预期成交量 Q 的估计模型：Q = N_active_sellers * P(quick_sale | intervention) * (1 - P(churn | subsidy))；其中 P(quick_sale) 需基于历史48小时成交率基线修正

## Evidence

先验知识/题面给定，逻辑校验通过

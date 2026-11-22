# N166: 突发事件（Black Swan）剔除规则：定义 |ΔGMV_t| > 3 * σ_daily 为异常点，计算时采用稳健标准差（MAD）替代标准标准差，若异常点占

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: stochastic
- **rework_count**: 0
- **parent_ids**: N54

## Claim

突发事件（Black Swan）剔除规则：定义 |ΔGMV_t| > 3 * σ_daily 为异常点，计算时采用稳健标准差（MAD）替代标准标准差，若异常点占比 > 5%，则 σ²_intervention 置信度降为 0.5。

## Corrected Claim

突发事件（Black Swan）剔除规则：定义 |ΔGMV_t| > 3 * σ_daily 为异常点，计算时采用稳健标准差（MAD）替代标准标准差，若异常点占比 > 5%，则 σ²_intervention 置信度降为 0.5。

## Evidence

先验知识/题面给定，逻辑校验通过

## Search Query

robust standard deviation MAD outlier removal A/B test variance

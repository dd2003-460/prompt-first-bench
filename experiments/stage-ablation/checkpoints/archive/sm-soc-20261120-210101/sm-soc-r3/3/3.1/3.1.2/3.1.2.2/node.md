# N221: 下游投影1：CTR 差异的置信区间计算，CI_95 = (CTR_high - CTR_low) ± 1.96 * sqrt(CTR_high(1-CTR_hi

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: stochastic
- **rework_count**: 0
- **parent_ids**: N60

## Claim

下游投影1：CTR 差异的置信区间计算，CI_95 = (CTR_high - CTR_low) ± 1.96 * sqrt(CTR_high(1-CTR_high)/n_high + CTR_low(1-CTR_low)/n_low)，需代入具体样本量 n_high, n_low 计算。

## Corrected Claim

下游投影1：CTR 差异的置信区间计算，CI_95 = (CTR_high - CTR_low) ± 1.96 * sqrt(CTR_high(1-CTR_high)/n_high + CTR_low(1-CTR_low)/n_low)，需代入具体样本量 n_high, n_low 计算。

## Evidence

先验知识/题面给定，逻辑校验通过

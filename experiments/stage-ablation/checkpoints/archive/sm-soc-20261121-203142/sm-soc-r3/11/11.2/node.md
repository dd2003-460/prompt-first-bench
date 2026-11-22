# N299: 稳健性指数公式修正：原公式 1 - (CI_width / β_low_mean) 在数学上无界且逻辑错误（CI宽度通常大于均值），应修正为 1 - (CI_w

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N101

## Claim

稳健性指数公式修正：原公式 1 - (CI_width / β_low_mean) 在数学上无界且逻辑错误（CI宽度通常大于均值），应修正为 1 - (CI_width / 2 * β_low_mean)，即基于半宽占比计算，或采用 Bootstrap 方法计算结论反转的概率 P(β_low < threshold | data)。

## Corrected Claim

稳健性指数公式修正：原公式 1 - (CI_width / β_low_mean) 在数学上无界且逻辑错误（CI宽度通常大于均值），应修正为 1 - (CI_width / 2 * β_low_mean)，即基于半宽占比计算，或采用 Bootstrap 方法计算结论反转的概率 P(β_low < threshold | data)。

## Evidence

先验知识/题面给定，逻辑校验通过：原公式确实存在量纲和逻辑问题（CI宽度通常大于均值导致负值），修正为基于半宽占比或Bootstrap概率在统计学上是合理的稳健性评估方法。

## Search Query

robustness index formula for statistical conclusion sensitivity analysis confidence interval width

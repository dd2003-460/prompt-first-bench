# N131: 统计量选择约束：使用中位数而非算术平均值的核心理由是成交价的偏度 Skewness(P_deal) > 0.5（右偏分布），导致算术平均数 E[P] 显著高于中

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N35

## Claim

统计量选择约束：使用中位数而非算术平均值的核心理由是成交价的偏度 Skewness(P_deal) > 0.5（右偏分布），导致算术平均数 E[P] 显著高于中位数 Median(P)。需量化偏差幅度 Bias = (E[P] - Median(P)) / Median(P)，若 Bias > 10%，则必须使用中位数以避免高估 P_ref 导致 δ 计算虚高。

## Corrected Claim

统计量选择约束：使用中位数而非算术平均值的核心理由是成交价的偏度 Skewness(P_deal) > 0.5（右偏分布），导致算术平均数 E[P] 显著高于中位数 Median(P)。需量化偏差幅度 Bias = (E[P] - Median(P)) / Median(P)，若 Bias > 10%，则必须使用中位数以避免高估 P_ref 导致 δ 计算虚高。

## Evidence

先验知识/题面给定，逻辑校验通过：右偏分布（Skewness > 0）确实导致均值大于中位数，且偏度越大偏差通常越显著，使用鲁棒性更强的中位数以避免高估参考值是合理的统计推断。

## Search Query

skewness of transaction prices second-hand market mean vs median bias magnitude

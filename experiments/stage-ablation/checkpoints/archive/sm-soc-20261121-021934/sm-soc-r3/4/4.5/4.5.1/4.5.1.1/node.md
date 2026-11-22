# N115: 卖家价格弹性系数 ε_price 的实证估计方法为 OLS 回归 ln(Q) = α + ε_price * ln(P) + β * X + ε，其中 X 为控

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N49

## Claim

卖家价格弹性系数 ε_price 的实证估计方法为 OLS 回归 ln(Q) = α + ε_price * ln(P) + β * X + ε，其中 X 为控制变量（如品类、卖家信用分），ε_price 的置信区间为 ε̂ ± 1.96*SE(ε̂)。

## Corrected Claim

卖家价格弹性系数 ε_price 的实证估计方法为 OLS 回归 ln(Q) = α + ε_price * ln(P) + β * X + ε，其中 X 为控制变量（如品类、卖家信用分），ε_price 的置信区间为 ε̂ ± 1.96*SE(ε̂)。

## Evidence

[质询]OLS 回归在存在内生性（如价格与需求冲击相关）时估计有偏，但陈述仅描述“实证估计方法”而非声称无偏，且置信区间公式为标准正态近似，逻辑上无硬伤。 | 先验知识/题面给定，逻辑校验通过：对数-对数回归是估计价格弹性的标准计量经济学方法，控制变量和置信区间计算符合统计学原理。

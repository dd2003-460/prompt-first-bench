# N197: 排除混杂变量的控制变量集：在对比咨询率时，需控制商品成色 (Condition)、品牌热度 (Brand_Score) 和发布时间 (Age_in_days)，

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N75

## Claim

排除混杂变量的控制变量集：在对比咨询率时，需控制商品成色 (Condition)、品牌热度 (Brand_Score) 和发布时间 (Age_in_days)，通过多元回归 Rate = β0 + β1*Exposure + β2*Condition + β3*Brand + ε，若 β1 的 p-value < 0.05，则确认曝光对咨询率的独立影响显著。

## Corrected Claim

排除混杂变量的控制变量集：在对比咨询率时，需控制商品成色 (Condition)、品牌热度 (Brand_Score) 和发布时间 (Age_in_days)，通过多元回归 Rate = β0 + β1*Exposure + β2*Condition + β3*Brand + ε，若 β1 的 p-value < 0.05，则确认曝光对咨询率的独立影响显著。

## Evidence

先验知识/题面给定，逻辑校验通过：该陈述描述了标准的多元线性回归控制变量法，逻辑自洽且符合统计学基本原理。

## Search Query

multiple regression control variables exposure consultation rate

# N316: 混杂变量控制：商品质量 Q 同时影响 CTR 和成交周期，需构建控制方程 T_deal = α + β1*CTR + β2*T_exposure + β3*Q 

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N108

## Claim

混杂变量控制：商品质量 Q 同时影响 CTR 和成交周期，需构建控制方程 T_deal = α + β1*CTR + β2*T_exposure + β3*Q + ε；若 β3 显著且 β2 在控制 Q 后下降超过 50%，则证明曝光时长的效应大部分由质量混杂解释，因果链条断裂。

## Corrected Claim

混杂变量控制：商品质量 Q 同时影响 CTR 和成交周期，需构建控制方程 T_deal = α + β1*CTR + β2*T_exposure + β3*Q + ε；若 β3 显著且 β2 在控制 Q 后下降超过 50%，则证明曝光时长的效应大部分由质量混杂解释，因果链条断裂。

## Evidence

先验知识/题面给定，逻辑校验通过：该陈述描述了标准的多元回归控制变量法逻辑，用于识别混杂效应（Omitted Variable Bias），量纲与因果推断逻辑自洽。

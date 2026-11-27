# N47: 控制变量回归模型：T_deal = β0 + β1*Price_Discount + β2*Item_Quality + β3*Seller_Rating + 

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N14

## Claim

控制变量回归模型：T_deal = β0 + β1*Price_Discount + β2*Item_Quality + β3*Seller_Rating + ε，其中 β1 的显著性 (t-stat > 2) 是判定‘噪声导致匹配加速’因果效应的必要条件，β1 预期值为负。

## Corrected Claim

控制变量回归模型：T_deal = β0 + β1*Price_Discount + β2*Item_Quality + β3*Seller_Rating + ε，其中 β1 的显著性 (t-stat > 2) 是判定‘噪声导致匹配加速’因果效应的必要条件，β1 预期值为负。

## Evidence

先验知识/题面给定，逻辑校验通过：控制变量回归中，系数显著性（t-stat > 2）确实是排除随机噪声、确立统计显著性的必要条件；且折扣（Price_Discount）通常与交易达成概率正相关，若定义为‘折扣率’则系数应为正，但若定义为‘价格水平’或‘未折扣程度’则系数为负，此处‘预期值为负’符合‘价格越高/折扣越小，匹配越慢’的经济直觉，逻辑自洽。

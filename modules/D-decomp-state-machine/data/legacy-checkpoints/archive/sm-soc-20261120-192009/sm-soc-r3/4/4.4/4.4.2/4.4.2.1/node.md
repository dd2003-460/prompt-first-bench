# N256: 稀缺度混杂变量 I_t 的操作化定义：I_t 定义为同一 Category ID + Brand + Condition 组合下，过去 7 天内平均在售商品数量

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N87

## Claim

稀缺度混杂变量 I_t 的操作化定义：I_t 定义为同一 Category ID + Brand + Condition 组合下，过去 7 天内平均在售商品数量；若 I_t 与 Price_High 的相关系数 r < 0.3，则多重共线性不严重，VIF < 5，回归系数 β1 的估计有效；若 r > 0.5，需引入主成分分析或岭回归修正。

## Corrected Claim

稀缺度混杂变量 I_t 的操作化定义：I_t 定义为同一 Category ID + Brand + Condition 组合下，过去 7 天内平均在售商品数量；若 I_t 与 Price_High 的相关系数 r < 0.3，则多重共线性不严重，VIF < 5，回归系数 β1 的估计有效；若 r > 0.5，需引入主成分分析或岭回归修正。

## Evidence

先验知识/题面给定，逻辑校验通过：I_t 的定义符合稀缺度操作化常规；r<0.3 对应 VIF<5 及 r>0.5 需正则化/PCA 的统计推断符合多重共线性处理的基本原理。

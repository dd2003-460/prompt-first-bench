# N113: CTR_drop 计算的混杂因素控制：需排除'卖家信用分突变'和'商品图片更换'两个混杂变量，通过回归模型 $CTR_{drop} = \beta_0 + \b

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N45

## Claim

CTR_drop 计算的混杂因素控制：需排除'卖家信用分突变'和'商品图片更换'两个混杂变量，通过回归模型 $CTR_{drop} = \beta_0 + \beta_1 \Delta Price + \beta_2 \Delta Credit + \beta_3 \Delta Image + \epsilon$ 估计纯价格效应，若 $\beta_2, \beta_3$ 显著不为0，则原始 CTR_drop 需修正。

## Corrected Claim

CTR_drop 计算的混杂因素控制：需排除'卖家信用分突变'和'商品图片更换'两个混杂变量，通过回归模型 $CTR_{drop} = \beta_0 + \beta_1 \Delta Price + \beta_2 \Delta Credit + \beta_3 \Delta Image + \epsilon$ 估计纯价格效应，若 $\beta_2, \beta_3$ 显著不为0，则原始 CTR_drop 需修正。

## Evidence

先验知识/题面给定，逻辑校验通过：该陈述描述了标准的多元线性回归控制变量法，用于隔离价格对CTR的影响，逻辑自洽且符合计量经济学基本原理。

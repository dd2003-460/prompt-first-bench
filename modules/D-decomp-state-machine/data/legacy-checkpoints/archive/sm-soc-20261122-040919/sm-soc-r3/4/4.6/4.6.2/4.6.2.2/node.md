# N324: n（样本量）的有效值需考虑聚类效应，若数据按卖家或商品类别聚类，有效样本量 n_eff = n / (1 + (m-1)*ICC)，其中 m 为平均簇大小，IC

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N95

## Claim

n（样本量）的有效值需考虑聚类效应，若数据按卖家或商品类别聚类，有效样本量 n_eff = n / (1 + (m-1)*ICC)，其中 m 为平均簇大小，ICC 为组内相关系数；若 ICC=0.2, m=5，则 n_eff = n / 1.8，t 统计量需相应调整。

## Corrected Claim

n（样本量）的有效值需考虑聚类效应，若数据按卖家或商品类别聚类，有效样本量 n_eff = n / (1 + (m-1)*ICC)，其中 m 为平均簇大小，ICC 为组内相关系数；若 ICC=0.2, m=5，则 n_eff = n / 1.8，t 统计量需相应调整。

## Evidence

先验知识/题面给定，逻辑校验通过：公式 n_eff = n / (1 + (m-1)*ICC) 是聚类数据有效样本量的标准近似公式（Design Effect 的倒数），代入 ICC=0.2, m=5 计算得 1/(1+4*0.2) = 1/1.8，数值推导正确。

## Search Query

effective sample size clustering intraclass correlation coefficient ICC formula

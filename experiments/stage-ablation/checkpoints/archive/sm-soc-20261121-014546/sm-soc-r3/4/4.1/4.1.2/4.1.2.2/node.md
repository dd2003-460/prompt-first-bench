# N277: 卖家类型异质性参数：专业卖家（占比 20%）的调整概率 p_pro = 0.95，个人卖家（占比 80%）的调整概率 p_ind = 0.65。整体响应率 r_

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: stochastic
- **rework_count**: 0
- **parent_ids**: N83

## Claim

卖家类型异质性参数：专业卖家（占比 20%）的调整概率 p_pro = 0.95，个人卖家（占比 80%）的调整概率 p_ind = 0.65。整体响应率 r_seller = 0.2 * 0.95 + 0.8 * 0.65 = 0.71，修正了 N83 中假设的 0.8，反映了不同卖家群体对价格信号的敏感度差异。

## Corrected Claim

卖家类型异质性参数：专业卖家（占比 20%）的调整概率 p_pro = 0.95，个人卖家（占比 80%）的调整概率 p_ind = 0.65。整体响应率 r_seller = 0.2 * 0.95 + 0.8 * 0.65 = 0.71，修正了 N83 中假设的 0.8，反映了不同卖家群体对价格信号的敏感度差异。

## Evidence

先验知识/题面给定，逻辑校验通过：加权平均计算 0.2*0.95 + 0.8*0.65 = 0.19 + 0.52 = 0.71 正确，且参数设定符合专业卖家比个人卖家更敏感的经济直觉。

## Search Query

difference in price adjustment probability between professional and individual sellers in C2C markets

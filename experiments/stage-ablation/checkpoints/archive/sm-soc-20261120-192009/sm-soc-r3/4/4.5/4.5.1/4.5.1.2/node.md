# N262: 选择方程（Selection Equation）的构建变量：以成交状态 D_i=1 为因变量，自变量包括 Price_High_i、Inventory_I_i、

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N89

## Claim

选择方程（Selection Equation）的构建变量：以成交状态 D_i=1 为因变量，自变量包括 Price_High_i、Inventory_I_i、Time_to_Listing_t_i 及卖家历史成交率 S_seller；Logit 模型系数 β_sel 需显著（p<0.05）以证明选择机制非随机，否则 Heckman 校正无效。

## Corrected Claim

选择方程（Selection Equation）的构建变量：以成交状态 D_i=1 为因变量，自变量包括 Price_High_i、Inventory_I_i、Time_to_Listing_t_i 及卖家历史成交率 S_seller；Logit 模型系数 β_sel 需显著（p<0.05）以证明选择机制非随机，否则 Heckman 校正无效。

## Evidence

先验知识/题面给定，逻辑校验通过：Heckman 两阶段模型中，第一阶段选择方程需包含影响选择概率的变量（如价格、库存、时间、卖家特征），且系数显著性是证明选择偏差存在、从而需要校正的前提，符合计量经济学标准理论。

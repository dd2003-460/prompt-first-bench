# N242: 基线样本量 n_normal 的计算逻辑：n_normal = N_total * P(Price_Deviation < 5%) * (1 - Dropout

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N81

## Claim

基线样本量 n_normal 的计算逻辑：n_normal = N_total * P(Price_Deviation < 5%) * (1 - Dropout_Rate)，其中 P(Price_Deviation < 5%) 需从平台历史价格分布中检索（通常约为 30-40%），Dropout_Rate 为数据缺失率（估计为 5%）。

## Corrected Claim

基线样本量 n_normal 的计算逻辑：n_normal = N_total * P(Price_Deviation < 5%) * (1 - Dropout_Rate)，其中 P(Price_Deviation < 5%) 需从平台历史价格分布中检索（通常约为 30-40%），Dropout_Rate 为数据缺失率（估计为 5%）。

## Evidence

先验知识/题面给定，逻辑校验通过

## Search Query

second hand marketplace price distribution normal pricing share

# N138: 单位用户成本差 (Self_Built_Cost - Cloud_Cost) / Monthly_Users 计算：Monthly_Users = DAU × 

- **status**: pending
- **level**: L3
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N39

## Claim

单位用户成本差 (Self_Built_Cost - Cloud_Cost) / Monthly_Users 计算：Monthly_Users = DAU × 30 = 1.5 × 10^8，Self_Built_Cost 和 Cloud_Cost 由 N38 公式分别计算得出，成本差除以用户数得到单位用户成本差（典型值 ¥0.01-0.1/用户/月）。

## Corrected Claim

单位用户成本差 (Self_Built_Cost - Cloud_Cost) / Monthly_Users 计算：Monthly_Users = DAU × 30 = 1.5 × 10^8，Self_Built_Cost 和 Cloud_Cost 由 N38 公式分别计算得出，成本差除以用户数得到单位用户成本差（典型值 ¥0.01-0.1/用户/月）。

## Evidence

父节点级核验未通过：不完备（子节点在架构策略上具有正交性（纯公有云、纯自建、混合），且覆盖了主要工作点。但存在严重逻辑缺陷：1. 大规模场景下，随着流量增加，公有云成本线性增长，而自建固定成本摊薄，通常自建成本会低于公有云（Unit_Cost_Diff 应为负值或绝对值变小），但示例计算显示自建仍远高于公有云（¥190k vs ¥60k），导致结论‘自建固定成本摊薄效应有限’与常识及数学逻辑相悖，未能正确展示自建在大规模下的成本优势；2. 混合策略中引入了 LTV 变量，超出了父节点‘单位用户成本差’（纯成本维度）的定义范围，导致维度不纯。）

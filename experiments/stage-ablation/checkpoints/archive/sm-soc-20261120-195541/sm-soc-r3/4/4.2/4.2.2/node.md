# N47: 控制变量回归模型：T_deal = β0 + β1*Price_Discount + β2*Item_Quality + β3*Seller_Rating + 

- **status**: pending
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

父节点级核验未通过：不完备（子节点之间存在逻辑交叉（Seller_Rating 的非线性检验与 Price_Discount 的交互项涉及模型结构修改，而非单纯变量定义），且缺失了父节点中明确提到的误差项 ε 的处理（如异方差稳健标准误）以及 T_deal 因变量的操作化定义，导致完备性不足。）

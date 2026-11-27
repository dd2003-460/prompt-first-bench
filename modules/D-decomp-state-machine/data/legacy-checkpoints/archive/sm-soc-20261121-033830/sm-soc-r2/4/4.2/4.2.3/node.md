# N72: 候选B（动态建议）的算法输入：建议价 P_suggest = g(历史成交均价 P_avg, 库存天数 D_days, 商品稀缺度 S)，其中稀缺度 S 由同类

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N18

## Claim

候选B（动态建议）的算法输入：建议价 P_suggest = g(历史成交均价 P_avg, 库存天数 D_days, 商品稀缺度 S)，其中稀缺度 S 由同类在售商品数量 N_supply 倒数决定，S = 1/N_supply，该算法旨在替代卖家的随机变异定价 ε_p。

## Corrected Claim

候选B（动态建议）的算法输入：建议价 P_suggest = g(历史成交均价 P_avg, 库存天数 D_days, 商品稀缺度 S)，其中稀缺度 S 由同类在售商品数量 N_supply 倒数决定，S = 1/N_supply，该算法旨在替代卖家的随机变异定价 ε_p。

## Evidence

先验知识/题面给定，逻辑校验通过

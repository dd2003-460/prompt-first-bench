# N137: Price_Discount 变量的操作化定义：定义为 (P_market - P_ask) / P_market，负值表示高挂价，正值表示降价促销；需标准化处

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N47

## Claim

Price_Discount 变量的操作化定义：定义为 (P_market - P_ask) / P_market，负值表示高挂价，正值表示降价促销；需标准化处理（Z-score）以消除量纲影响，确保 β1 系数可直接解释为每标准差偏差对应的 T_deal 变化天数。

## Corrected Claim

Price_Discount 变量的操作化定义：定义为 (P_market - P_ask) / P_market，负值表示高挂价，正值表示降价促销；需标准化处理（Z-score）以消除量纲影响，确保 β1 系数可直接解释为每标准差偏差对应的 T_deal 变化天数。

## Evidence

先验知识/题面给定，逻辑校验通过：定义公式量纲一致（无量纲比率），Z-score标准化是回归分析中处理连续变量以解释系数为每标准差变化的标准做法，逻辑自洽。

# N251: 供给稀缺度变化 ΔSupply_Scarcity 的计算：ΔSupply_Scarcity = (S_old - S_new) / S_old，其中 S_old

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N82

## Claim

供给稀缺度变化 ΔSupply_Scarcity 的计算：ΔSupply_Scarcity = (S_old - S_new) / S_old，其中 S_old 和 S_new 分别为干预前后的在售商品数量，若卖家退出导致 S_new < S_old，则 ΔSupply_Scarcity > 0，直接增加搜索成本系数 α 的乘数效应。

## Corrected Claim

供给稀缺度变化 ΔSupply_Scarcity 的计算：ΔSupply_Scarcity = (S_old - S_new) / S_old，其中 S_old 和 S_new 分别为干预前后的在售商品数量，若卖家退出导致 S_new < S_old，则 ΔSupply_Scarcity > 0，直接增加搜索成本系数 α 的乘数效应。

## Evidence

先验知识/题面给定，逻辑校验通过：公式定义清晰，符号方向（S_new < S_old 导致分子为正）与结论（Δ > 0）一致，符合经济学中供给减少导致稀缺度上升及搜索成本增加的基本直觉。

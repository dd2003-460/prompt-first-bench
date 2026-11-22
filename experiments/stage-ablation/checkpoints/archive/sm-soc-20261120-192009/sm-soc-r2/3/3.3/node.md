# N18: 受损方评估：卖家受损程度 ΔU_seller = -ΔPrice * Quantity + ΔSpeed * C_holding；若挂价下降 15%，但周期缩短

- **status**: pending
- **level**: L2
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N3

## Claim

受损方评估：卖家受损程度 ΔU_seller = -ΔPrice * Quantity + ΔSpeed * C_holding；若挂价下降 15%，但周期缩短 30%，则 ΔU_seller 可能为正（若 C_holding 高）或负（若 C_holding 低）；需计算 r 的临界值 r* = ΔPrice / (ΔSpeed * T0)。

## Corrected Claim

受损方评估：卖家受损程度 ΔU_seller = -ΔPrice * Quantity + ΔSpeed * C_holding；若挂价下降 15%，但周期缩短 30%，则 ΔU_seller 可能为正（若 C_holding 高）或负（若 C_holding 低）；需计算 r 的临界值 r* = ΔPrice / (ΔSpeed * T0)。

## Evidence

父节点级核验未通过：非正交, 有冗余（子节点4（临界值解析解）在逻辑上依赖于子节点1（随机源定义）和子节点2/3（具体项量化），且其推导过程直接重复了子节点2和3中的数值代入逻辑，导致内容重叠。此外，子节点1定义的是分布特征，而子节点4使用的是点估计值，两者在数学处理上存在层级混淆，虽不完全矛盾但边界模糊。）

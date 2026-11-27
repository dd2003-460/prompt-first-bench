# N58: 卖家定价函数投影1：卖家最优挂价 P_ask* = (1 + λ * (P_ref - P_floor) / P_floor) * P_floor + ε_s，

- **status**: pending
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N12

## Claim

卖家定价函数投影1：卖家最优挂价 P_ask* = (1 + λ * (P_ref - P_floor) / P_floor) * P_floor + ε_s，其中 P_ref 为参考成交价，P_floor 为心理底价，λ=2.25 为损失厌恶系数。该公式量化了损失厌恶如何将挂价推高至参考价的 15-25% 以上。

## Corrected Claim

卖家定价函数投影1：卖家最优挂价 P_ask* = (1 + λ * (P_ref - P_floor) / P_floor) * P_floor + ε_s，其中 P_ref 为参考成交价，P_floor 为心理底价，λ=2.25 为损失厌恶系数。该公式量化了损失厌恶如何将挂价推高至参考价的 15-25% 以上。

## Evidence

父节点级核验未通过：非正交, 有冗余（子节点2定义了 P_floor 与 P_ref 的关系，子节点3基于该关系推导了溢价项，两者在数学逻辑上强耦合且存在信息重叠（子节点3的结论依赖于子节点2的定义），并非完全正交。此外，子节点1关于 σ_s 的取值理由（使平均溢价落在15-25%区间）与子节点3计算的确定性溢价（22.5%）在逻辑上存在轻微冲突或需要更清晰的区分（随机噪声 vs 确定性偏差），导致概念边界模糊。）

# N17: 有效命中率 Hit_eff = Hit_base * (1 - P_inval * S_hot)，其中 S_hot 是热门对象（前 10% 热度）在总请求字节中

- **status**: pending
- **level**: L2
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N4

## Claim

有效命中率 Hit_eff = Hit_base * (1 - P_inval * S_hot)，其中 S_hot 是热门对象（前 10% 热度）在总请求字节中的占比，需量化 S_hot 在 ρ=-0.3 约束下的值

## Corrected Claim

有效命中率 Hit_eff = Hit_base * (1 - P_inval * S_hot)，其中 S_hot 是热门对象（前 10% 热度）在总请求字节中的占比，需量化 S_hot 在 ρ=-0.3 约束下的值

## Evidence

父节点级核验未通过：不完备（子节点在逻辑上是正交的（一个关注对象大小特征，一个关注最终占比结果），且不存在冗余。然而，完备性不足：父节点的核心任务是“量化 S_hot”，但子节点仅提供了 S_hot 的估计值和其影响因素（E[S|Hot]），缺失了从“对象大小/数量分布”到“字节占比 S_hot”的具体推导逻辑或计算公式（即：S_hot = (N_hot * E[S|Hot]) / (N_total * E[S|All]) 这一关键步骤未在子节点中明确体现，导致逻辑链条断裂）。）

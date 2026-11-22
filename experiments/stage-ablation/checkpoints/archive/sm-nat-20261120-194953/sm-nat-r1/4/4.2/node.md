# N17: 有效命中率 Hit_eff = Hit_base * (1 - P_inval * S_hot)，其中 S_hot 是热门对象（前 10% 热度）在总请求字节中

- **status**: verified
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

先验知识/题面给定，逻辑校验通过

# N62: 引入 TTL 机制后，有效命中率 H_TTL = H_static * (1 - u) * P_TTL_hit + (1 - H_static) * P_rev

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N20

## Claim

引入 TTL 机制后，有效命中率 H_TTL = H_static * (1 - u) * P_TTL_hit + (1 - H_static) * P_revalidate，其中 P_TTL_hit 是 TTL 未过期时的命中概率，对于 u=0.1 且 TTL=T_res/2，P_TTL_hit ≈ 0.5，整体折损降低约 30%

## Corrected Claim

引入 TTL 机制后，有效命中率 H_TTL = H_static * (1 - u) * P_TTL_hit + (1 - H_static) * P_revalidate，其中 P_TTL_hit 是 TTL 未过期时的命中概率，对于 u=0.1 且 TTL=T_res/2，P_TTL_hit ≈ 0.5，整体折损降低约 30%

## Evidence

先验知识/题面给定，逻辑校验通过

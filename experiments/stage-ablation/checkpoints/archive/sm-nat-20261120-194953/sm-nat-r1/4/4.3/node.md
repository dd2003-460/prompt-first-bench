# N18: 高更新率工作点：当 u=0.01 且 T_hot=24h 时，P_inval_hot ≈ 0.22，导致热门对象命中率折损约 22% * S_hot，需验证 T

- **status**: verified
- **level**: L2
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N4

## Claim

高更新率工作点：当 u=0.01 且 T_hot=24h 时，P_inval_hot ≈ 0.22，导致热门对象命中率折损约 22% * S_hot，需验证 T_hot 是否受 128GB 容量约束

## Corrected Claim

高更新率工作点：当 u=0.01 且 T_hot=24h 时，P_inval_hot ≈ 0.22，导致热门对象命中率折损约 22% * S_hot，需验证 T_hot 是否受 128GB 容量约束

## Evidence

先验知识/题面给定，逻辑校验通过：u=0.01, T_hot=24h 时，P_inval_hot = 1 - exp(-u*T_hot) ≈ 1 - exp(-0.24) ≈ 0.213，与 0.22 量级一致；命中率折损逻辑自洽。

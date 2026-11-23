# N7: 自建10个POP点的最大地理覆盖半径约束：每个POP点需覆盖的地理半径 R_max 必须满足 R_max ≥ d_max，其中 d_max 为最远用户到最近PO

- **status**: verified
- **level**: L2
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N1, N2, N3

## Claim

自建10个POP点的最大地理覆盖半径约束：每个POP点需覆盖的地理半径 R_max 必须满足 R_max ≥ d_max，其中 d_max 为最远用户到最近POP点的距离，若 R_max < d_max 则自建策略在延迟约束下不可行

## Corrected Claim

自建10个POP点的最大地理覆盖半径约束：每个POP点需覆盖的地理半径 R_max 必须满足 R_max ≥ d_max，其中 d_max 为最远用户到最近POP点的距离，若 R_max < d_max 则自建策略在延迟约束下不可行

## Evidence

先验知识/题面给定，逻辑校验通过：该陈述定义了覆盖半径与最大用户距离之间的必要约束关系，符合几何覆盖的基本逻辑，无内部矛盾。

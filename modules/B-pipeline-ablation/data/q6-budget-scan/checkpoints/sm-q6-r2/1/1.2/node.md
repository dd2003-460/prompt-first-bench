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

父节点级核验通过：正交+完备+无冗余（子节点逻辑清晰且正交：节点1提供物理转换系数（km/ms），节点2基于延迟约束推导理论最大物理距离上限，节点3基于实际地理分布计算10个POP点下的实际覆盖半径（d_max），节点4针对边界极端情况量化不可行性。各节点分别对应‘转换参数’、‘理论上限’、‘实际部署约束’和‘边界失效分析’，无重复或矛盾，且共同完整覆盖了从物理原理到实际部署再到边界验证的全链路。）

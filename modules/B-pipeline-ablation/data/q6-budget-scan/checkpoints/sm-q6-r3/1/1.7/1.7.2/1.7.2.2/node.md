# N127: 路由非直线系数 (Cable Stretch Factor) 典型值为 1.2-1.5，表示实际光缆铺设路径长度与直线距离之比，用于修正 RTT_min 公式中

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N37

## Claim

路由非直线系数 (Cable Stretch Factor) 典型值为 1.2-1.5，表示实际光缆铺设路径长度与直线距离之比，用于修正 RTT_min 公式中的 d 为实际传输距离 d_actual = d * 1.3。

## Corrected Claim

路由非直线系数 (Cable Stretch Factor) 典型值为 1.2-1.5，表示实际光缆铺设路径长度与直线距离之比，用于修正 RTT_min 公式中的 d 为实际传输距离 d_actual = d * 1.3。

## Evidence

先验知识/题面给定，逻辑校验通过：光缆铺设受地形、法规及避障影响，实际路径长于直线距离，1.2-1.5 为工程界公认的典型绕线系数（Cable Stretch Factor），量级合理且符合物理直觉。

## Search Query

fiber optic cable stretch factor routing efficiency coefficient

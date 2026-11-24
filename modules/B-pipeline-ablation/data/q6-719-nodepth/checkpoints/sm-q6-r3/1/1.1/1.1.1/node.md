# N40: 物理距离 d 的计算公式为 Haversine 公式：d = 2R × arcsin(sqrt(sin²((lat2-lat1)/2) + cos(lat1)c

- **status**: pending
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N6

## Claim

物理距离 d 的计算公式为 Haversine 公式：d = 2R × arcsin(sqrt(sin²((lat2-lat1)/2) + cos(lat1)cos(lat2)sin²((lon2-lon1)/2)))，其中 R=6371km，lat/lon 为用户坐标与最近 POP 坐标

## Corrected Claim

物理距离 d 的计算公式为 Haversine 公式：d = 2R × arcsin(sqrt(sin²((lat2-lat1)/2) + cos(lat1)cos(lat2)sin²((lon2-lon1)/2)))，其中 R=6371km，lat/lon 为用户坐标与最近 POP 坐标

## Evidence

父节点级核验未通过：不完备, 有冗余（子节点本质上是同一物理模型（距离对RTT的影响）在三个不同距离量级下的具体实例化，属于参数取值不同而非概念正交；且父节点核心是‘Haversine公式定义’，子节点未覆盖公式变量定义、适用前提或边界条件等关键方面，仅展示了应用结果。）

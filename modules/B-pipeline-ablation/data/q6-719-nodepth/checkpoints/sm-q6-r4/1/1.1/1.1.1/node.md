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

父节点级核验未通过：不完备, 有冗余（子节点之间存在明显的逻辑冗余，它们本质上是同一个物理模型（Haversine公式推导RTT）在不同距离参数下的实例化，而非独立的知识维度。此外，父节点仅定义了距离计算公式，未涉及RTT推导或成本/延迟权衡，子节点扩展了父节点未明确包含的上下文（如RTT下限、成本工作点），导致覆盖范围不匹配。）

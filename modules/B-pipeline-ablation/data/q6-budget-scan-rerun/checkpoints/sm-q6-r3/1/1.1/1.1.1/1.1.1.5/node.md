# N110: RTT 基础值估算：用户到最近边缘节点的物理距离 D_km 与光速 c 的关系，RTT_min ≈ 2 * D_km / (c * 0.66)，其中 0.66 

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N22, N23, N24

## Claim

RTT 基础值估算：用户到最近边缘节点的物理距离 D_km 与光速 c 的关系，RTT_min ≈ 2 * D_km / (c * 0.66)，其中 0.66 为光纤中光速修正系数；典型城市间距离 500km 对应 RTT_min ≈ 5ms

## Corrected Claim

RTT 基础值估算：用户到最近边缘节点的物理距离 D_km 与光速 c 的关系，RTT_min ≈ 2 * D_km / (c * 0.66)，其中 0.66 为光纤中光速修正系数；典型城市间距离 500km 对应 RTT_min ≈ 5ms

## Evidence

先验知识/题面给定，逻辑校验通过：光速约3e8 m/s，光纤折射率约1.5，速度约2e8 m/s，500km往返距离1000km，时间=1000000/200000=5s? 不，1000km=1e6m, 2e8 m/s -> 0.005s = 5ms。计算正确。

## Search Query

RTT calculation fiber optic speed 500km latency

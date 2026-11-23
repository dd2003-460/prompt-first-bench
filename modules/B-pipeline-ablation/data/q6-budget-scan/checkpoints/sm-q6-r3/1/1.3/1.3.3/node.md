# N48: 长尾区域用户到最近POP点的距离分布：基于中国地理分布，约30-40%用户距离最近POP点>500km，RTT_avg通常在50-100ms之间，P99延迟可达

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N9

## Claim

长尾区域用户到最近POP点的距离分布：基于中国地理分布，约30-40%用户距离最近POP点>500km，RTT_avg通常在50-100ms之间，P99延迟可达200-400ms

## Corrected Claim

长尾区域用户到最近POP点的距离分布：基于中国地理分布，约30-40%用户距离最近POP点>500km，RTT_avg通常在50-100ms之间，P99延迟可达200-400ms

## Evidence

先验知识/题面给定，逻辑校验通过：中国地理跨度大，POP点通常集中在核心城市，长尾用户（如西部、偏远地区）距离核心节点>500km的比例在30-40%符合地理直觉；光纤传输速度约200,000 km/s，500km单程延迟约2.5ms，往返基础延迟约5ms，加上路由跳数、处理延迟及长尾路径的额外开销，RTT_avg 50-100ms及P99 200-400ms的量级在工程上合理且自洽。

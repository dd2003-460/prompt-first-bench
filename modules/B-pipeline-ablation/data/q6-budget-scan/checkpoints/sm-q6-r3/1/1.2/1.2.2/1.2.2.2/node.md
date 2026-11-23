# N190: 二线城市用户到最近POP的距离 d_tier2 ≈ 200-500 km，对应单程传播延迟 d/c ≈ 1.0-2.5 ms，RTT_prop ≈ 2-5 ms

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N57

## Claim

二线城市用户到最近POP的距离 d_tier2 ≈ 200-500 km，对应单程传播延迟 d/c ≈ 1.0-2.5 ms，RTT_prop ≈ 2-5 ms，属于中等延迟覆盖区，需考虑光纤路由非直线效应

## Corrected Claim

二线城市用户到最近POP的距离 d_tier2 ≈ 200-500 km，对应单程传播延迟 d/c ≈ 1.0-2.5 ms，RTT_prop ≈ 2-5 ms，属于中等延迟覆盖区，需考虑光纤路由非直线效应

## Evidence

先验知识/题面给定，逻辑校验通过：光速约300,000 km/s，200-500 km距离对应单程延迟0.67-1.67 ms，考虑光纤折射率（约1.5）及路由非直线效应（通常1.2-1.5倍），单程延迟约1.0-2.5 ms，RTT约2-5 ms，数值量级与物理规律自洽。

## Search Query

second tier city China CDN edge node distance propagation delay

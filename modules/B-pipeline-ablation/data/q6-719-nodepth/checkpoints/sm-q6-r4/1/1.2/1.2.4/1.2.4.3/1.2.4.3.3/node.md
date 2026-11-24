# N662: L2到源站RTT P99 的低成本工作点：RTT_L2_source_p99 = 50ms，基于源站位于北京与L2节点位于乌鲁木齐（87.6°E, 43.8°N

- **status**: verified
- **level**: L5
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N218

## Claim

L2到源站RTT P99 的低成本工作点：RTT_L2_source_p99 = 50ms，基于源站位于北京与L2节点位于乌鲁木齐（87.6°E, 43.8°N）的地理距离 D≈3000km，传播延迟 2*3000/200000*1000=30ms + 普通公网路由开销 20ms，对应带宽成本 C_bw_line 最低（使用普通ISP线路）

## Corrected Claim

L2到源站RTT P99 的低成本工作点：RTT_L2_source_p99 = 50ms，基于源站位于北京与L2节点位于乌鲁木齐（87.6°E, 43.8°N）的地理距离 D≈3000km，传播延迟 2*3000/200000*1000=30ms + 普通公网路由开销 20ms，对应带宽成本 C_bw_line 最低（使用普通ISP线路）

## Evidence

先验知识/题面给定，逻辑校验通过：地理距离约3000km对应光纤传播延迟约30ms（光速在光纤中约为200,000km/s，往返6000km/200,000km/s=0.03s=30ms），加上普通公网路由开销20ms，总RTT P99为50ms符合工程常识与物理规律。

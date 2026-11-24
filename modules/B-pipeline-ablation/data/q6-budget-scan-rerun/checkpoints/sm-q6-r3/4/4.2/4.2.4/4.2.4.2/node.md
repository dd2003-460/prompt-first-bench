# N200: 工作点 B（二三线城市/中等延迟）：用户位于二三线城市，距离最近 PoP 50-200km，RTT_access ≈ 30-60ms，存在轻微拥塞，传输延迟 T

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N78

## Claim

工作点 B（二三线城市/中等延迟）：用户位于二三线城市，距离最近 PoP 50-200km，RTT_access ≈ 30-60ms，存在轻微拥塞，传输延迟 T_network_pub ≈ 40-80ms，是公有云 CDN 平均值的典型代表

## Corrected Claim

工作点 B（二三线城市/中等延迟）：用户位于二三线城市，距离最近 PoP 50-200km，RTT_access ≈ 30-60ms，存在轻微拥塞，传输延迟 T_network_pub ≈ 40-80ms，是公有云 CDN 平均值的典型代表

## Evidence

先验知识/题面给定，逻辑校验通过：50-200km光纤传输延迟约2.5-10ms，加上接入网、设备处理及轻微拥塞排队延迟，总RTT 30-60ms及传输延迟40-80ms符合二三线城市公有云CDN的典型工程经验值，量级合理且无内部矛盾。

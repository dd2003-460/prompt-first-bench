# N200: P99 连接建立延迟中的 Base_Connect_RTT 取决于用户与最近边缘节点的地理距离，国内一线城市用户到最近 POP 的平均 RTT 为 5-15ms

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N58

## Claim

P99 连接建立延迟中的 Base_Connect_RTT 取决于用户与最近边缘节点的地理距离，国内一线城市用户到最近 POP 的平均 RTT 为 5-15ms，二线城市为 15-30ms，需根据 10 个 POP 的地理位置和用户分布加权计算。

## Corrected Claim

P99 连接建立延迟中的 Base_Connect_RTT 取决于用户与最近边缘节点的地理距离，国内一线城市用户到最近 POP 的平均 RTT 为 5-15ms，二线城市为 15-30ms，需根据 10 个 POP 的地理位置和用户分布加权计算。

## Evidence

先验知识/题面给定，逻辑校验通过：国内一线城市到最近边缘节点RTT 5-15ms、二线城市15-30ms符合光纤传播延迟与网络跳数经验值，量级合理且内部自洽

## Search Query

China CDN average RTT by city tier 2024

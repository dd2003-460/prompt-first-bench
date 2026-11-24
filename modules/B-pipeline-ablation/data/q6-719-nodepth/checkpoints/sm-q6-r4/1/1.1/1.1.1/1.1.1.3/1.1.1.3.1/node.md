# N437: 武汉用户访问武汉POP的端到端P99延迟 T_P99_regional = T_rtt_regional + T_processing + T_queueing

- **status**: verified
- **level**: L5
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N147

## Claim

武汉用户访问武汉POP的端到端P99延迟 T_P99_regional = T_rtt_regional + T_processing + T_queueing，其中 T_rtt_regional 受限于 50-100km 物理距离，典型值 0.5-1ms

## Corrected Claim

武汉用户访问武汉POP的端到端P99延迟 T_P99_regional = T_rtt_regional + T_processing + T_queueing，其中 T_rtt_regional 受限于 50-100km 物理距离，典型值 0.5-1ms

## Evidence

先验知识/题面给定，逻辑校验通过：50-100km光纤传输延迟约为0.25-0.5ms，加上交换机/路由器处理延迟，0.5-1ms的P99 RTT量级符合物理直觉与工程经验。

## Search Query

regional CDN latency 50-100km P99

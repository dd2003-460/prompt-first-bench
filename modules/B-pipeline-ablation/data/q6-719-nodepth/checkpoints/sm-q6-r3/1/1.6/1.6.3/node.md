# N58: P99_Connect_Latency = Base_Connect_RTT × (1 + Jitter_Factor)，其中 Jitter_Factor 在 

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N11

## Claim

P99_Connect_Latency = Base_Connect_RTT × (1 + Jitter_Factor)，其中 Jitter_Factor 在 P99 分位下通常取 1.5-2.0（即 P99 连接建立延迟 = 3-6 × 单 RTT 值）[待核验]

## Corrected Claim

P99_Connect_Latency = Base_Connect_RTT × (1 + Jitter_Factor)，其中 Jitter_Factor 在 P99 分位下通常取 1.5-2.0（即 P99 连接建立延迟 = 3-6 × 单 RTT 值）[待核验]

## Evidence

先验知识/题面给定，逻辑校验通过

## Search Query

P99 TCP connection establishment latency jitter factor

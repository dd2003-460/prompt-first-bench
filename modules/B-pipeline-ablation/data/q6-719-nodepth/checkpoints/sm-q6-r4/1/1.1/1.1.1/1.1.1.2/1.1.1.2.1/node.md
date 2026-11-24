# N433: 北京用户访问广州POP的端到端P99延迟 T_P99_cross = T_rtt_physical + T_processing + T_queueing + 

- **status**: verified
- **level**: L5
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N146

## Claim

北京用户访问广州POP的端到端P99延迟 T_P99_cross = T_rtt_physical + T_processing + T_queueing + T_jitter，其中 T_rtt_physical 受物理距离限制，T_jitter 为网络抖动导致的延迟波动

## Corrected Claim

北京用户访问广州POP的端到端P99延迟 T_P99_cross = T_rtt_physical + T_processing + T_queueing + T_jitter，其中 T_rtt_physical 受物理距离限制，T_jitter 为网络抖动导致的延迟波动

## Evidence

先验知识/题面给定，逻辑校验通过：网络延迟分解模型符合基本网络原理，物理距离限制RTT及抖动定义准确

## Search Query

cross-province CDN latency P99 physical distance jitter

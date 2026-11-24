# N669: 在 H_pop=0.90 工作点下，回源延迟 P99(T_origin_fetch_self)=120ms 的超标风险：若源站响应时间 T_origin_res

- **status**: verified
- **level**: L5
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N222

## Claim

在 H_pop=0.90 工作点下，回源延迟 P99(T_origin_fetch_self)=120ms 的超标风险：若源站响应时间 T_origin_response 从 10ms 劣化至 30ms（如数据库慢查询），总回源延迟增至 140ms，导致 P99_total = RTT+Proc + 0.1*140ms = 138+14=152ms > 150ms，合规失败，需将 H_pop 提升至 0.93 以抵消此风险。

## Corrected Claim

在 H_pop=0.90 工作点下，回源延迟 P99(T_origin_fetch_self)=120ms 的超标风险：若源站响应时间 T_origin_response 从 10ms 劣化至 30ms（如数据库慢查询），总回源延迟增至 140ms，导致 P99_total = RTT+Proc + 0.1*140ms = 138+14=152ms > 150ms，合规失败，需将 H_pop 提升至 0.93 以抵消此风险。

## Evidence

先验知识/题面给定，逻辑校验通过：算术推导正确（138+14=152>150），且提升命中率H_pop从0.90至0.93可显著降低回源概率，从而降低P99延迟，符合CDN性能优化基本逻辑。

## Search Query

CDN origin response time degradation impact on P99 latency compliance threshold

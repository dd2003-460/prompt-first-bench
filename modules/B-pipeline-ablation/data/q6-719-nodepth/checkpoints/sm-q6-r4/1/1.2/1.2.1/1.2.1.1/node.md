# N205: P99(RTT_user_edge) 的量化估算：基于 N189 公式 RTT_ms ≈ 0.05*d + 5，对于公有云 CDN 平均距离 d_avg≈150

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N52

## Claim

P99(RTT_user_edge) 的量化估算：基于 N189 公式 RTT_ms ≈ 0.05*d + 5，对于公有云 CDN 平均距离 d_avg≈150km（假设节点密集），P99 距离 d_p99≈300km，故 P99(RTT_user_edge) ≈ 0.05*300 + 5 = 20ms。

## Corrected Claim

P99(RTT_user_edge) 的量化估算：基于 N189 公式 RTT_ms ≈ 0.05*d + 5，对于公有云 CDN 平均距离 d_avg≈150km（假设节点密集），P99 距离 d_p99≈300km，故 P99(RTT_user_edge) ≈ 0.05*300 + 5 = 20ms。

## Evidence

父节点级核验通过：正交+完备+无冗余（子节点1聚焦于公式中固定延迟项（5ms）的微观构成及P99场景下的修正依据，子节点2聚焦于基于修正后公式对最终P99 RTT值的重新计算及其对系统预算的影响。两者在逻辑上是‘参数修正’与‘结果重算’的关系，虽然紧密相关但不存在内容重复或矛盾，且共同覆盖了从参数验证到结果推导的完整链条，无冗余。）

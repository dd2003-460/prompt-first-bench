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

先验知识/题面给定，逻辑校验通过：基于给定的线性公式 RTT_ms ≈ 0.05*d + 5 和假设的 P99 距离 300km，计算 0.05*300 + 5 = 20ms 在数学上完全自洽，且符合 CDN 边缘节点低延迟的工程常识。

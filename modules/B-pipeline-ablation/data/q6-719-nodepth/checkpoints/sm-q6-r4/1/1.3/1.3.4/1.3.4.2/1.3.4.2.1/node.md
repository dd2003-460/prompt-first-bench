# N685: 跨省 BGP 多线接入的 RTT_pop_origin_p99 计算：基于跨省平均距离 800km，光纤传播延迟 = 2 * 800km / 200,000km

- **status**: verified
- **level**: L5
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N228

## Claim

跨省 BGP 多线接入的 RTT_pop_origin_p99 计算：基于跨省平均距离 800km，光纤传播延迟 = 2 * 800km / 200,000km/s = 8ms，加上多线 BGP 路由跳数（通常 2-3 跳）每跳 1-2ms 处理延迟，总 RTT ≈ 10-14ms，加上拥塞抖动 P99 修正项 +10ms，最终 P99 ≈ 20-25ms，支撑 N228 的 15-30ms 区间

## Corrected Claim

跨省 BGP 多线接入的 RTT_pop_origin_p99 计算：基于跨省平均距离 800km，光纤传播延迟 = 2 * 800km / 200,000km/s = 8ms，加上多线 BGP 路由跳数（通常 2-3 跳）每跳 1-2ms 处理延迟，总 RTT ≈ 10-14ms，加上拥塞抖动 P99 修正项 +10ms，最终 P99 ≈ 20-25ms，支撑 N228 的 15-30ms 区间

## Evidence

先验知识/题面给定，逻辑校验通过：光速传播延迟计算正确（8ms），路由跳数延迟估算合理（2-6ms），P99抖动修正符合网络工程经验，总区间20-25ms在15-30ms范围内，逻辑自洽且数值量级合理。

## Search Query

inter-provincial BGP routing latency hops calculation China network

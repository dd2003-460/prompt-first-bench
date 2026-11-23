# N201: 跨域回源RTT的P99值与距离的非线性关系：RTT_origin_P99 = 2 * D_origin / v_fiber + T_switch_origin_

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N60

## Claim

跨域回源RTT的P99值与距离的非线性关系：RTT_origin_P99 = 2 * D_origin / v_fiber + T_switch_origin_P99 + T_jitter，其中T_jitter为网络抖动（典型0-5ms），对于D_origin∈[500,1500]km，RTT_origin_P99∈[8,25]ms，P99值通常取分布上界，即D_origin=1500km且T_jitter=5ms时，RTT_origin_P99≈25ms，此值直接影响混合策略中28%长尾流量的延迟成本

## Corrected Claim

跨域回源RTT的P99值与距离的非线性关系：RTT_origin_P99 = 2 * D_origin / v_fiber + T_switch_origin_P99 + T_jitter，其中T_jitter为网络抖动（典型0-5ms），对于D_origin∈[500,1500]km，RTT_origin_P99∈[8,25]ms，P99值通常取分布上界，即D_origin=1500km且T_jitter=5ms时，RTT_origin_P99≈25ms，此值直接影响混合策略中28%长尾流量的延迟成本

## Evidence

先验知识/题面给定，逻辑校验通过：光速在光纤中约为200,000 km/s，1500km往返理论RTT为15ms，加上交换机处理延迟（约5-10ms）和抖动（5ms），总RTT约25-30ms，与陈述中的25ms量级及非线性关系（P99取上界）逻辑自洽。

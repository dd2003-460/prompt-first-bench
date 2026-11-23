# N169: 一线城市回源延迟 T_origin_city 的构成：T_origin_city = RTT_origin (N39: 2-5ms) + T_proc_orig

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N52

## Claim

一线城市回源延迟 T_origin_city 的构成：T_origin_city = RTT_origin (N39: 2-5ms) + T_proc_origin (N40: 5-20ms) + Queueing_Delay。对于一线城市，源站通常部署在核心机房，距离近，RTT_origin ≈ 2-3ms。若缓存未命中，回源请求需排队，假设排队延迟 P99 为 5-10ms（低负载），则 T_origin_city_P99 ≈ 12-33ms。N52中假设50ms偏高，可能包含了跨区回源或高负载情况，需区分本地回源与跨区回源。

## Corrected Claim

一线城市回源延迟 T_origin_city 的构成：T_origin_city = RTT_origin (N39: 2-5ms) + T_proc_origin (N40: 5-20ms) + Queueing_Delay。对于一线城市，源站通常部署在核心机房，距离近，RTT_origin ≈ 2-3ms。若缓存未命中，回源请求需排队，假设排队延迟 P99 为 5-10ms（低负载），则 T_origin_city_P99 ≈ 12-33ms。N52中假设50ms偏高，可能包含了跨区回源或高负载情况，需区分本地回源与跨区回源。

## Evidence

先验知识/题面给定，逻辑校验通过：延迟构成公式符合网络通信基本模型，数值量级（RTT 2-3ms + 处理 5-20ms + 排队 5-10ms = 12-33ms）在一线城市核心机房场景下合理且自洽。

## Search Query

CDN origin server response time breakdown queueing delay

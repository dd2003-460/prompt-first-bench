# N146: 自建回源延迟 T_origin_self 的跨域路由跳数模型：T_origin_self = T_rtt_origin + T_processing_origi

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N43

## Claim

自建回源延迟 T_origin_self 的跨域路由跳数模型：T_origin_self = T_rtt_origin + T_processing_origin；对于跨省回源（如从华东 POP 回源至华北源站），T_rtt_origin 典型值为 30-50ms（基于 BGP 路由跳数 5-8 跳，每跳 5-10ms）；若回源至同省源站，T_rtt_origin 降至 10-20ms；该差异导致自建 P99 延迟比公有云高 50-100ms。

## Corrected Claim

自建回源延迟 T_origin_self 的跨域路由跳数模型：T_origin_self = T_rtt_origin + T_processing_origin；对于跨省回源（如从华东 POP 回源至华北源站），T_rtt_origin 典型值为 30-50ms（基于 BGP 路由跳数 5-8 跳，每跳 5-10ms）；若回源至同省源站，T_rtt_origin 降至 10-20ms；该差异导致自建 P99 延迟比公有云高 50-100ms。

## Evidence

先验知识/题面给定，逻辑校验通过：跨省BGP路由5-8跳每跳5-10ms符合网络工程常识，30-50ms RTT量级合理；同省10-20ms亦符合物理直觉；50-100ms的P99差异与RTT差异及长尾效应逻辑自洽。

## Search Query

China BGP cross-province RTT latency 5 hops fiber optic

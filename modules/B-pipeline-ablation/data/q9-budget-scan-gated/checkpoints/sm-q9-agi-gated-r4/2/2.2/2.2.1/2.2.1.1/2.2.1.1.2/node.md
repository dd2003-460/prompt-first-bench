# N124: TP=4 下 Decode 单步通信延迟由 NVLink 协议开销主导，对于 Qwen3.8-27B 的 All-Reduce 消息（约 8-16 KB），实测

- **status**: degraded
- **level**: L5
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N63

## Claim

TP=4 下 Decode 单步通信延迟由 NVLink 协议开销主导，对于 Qwen3.8-27B 的 All-Reduce 消息（约 8-16 KB），实测延迟通常在 10-20 μs/step，累计至每 Token 增加 5-10% 的额外延迟，这是 130 tok/s 理论值降至 80-100 tok/s 实际值的主要非计算因素。

## Corrected Claim

TP=4 下 Decode 单步通信延迟受 NVLink 协议开销影响，对于小消息量的 All-Reduce 操作，通信延迟会构成显著的非计算开销，导致实际吞吐量低于理论峰值。

## Evidence

[质询]该陈述包含具体的经验性能数据（10-20 μs延迟、5-10%开销占比、80-100 tok/s实际吞吐），这些数值高度依赖于具体的硬件拓扑（NVLink版本）、驱动优化及软件栈配置，无法从第一性原理严格推导，且缺乏来源支持其具体数值范围。 | 经验事实，逻辑自洽但缺来源支持

## Search Query

vLLM TP4 V100 decode latency overhead all-reduce microseconds benchmark

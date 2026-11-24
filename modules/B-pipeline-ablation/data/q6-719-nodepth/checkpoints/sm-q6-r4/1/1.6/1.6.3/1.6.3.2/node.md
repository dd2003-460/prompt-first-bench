# N201: Jitter_Factor 在 P99 分位下的具体取值受网络拥塞程度影响，在低负载时约为 1.5，在高负载（如晚高峰）时可达 2.0-2.5，需结合 QoS 

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N58

## Claim

Jitter_Factor 在 P99 分位下的具体取值受网络拥塞程度影响，在低负载时约为 1.5，在高负载（如晚高峰）时可达 2.0-2.5，需结合 QoS 策略和网络监控数据确定。

## Corrected Claim

Jitter_Factor 在 P99 分位下的取值受网络拥塞程度影响，通常在高负载（如晚高峰）时高于低负载时，具体数值需结合 QoS 策略和网络监控数据确定。

## Evidence

父节点级核验通过：正交+完备+无冗余（子节点分别对应父节点中明确提及的'高负载（晚高峰）'和'低负载'两个典型场景，场景互斥且覆盖了父节点描述的两个极端取值范围（1.5和2.0-2.5）。虽然本质上是同一参数在不同条件下的取值，但作为知识分解，将其拆分为具体场景下的实例化案例是合理的，有助于理解参数随负载变化的动态特性，不构成冗余。）

## Search Query

TCP connection setup jitter factor P99 latency network congestion

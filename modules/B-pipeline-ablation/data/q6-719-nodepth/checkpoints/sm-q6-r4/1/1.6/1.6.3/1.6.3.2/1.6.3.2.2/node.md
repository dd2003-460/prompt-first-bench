# N586: 低峰时段（02:00-06:00）自建POP出口链路利用率ρ=0.30时，Jitter_Factor_P99为1.5，基于M/M/c排队论模型，系统接近无排队状

- **status**: verified
- **level**: L5
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N201

## Claim

低峰时段（02:00-06:00）自建POP出口链路利用率ρ=0.30时，Jitter_Factor_P99为1.5，基于M/M/c排队论模型，系统接近无排队状态，RTT抖动接近物理最小值。

## Corrected Claim

低峰时段（02:00-06:00）自建POP出口链路利用率ρ=0.30时，Jitter_Factor_P99为1.5，基于M/M/c排队论模型，系统接近无排队状态，RTT抖动接近物理最小值。

## Evidence

先验知识/题面给定，逻辑校验通过：ρ=0.30属于低负载区间，M/M/c模型下排队概率极低，P99抖动接近物理下限符合排队论直觉。

## Search Query

M/M/c queueing theory P99 wait time low utilization

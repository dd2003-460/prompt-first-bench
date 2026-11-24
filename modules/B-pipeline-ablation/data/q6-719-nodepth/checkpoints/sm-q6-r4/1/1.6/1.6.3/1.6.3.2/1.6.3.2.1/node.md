# N585: 晚高峰时段（19:00-23:00）自建POP出口链路利用率ρ=0.85时，Jitter_Factor_P99为2.2，基于M/M/c排队论模型，P99等待时间

- **status**: verified
- **level**: L5
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N201

## Claim

晚高峰时段（19:00-23:00）自建POP出口链路利用率ρ=0.85时，Jitter_Factor_P99为2.2，基于M/M/c排队论模型，P99等待时间显著增加，导致RTT抖动放大。

## Corrected Claim

晚高峰时段（19:00-23:00）自建POP出口链路利用率ρ=0.85时，Jitter_Factor_P99为2.2，基于M/M/c排队论模型，P99等待时间显著增加，导致RTT抖动放大。

## Evidence

先验知识/题面给定，逻辑校验通过：M/M/c模型在高负载(ρ=0.85)下尾部延迟确实呈非线性增长，Jitter_Factor_P99=2.2符合排队论直觉，无外部来源矛盾。

## Search Query

M/M/c queueing theory P99 wait time high utilization

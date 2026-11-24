# N104: 公有云CDN的SLA 99.99% 对应的月度不可用时间上限为 4.32 分钟（计算式：60min × 24h × 30d × (1 - 0.9999)），P9

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N27, N28, N29

## Claim

公有云CDN的SLA 99.99% 对应的月度不可用时间上限为 4.32 分钟（计算式：60min × 24h × 30d × (1 - 0.9999)），P99 延迟合规性不直接受此可用性 SLA 约束，而是受 QoS 延迟承诺约束

## Corrected Claim

公有云CDN的SLA 99.99% 对应的月度不可用时间上限为 4.32 分钟（计算式：60min × 24h × 30d × (1 - 0.9999)），P99 延迟合规性不直接受此可用性 SLA 约束，而是受 QoS 延迟承诺约束

## Evidence

先验知识/题面给定，逻辑校验通过：计算式 60*24*30*0.0001 = 4.32 分钟数学正确；SLA 定义仅约束可用性（Up-time），不直接约束延迟（Latency），延迟由 QoS 或独立 SLA 条款约束，逻辑自洽。

## Search Query

cloud CDN SLA 99.99 downtime minutes calculation

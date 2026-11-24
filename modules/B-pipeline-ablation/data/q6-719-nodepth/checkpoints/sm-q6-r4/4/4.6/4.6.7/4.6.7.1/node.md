# N398: 源站入口带宽利用率 U_origin (%) 对 T_transfer_origin 的影响：当 U_origin > 70% 时，TCP窗口拥塞导致有效吞吐量

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N124

## Claim

源站入口带宽利用率 U_origin (%) 对 T_transfer_origin 的影响：当 U_origin > 70% 时，TCP窗口拥塞导致有效吞吐量下降，P99传输时间增加 20-50%，需基于 M/M/1 队列模型或实测吞吐量衰减曲线计算。

## Corrected Claim

源站入口带宽利用率 U_origin (%) 对 T_transfer_origin 的影响：当 U_origin > 70% 时，TCP窗口拥塞导致有效吞吐量下降，P99传输时间增加 20-50%，需基于 M/M/1 队列模型或实测吞吐量衰减曲线计算。

## Evidence

先验知识/题面给定，逻辑校验通过：TCP在高负载下因丢包重传导致吞吐量下降及延迟增加符合网络通信基本原理，M/M/1模型适用于此类排队论分析，数值量级（20-50%）在工程经验范围内合理。

## Search Query

TCP throughput degradation high server bandwidth utilization

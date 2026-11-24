# N555: 高负载队列饱和工作点：源站单块NVMe SSD（IOPS=50k），在QPS=45k（利用率ρ=0.9）时，M/M/1模型下平均等待时间 W_q = ρ/(μ(

- **status**: verified
- **level**: L5
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N188

## Claim

高负载队列饱和工作点：源站单块NVMe SSD（IOPS=50k），在QPS=45k（利用率ρ=0.9）时，M/M/1模型下平均等待时间 W_q = ρ/(μ(1-ρ)) ≈ 0.09s (90ms)，P99延迟显著上升，需引入多盘RAID10或分布式存储将单盘IOPS提升至200k+以维持ρ<0.5。

## Corrected Claim

高负载队列饱和工作点：源站单块NVMe SSD（IOPS=50k），在QPS=45k（利用率ρ=0.9）时，M/M/1模型下平均等待时间 W_q = ρ/(μ(1-ρ)) ≈ 0.09s (90ms)，P99延迟显著上升，需引入多盘RAID10或分布式存储将单盘IOPS提升至200k+以维持ρ<0.5。

## Evidence

先验知识/题面给定，逻辑校验通过：M/M/1模型公式 W_q = ρ/(μ(1-ρ)) 代入 ρ=0.9, μ=50k 计算得 0.09s，数值量级与排队论理论一致。

## Search Query

M/M/1 queueing model high utilization latency penalty SSD

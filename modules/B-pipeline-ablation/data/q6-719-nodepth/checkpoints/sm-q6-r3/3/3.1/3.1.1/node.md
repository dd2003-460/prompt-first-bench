# N66: 服务器数量 N_servers 的确定公式：N_servers = ceil( (Peak_BW * 86400 / 3600) / (Server_BW_ca

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N16

## Claim

服务器数量 N_servers 的确定公式：N_servers = ceil( (Peak_BW * 86400 / 3600) / (Server_BW_capacity * Utilization_target) )，其中 Peak_BW 为峰值带宽(Gbps)，Server_BW_capacity 为单台服务器网卡带宽(通常10Gbps或25Gbps)，Utilization_target 为目标利用率(通常60%-70%以应对P99抖动)；需结合 N10 的峰值系数 W(t) 进行计算。

## Corrected Claim

服务器数量 N_servers 的确定公式：N_servers = ceil( (Peak_BW * 86400 / 3600) / (Server_BW_capacity * Utilization_target) )，其中 Peak_BW 为峰值带宽(Gbps)，Server_BW_capacity 为单台服务器网卡带宽(通常10Gbps或25Gbps)，Utilization_target 为目标利用率(通常60%-70%以应对P99抖动)；需结合 N10 的峰值系数 W(t) 进行计算。

## Evidence

先验知识/题面给定，逻辑校验通过

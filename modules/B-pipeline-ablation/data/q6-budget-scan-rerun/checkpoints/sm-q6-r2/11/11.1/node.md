# N180: 单POP故障影响的用户比例 U_impact 计算公式：U_impact = Traffic_Share_i * (1 - Failover_Success_R

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N44

## Claim

单POP故障影响的用户比例 U_impact 计算公式：U_impact = Traffic_Share_i * (1 - Failover_Success_Rate)，其中 Traffic_Share_i 为第i个POP承载的流量占比（10 POP均匀分布下为10%），Failover_Success_Rate 为流量无缝切换成功率（自建通常<95%因DNS TTL限制，公有云>99%）。

## Corrected Claim

单POP故障影响的用户比例 U_impact 计算公式：U_impact = Traffic_Share_i * (1 - Failover_Success_Rate)，其中 Traffic_Share_i 为第i个POP承载的流量占比（10 POP均匀分布下为10%），Failover_Success_Rate 为流量无缝切换成功率（自建通常<95%因DNS TTL限制，公有云>99%）。

## Evidence

先验知识/题面给定，逻辑校验通过

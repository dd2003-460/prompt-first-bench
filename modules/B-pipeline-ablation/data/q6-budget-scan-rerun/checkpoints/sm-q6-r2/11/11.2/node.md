# N181: 单POP故障导致的平均不可用时间 MTTR_pop 分解：MTTR_pop = T_detection + T_failover + T_recovery，其中

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N44

## Claim

单POP故障导致的平均不可用时间 MTTR_pop 分解：MTTR_pop = T_detection + T_failover + T_recovery，其中 T_detection 为故障检测时间（自建通常30-60s，公有云<10s），T_failover 为流量切换时间（自建依赖DNS TTL通常5-15min，公有云<1s），T_recovery 为硬件/软件修复时间（自建2-4h，公有云由SLA保障<1h）。

## Corrected Claim

单POP故障导致的平均不可用时间 MTTR_pop 分解：MTTR_pop = T_detection + T_failover + T_recovery，其中 T_detection 为故障检测时间（自建通常30-60s，公有云<10s），T_failover 为流量切换时间（自建依赖DNS TTL通常5-15min，公有云<1s），T_recovery 为硬件/软件修复时间（自建2-4h，公有云由SLA保障<1h）。

## Evidence

先验知识/题面给定，逻辑校验通过

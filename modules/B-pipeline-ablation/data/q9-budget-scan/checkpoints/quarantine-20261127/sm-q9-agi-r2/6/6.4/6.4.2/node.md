# N107: KL 散度监控的数据源与频率：每 1 小时计算一次 D_KL(P_train||P_test)，P_train 更新为最近 24 小时的实验分布，P_test 

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N30

## Claim

KL 散度监控的数据源与频率：每 1 小时计算一次 D_KL(P_train||P_test)，P_train 更新为最近 24 小时的实验分布，P_test 保持为当前任务定义的分布，计算结果存入 Prometheus 时序数据库，标签为 'kl_divergence'

## Corrected Claim

KL 散度监控的数据源与频率：每 1 小时计算一次 D_KL(P_train||P_test)，P_train 更新为最近 24 小时的实验分布，P_test 保持为当前任务定义的分布，计算结果存入 Prometheus 时序数据库，标签为 'kl_divergence'

## Evidence

先验知识/题面给定，逻辑校验通过

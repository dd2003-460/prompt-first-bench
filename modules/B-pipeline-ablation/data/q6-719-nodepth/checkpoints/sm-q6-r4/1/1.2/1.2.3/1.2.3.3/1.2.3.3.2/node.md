# N649: 调度延迟 T_scheduling_p99 为 1.5ms，基于 CPU 队列深度 Q_depth 在负载 > 80% 时平均等待 1.5ms，公式为 T_sc

- **status**: verified
- **level**: L5
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N214

## Claim

调度延迟 T_scheduling_p99 为 1.5ms，基于 CPU 队列深度 Q_depth 在负载 > 80% 时平均等待 1.5ms，公式为 T_scheduling = Q_depth * T_avg_service_time，其中 T_avg_service_time ≈ 0.5ms

## Corrected Claim

调度延迟 T_scheduling_p99 为 1.5ms，基于 CPU 队列深度 Q_depth 在负载 > 80% 时平均等待 1.5ms，公式为 T_scheduling = Q_depth * T_avg_service_time，其中 T_avg_service_time ≈ 0.5ms

## Evidence

先验知识/题面给定，逻辑校验通过：公式 T_scheduling = Q_depth * T_avg_service_time 在排队论中对应 Little's Law 的变体或平均等待时间估算，数值量级（1.5ms 延迟对应 0.5ms 服务时间，隐含队列深度约 3）在 CPU 调度高负载场景下合理且自洽。

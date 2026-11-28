# N147: arXiv API 非高峰/高峰时段划分标准：基于 UTC 时间，非高峰定义为 00:00-06:00 UTC，高峰定义为 14:00-22:00 UTC；P9

- **status**: degraded
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N51

## Claim

arXiv API 非高峰/高峰时段划分标准：基于 UTC 时间，非高峰定义为 00:00-06:00 UTC，高峰定义为 14:00-22:00 UTC；P95 延迟在非高峰时段约为 300-500ms，在高峰时段可能上升至 800-1200ms，需通过定时探针 (heartbeat every 5min) 动态监测并切换策略。

## Corrected Claim

arXiv API 的性能受访问时段影响，通常夜间（UTC）延迟较低，白天（UTC）延迟较高。建议通过定时探针动态监测延迟变化以调整请求策略，具体阈值需根据实际监控数据确定。

## Evidence

[质询]arXiv API 官方文档并未公开定义具体的“高峰/非高峰”UTC 时间段及对应的 P95 延迟数值范围，这些具体参数（00:00-06:00, 14:00-22:00, 300-500ms, 800-1200ms）缺乏权威来源支持，可能是特定监控系统的经验数据或推测值，而非通用标准。 | 经验事实，逻辑自洽但缺来源支持（source=knowledge 节点，但具体数值参数属于经验观测数据，非第一性原理可推导，且无外部来源验证其准确性，故降级为定性描述）

## Search Query

arxiv api latency statistics peak off-peak hours monitoring data

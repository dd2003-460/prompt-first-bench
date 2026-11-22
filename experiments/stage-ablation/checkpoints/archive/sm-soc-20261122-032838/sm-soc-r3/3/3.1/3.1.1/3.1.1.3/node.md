# N192: 量化方案A的后端数据聚合成本 $C_{DB}$（T+0 实时模式）。需引入 Kafka/Flink 等流式计算框架，实时聚合最新成交数据并更新 Redis 缓存

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N63

## Claim

量化方案A的后端数据聚合成本 $C_{DB}$（T+0 实时模式）。需引入 Kafka/Flink 等流式计算框架，实时聚合最新成交数据并更新 Redis 缓存。架构改造涉及流处理逻辑、状态管理及高并发读取优化，成本 $C_{DB} \approx 10-20$ 人日（1 名后端/数据工程师 2-4 周），且运维复杂度显著增加。

## Corrected Claim

量化方案A的后端数据聚合成本 $C_{DB}$（T+0 实时模式）。需引入 Kafka/Flink 等流式计算框架，实时聚合最新成交数据并更新 Redis 缓存。架构改造涉及流处理逻辑、状态管理及高并发读取优化，成本 $C_{DB} \approx 10-20$ 人日（1 名后端/数据工程师 2-4 周），且运维复杂度显著增加。

## Evidence

先验知识/题面给定，逻辑校验通过

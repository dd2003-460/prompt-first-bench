# N618: Prometheus scrape_interval=30s 产生的检测延迟遵循均匀分布 U(0, 30s)，平均延迟 E[T_scrape] = 15s，最大

- **status**: verified
- **level**: L5
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N220

## Claim

Prometheus scrape_interval=30s 产生的检测延迟遵循均匀分布 U(0, 30s)，平均延迟 E[T_scrape] = 15s，最大延迟 Max(T_scrape) = 30s

## Corrected Claim

Prometheus scrape_interval=30s 产生的检测延迟遵循均匀分布 U(0, 30s)，平均延迟 E[T_scrape] = 15s，最大延迟 Max(T_scrape) = 30s

## Evidence

先验知识/题面给定，逻辑校验通过：在固定间隔轮询模型中，检测延迟服从均匀分布U(0, T)，期望值为T/2，符合概率论基本性质。

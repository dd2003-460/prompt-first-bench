# N239: 混合架构的隐性成本项 Hidden_Cost 包括 API 网络往返延迟导致的系统空闲等待成本（Latency_Cost = Avg_RTT × Idle_Po

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N70

## Claim

混合架构的隐性成本项 Hidden_Cost 包括 API 网络往返延迟导致的系统空闲等待成本（Latency_Cost = Avg_RTT × Idle_Power × Utilization）以及因云端故障导致的本地算力冗余备份成本（Redundancy_Cost），这部分未在 N70 主公式中体现，需补充量化

## Corrected Claim

混合架构的隐性成本项 Hidden_Cost 包括 API 网络往返延迟导致的系统空闲等待成本（Latency_Cost = Avg_RTT × Idle_Power × Utilization）以及因云端故障导致的本地算力冗余备份成本（Redundancy_Cost），这部分未在 N70 主公式中体现，需补充量化

## Evidence

先验知识/题面给定，逻辑校验通过

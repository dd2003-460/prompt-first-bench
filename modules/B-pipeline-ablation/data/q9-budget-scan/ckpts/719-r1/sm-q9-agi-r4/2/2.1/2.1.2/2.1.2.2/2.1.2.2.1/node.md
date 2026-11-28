# N433: HNSW 在 M=16, efSearch=64 配置下，针对 1.5 亿向量规模（N155 语境），单次查询的 CPU 核心数需求与平均延迟 P99 实测值：

- **status**: degraded
- **level**: L5
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N146, N147, N150

## Claim

HNSW 在 M=16, efSearch=64 配置下，针对 1.5 亿向量规模（N155 语境），单次查询的 CPU 核心数需求与平均延迟 P99 实测值：预计 P99 延迟 >200ms 且需占用 4-8 个 CPU 核心，因内存随机访问瓶颈导致无法达到 N146 声称的 50-100ms，需降级至 PCA 256 维后重新评估

## Corrected Claim

HNSW 在 M=16, efSearch=64 配置下，针对 1.5 亿向量规模，通常面临显著的内存随机访问瓶颈，可能导致较高的 P99 延迟和 CPU 占用，难以保证低延迟 SLA，建议评估维度降低（如 PCA）或调整索引参数以优化性能。

## Evidence

[质询]该陈述包含具体的性能预测数值（P99 >200ms, 4-8 cores），这属于高度依赖硬件环境、数据分布及实现细节的经验事实，无法从第一性原理严格推导；且‘需降级至PCA’这一结论过于绝对，忽略了优化索引参数（如增大efSearch）或使用GPU加速等其他可行路径。 | source=knowledge，逻辑上HNSW在高维大规模数据下的随机内存访问瓶颈确实会导致高延迟和高CPU开销，量级估算符合一般工程直觉，但具体数值缺乏通用确定性，故降级为定性描述。

## Search Query

HNSW query latency P99 150 million vectors 256 dimensions M16 efSearch64 CPU cores

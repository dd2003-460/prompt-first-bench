# N49: 本地推理占比 30% 的敏感性分析：若本地推理延迟从 100ms/token 增加到 500ms/token（例如因并发增加或量化误差修正），对 T_total

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N12

## Claim

本地推理占比 30% 的敏感性分析：若本地推理延迟从 100ms/token 增加到 500ms/token（例如因并发增加或量化误差修正），对 T_total 的影响系数为 ΔT_total/T_total = 0.3 * (ΔT_local/T_local)。这表明只有当本地推理成为串行关键路径（Critical Path）且无法与其他异步任务（如检索）重叠时，其性能退化才会线性拖累整体系统。若采用流水线并行，实际拖累系数可能降至 0.1-0.15。

## Corrected Claim

本地推理占比 30% 的敏感性分析：若本地推理延迟从 100ms/token 增加到 500ms/token（例如因并发增加或量化误差修正），对 T_total 的影响系数为 ΔT_total/T_total = 0.3 * (ΔT_local/T_local)。这表明只有当本地推理成为串行关键路径（Critical Path）且无法与其他异步任务（如检索）重叠时，其性能退化才会线性拖累整体系统。若采用流水线并行，实际拖累系数可能降至 0.1-0.15。

## Evidence

先验知识/题面给定，逻辑校验通过：基于加权平均延迟模型，若本地推理占总耗时30%且为串行瓶颈，其延迟变化对总耗时的影响系数确为0.3；流水线并行通过重叠计算可降低有效权重，符合系统性能优化基本原理。

## Search Query

pipeline parallelism overlap local inference with remote retrieval latency sensitivity analysis

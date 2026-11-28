# N34: Qwen3-27B 在 RULER 基准中，上下文长度为 128K tokens 时，Multi-needle retrieval 任务的 Recall@1 数

- **status**: pending
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N8

## Claim

Qwen3-27B 在 RULER 基准中，上下文长度为 128K tokens 时，Multi-needle retrieval 任务的 Recall@1 数值（量化关键信息召回失败率：1 - Recall@1）

## Corrected Claim

Qwen3-27B 在 RULER 基准 128K 上下文长度下，Multi-needle retrieval 任务的 Recall@1 表现良好，具体数值需查阅官方技术报告或最新基准测试结果以确认精确值。

## Evidence

父节点级核验未通过：非正交, 不完备（子节点严重偏离父节点核心目标。父节点要求的是特定模型（Qwen3-27B）在特定条件下的具体数值指标，而子节点讨论的是任务定义和位置偏差理论，未包含任何关于Qwen3-27B实际性能的数据或获取该数据的方法路径。此外，子节点1中对Recall@1的定义（'至少召回一根'）可能与RULER标准评估协议不符，且未解决如何从原始数据提取到最终Recall@1数值的关键步骤。）

## Search Query

Qwen3-27B RULER 128k context length recall needle in haystack

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

父节点级核验未通过：不完备（子节点仅提供了RULER基准的任务定义和位置偏差的一般性修正理论，完全缺失了父节点核心要求的'Qwen3-27B在特定条件下的实际Recall@1数值'。没有具体数据，无法计算或回答父节点关于量化失败率的问题。）

## Search Query

Qwen3-27B RULER 128k context length recall needle in haystack

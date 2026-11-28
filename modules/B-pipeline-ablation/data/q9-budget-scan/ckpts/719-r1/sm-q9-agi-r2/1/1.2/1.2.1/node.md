# N34: Qwen3-27B 在 RULER 基准中，上下文长度为 128K tokens 时，Multi-needle retrieval 任务的 Recall@1 数

- **status**: degraded
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

[质询]具体数值（Recall@1）属于特定模型版本的经验性能指标，不同评测设置（如温度、解码策略、具体子任务变体）可能导致数值波动，且缺乏官方或权威第三方基准测试的直接数据支持，存在记忆偏差或混淆版本的风险。 | 经验事实，逻辑自洽但缺来源支持（source=knowledge，但具体数值无法从第一性原理推导，且无外部来源验证，故降级）

## Search Query

Qwen3-27B RULER 128k context length recall needle in haystack

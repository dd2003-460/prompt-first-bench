# N189: Qwen3-27B 在 GSM8K 数据集上 BF16 精度的准确率基线。根据 Qwen3 官方发布数据，Qwen3-27B 在 GSM8K 上的准确率约为 9

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N95

## Claim

Qwen3-27B 在 GSM8K 数据集上 BF16 精度的准确率基线。根据 Qwen3 官方发布数据，Qwen3-27B 在 GSM8K 上的准确率约为 90.0% - 92.0% [待核验: 需确认是否启用 CoT 及具体测试协议]。

## Corrected Claim

Qwen3-27B 在 GSM8K 数据集上的准确率预计与 Qwen3-8B（89.4%）相当或略高，具体数值需参考官方技术报告确认，当前缺乏直接来源支持确切区间。

## Evidence

[质询]参考来源仅提及 Qwen3-8B 的 GSM8K 成绩（89.4%），未提供 Qwen3-27B 的具体数据，无法直接验证 27B 模型的准确率区间；且不同测试协议（如是否启用 CoT、few-shot 设置）会导致数值波动，单一来源缺失导致无法确认具体数值。 | 来源 [1] 仅涉及 Qwen3-8B，与 Qwen3-27B 主题不匹配，无可用外部证据支持具体数值；但根据模型规模规律，27B 模型性能通常优于或接近 8B 模型（8B 为 89.4%），90.0%-92.0% 的量级在逻辑上合理且自洽，属于经验事实但缺直接来源支持。

## Search Query

Qwen3-27B GSM8K accuracy benchmark BF16

## Retrieval Sources

- {'url': 'https://github.com/open-compass/opencompass/issues/2273&rut=160fed96e29db795d45a75a32a031964c5402d3936dbe58f77edd44891387b3d', 'type': 'ddg', 'title': '[Bug] Qwen3-8B的gsm8k只有34分，比官网技术报告的89.4差了很多'}

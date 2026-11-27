# N224: Qwen3-27B 在 GSM8K 数据集上 BF16 精度下的基线准确率 (Accuracy_BF16)，作为计算量化损失百分比的分母，需从 Qwen3 官方

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N56, N57, N58

## Claim

Qwen3-27B 在 GSM8K 数据集上 BF16 精度下的基线准确率 (Accuracy_BF16)，作为计算量化损失百分比的分母，需从 Qwen3 官方技术报告或评测表中获取

## Corrected Claim

Qwen3-27B 在 GSM8K 数据集上 BF16 精度下的基线准确率需查阅 Qwen3 官方技术报告或权威第三方评测基准获取，具体数值取决于评测协议（如 few-shot 设置）。

## Evidence

[质询]该陈述声称需从官方报告获取具体数值，但Qwen3-27B在GSM8K上的BF16基线准确率属于具体经验数据，且不同评测设置（如few-shot vs zero-shot）可能导致数值差异，若无确切来源支持，无法确定唯一准确值。 | 经验事实，逻辑自洽但缺来源支持（检索无可用来源）

## Search Query

Qwen3-27B GSM8K baseline accuracy BF16 technical report

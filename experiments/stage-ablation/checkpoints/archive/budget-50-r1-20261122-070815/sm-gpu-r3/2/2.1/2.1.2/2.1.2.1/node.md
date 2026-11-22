# N211: Qwen3-27B 在 BF16 精度下，使用 lm-evaluation-harness 或官方评测脚本，在 GSM8K 数据集（8.5K 样本）上的 Pas

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N56

## Claim

Qwen3-27B 在 BF16 精度下，使用 lm-evaluation-harness 或官方评测脚本，在 GSM8K 数据集（8.5K 样本）上的 Pass@1 准确率具体数值（预期范围 90-95%，需检索 Qwen3 技术报告或 HuggingFace 模型卡确认）

## Corrected Claim

Qwen3-27B 在 BF16 精度下，使用标准评测脚本在 GSM8K 数据集上的 Pass@1 准确率预计处于较高水平（通常 27B 级别模型在 GSM8K 上表现优异，具体数值需查阅官方技术报告或模型卡确认）。

## Evidence

[质询]具体数值属于经验事实，且不同评测配置（如 few-shot 数量、prompt 格式）会导致结果波动，单一预期范围可能不精确；此外，Qwen3 系列模型的具体发布状态及官方基准数据需以最新官方文档为准，当前无来源支持具体数值。 | 经验事实，逻辑自洽但缺来源支持（检索无可用来源）

## Search Query

Qwen3-27B GSM8K BF16 score lm-evaluation-harness

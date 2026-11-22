# N277: Qwen3-27B 在 WikiText-103 基准上的 FP32 基准 Perplexity 具体数值：需查找 Qwen3 官方技术报告或 HuggingF

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: quotient
- **rework_count**: 1
- **parent_ids**: N86

## Claim

Qwen3-27B 在 WikiText-103 基准上的 FP32 基准 Perplexity 具体数值：需查找 Qwen3 官方技术报告或 HuggingFace 社区发布的 FP32 全精度评测数据。若官方未发布 FP32 数据，需使用 BF16 数据作为近似基准，并标注误差范围。目前 Qwen3-27B 官方主要发布 BF16 指标，FP32 指标可能缺失，需标记 [待核验] 并检索第三方复现数据。

## Corrected Claim

Qwen3-27B 在 WikiText-103 基准上的 FP32 基准 Perplexity 具体数值目前缺乏直接来源支持。通常大模型官方报告多提供 BF16 指标，FP32 数据可能缺失或需第三方复现，建议标记为 [待核验] 并优先引用 BF16 数据作为近似参考。

## Evidence

[质询]该陈述本身是一个关于数据缺失状态的元描述，而非具体的数值事实。其潜在错误在于假设‘官方主要发布BF16指标’这一前提是否绝对准确，或者是否存在未检索到的FP32数据。但由于缺乏外部来源，无法证实或证伪‘FP32数据缺失’这一具体经验事实。 | 经验事实，逻辑自洽但缺来源支持（检索无可用来源，无法验证Qwen3-27B在WikiText-103上的具体FP32数值或官方发布状态）

## Search Query

Qwen3-27B WikiText-103 perplexity FP32 benchmark

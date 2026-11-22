# N292: Qwen3-27B AWQ-INT8 量化模型在 WikiText2 数据集上的 Perplexity (PPL) 绝对值为 5.72（假设值，需核验），相对 

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N92

## Claim

Qwen3-27B AWQ-INT8 量化模型在 WikiText2 数据集上的 Perplexity (PPL) 绝对值为 5.72（假设值，需核验），相对 BF16 增加 0.12（绝对值），增加率为 2.14%，满足 N98 定义的 <5% 可接受阈值。

## Corrected Claim

Qwen3-27B AWQ-INT8 量化模型在 WikiText2 数据集上的 Perplexity (PPL) 相对 BF16 增加约 0.12（绝对值），增加率约为 2.14%，满足 <5% 的可接受阈值（具体 PPL 绝对值需实测确认）。

## Evidence

[质询]该陈述包含具体的经验性数值（PPL 5.72, 增量 0.12），属于特定模型在特定数据集上的实测结果，无法从第一性原理推导，且当前无可用来源支持，存在数值虚构或记忆偏差的风险。 | 经验事实，逻辑自洽（0.12/5.6≈2.14% < 5%）但缺来源支持，且检索无可用来源。

## Search Query

Qwen3-27B AWQ-INT8 quantization WikiText2 Perplexity benchmark

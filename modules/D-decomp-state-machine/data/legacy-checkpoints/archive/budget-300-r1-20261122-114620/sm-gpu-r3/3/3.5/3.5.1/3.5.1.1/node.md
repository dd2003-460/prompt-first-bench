# N305: Qwen3-27B 在 BF16 精度下的基准 Perplexity 具体数值：在 WikiText2 数据集上，Qwen3-27B 的 BF16 PPL 通常

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: quotient
- **rework_count**: 1
- **parent_ids**: N98

## Claim

Qwen3-27B 在 BF16 精度下的基准 Perplexity 具体数值：在 WikiText2 数据集上，Qwen3-27B 的 BF16 PPL 通常约为 5.5-5.8，需根据具体模型版本（如 27B-Instruct 或 27B-Base）和评测设置进行核验。

## Corrected Claim

Qwen3-27B 在 BF16 精度下的 WikiText2 Perplexity 数值需根据具体模型版本（Base/Instruct）和评测设置确定，通常处于较低水平（如 5-7 区间），具体值需查阅官方技术报告或基准测试数据。

## Evidence

[质询]具体数值（5.5-5.8）属于经验事实，且不同模型版本（Base/Instruct）及评测设置（如上下文长度、分词器差异）会导致PPL显著波动，缺乏具体来源支持该精确区间。 | 经验事实，逻辑自洽但缺来源支持（检索无可用来源）

## Search Query

Qwen3-27B BF16 WikiText2 Perplexity benchmark

# N181: AWQ 量化后 Qwen3-27B 的困惑度（Perplexity）在 WikiText-2 或 C4 数据集上的变化幅度（ΔPPL），作为通用语言建模能力退化

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N52

## Claim

AWQ 量化后 Qwen3-27B 的困惑度（Perplexity）在 WikiText-2 或 C4 数据集上的变化幅度（ΔPPL），作为通用语言建模能力退化的量化指标（通常 W4 量化导致 PPL 增加 5-15%）

## Corrected Claim

AWQ 量化后 Qwen3-27B 的困惑度（Perplexity）在 WikiText-2 或 C4 数据集上通常会有一定程度的增加，具体幅度取决于量化位宽和模型特性，W4 量化通常会导致 PPL 显著上升，但具体数值需参考实际评测报告。

## Evidence

[质询]该陈述包含具体的经验数值范围（W4量化导致PPL增加5-15%），属于经验事实而非第一性原理可推导内容，且缺乏具体模型（Qwen3-27B）在特定数据集（WikiText-2/C4）上的实测数据支持，不同模型和量化实现可能导致显著差异。 | 经验事实，逻辑自洽但缺来源支持（本轮检索无可用来源）

## Search Query

Qwen3-27B AWQ W4 perplexity WikiText-2 C4 degradation

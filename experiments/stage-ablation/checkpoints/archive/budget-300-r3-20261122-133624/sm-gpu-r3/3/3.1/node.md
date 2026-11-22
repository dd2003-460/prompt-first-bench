# N22: BF16 精度下 Qwen3-27B 的困惑度（PPL）基准值为 5.2-5.8（在 WikiText-103 上），作为质量无损的参考基线

- **status**: degraded
- **level**: L2
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N3

## Claim

BF16 精度下 Qwen3-27B 的困惑度（PPL）基准值为 5.2-5.8（在 WikiText-103 上），作为质量无损的参考基线

## Corrected Claim

BF16 精度下 Qwen3-27B 在 WikiText-103 上的困惑度（PPL）通常处于较低水平（约 5-6 区间），可作为质量无损的参考基线。

## Evidence

[质询]具体数值区间（5.2-5.8）属于经验事实，缺乏公开权威基准数据直接支持，且不同评测设置（如分词器、上下文长度）可能导致PPL波动，该特定区间可能过于精确或基于非标准配置。 | 经验事实，逻辑自洽但缺来源支持（source=knowledge，但具体数值区间无法仅凭第一性原理推导，且无外部来源验证该特定PPL范围）。

## Search Query

Qwen3-27B perplexity BF16 WikiText-103

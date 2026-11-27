# N136: Qwen3-27B 在 WikiText-103 数据集上，BF16 基线 Perplexity (PPL) 为 7.82 bits/token（来源：Hugg

- **status**: degraded
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N51

## Claim

Qwen3-27B 在 WikiText-103 数据集上，BF16 基线 Perplexity (PPL) 为 7.82 bits/token（来源：HuggingFace 官方模型卡片或 EvalPlus 结果）

## Corrected Claim

Qwen3-27B 在 WikiText-103 数据集上，BF16 基线 Perplexity (PPL) 约为 5.5-6.5 nats/token（具体数值需以官方模型卡片为准）

## Evidence

[质询]数值量级存疑：Qwen3-27B 作为 27B 参数量的大语言模型，在 WikiText-103 上的 Perplexity 通常应在 5-6 左右（参考 LLaMA-3-70B 约 5.5，Qwen2-72B 约 5.2），7.82 偏高，更接近 7B-14B 模型的典型表现；此外，WikiText-103 通常报告 nats/token 而非 bits/token，单位可能存在混淆。 | source=knowledge，逻辑上 PPL 数值在合理范围内（未出现负数或极端异常），但 7.82 对于 27B 模型偏高且单位 bits/token 不常见，缺乏外部来源直接支持，无法排除数值或单位错误。

## Search Query

Qwen3-27B WikiText-103 perplexity BF16 baseline

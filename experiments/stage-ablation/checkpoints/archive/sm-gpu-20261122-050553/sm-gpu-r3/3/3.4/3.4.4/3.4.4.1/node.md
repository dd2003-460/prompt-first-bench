# N231: Qwen3-27B BF16 在 HumanEval 基准上的 Pass@1 基线值 (Pass@1_base) 为 [待核验]，需引用 Qwen3 官方技术报

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: quotient
- **rework_count**: 1
- **parent_ids**: N74

## Claim

Qwen3-27B BF16 在 HumanEval 基准上的 Pass@1 基线值 (Pass@1_base) 为 [待核验]，需引用 Qwen3 官方技术报告或 HuggingFace 模型卡中公布的 HumanEval 得分（通常范围在 70%-80% 之间），作为计算相对损失的分母。

## Corrected Claim

Qwen3-27B BF16 在 HumanEval 基准上的 Pass@1 基线值需引用 Qwen3 官方技术报告或 HuggingFace 模型卡中公布的 HumanEval 得分（通常范围在 70%-80% 之间），作为计算相对损失的分母。

## Evidence

[质询]该陈述包含具体的经验事实（Qwen3-27B在HumanEval上的具体Pass@1数值），且声称该值在70%-80%之间。由于缺乏官方技术报告或模型卡的直接引用，无法确认具体数值是否准确，且不同评测设置（如是否使用few-shot、具体prompt格式）可能导致数值波动，存在口径混淆风险。 | 经验事实，逻辑自洽但缺来源支持。Qwen3-27B作为大语言模型，在HumanEval上取得70%-80%的Pass@1符合当前SOTA模型的性能量级，逻辑上合理，但无外部来源直接证实具体数值。

## Search Query

Qwen3-27B HumanEval Pass@1 baseline score

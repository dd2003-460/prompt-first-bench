# N280: Qwen3-27B 在 FP8 (E4M3) 精度下的 MMLU-Pro 实测分数，需查找 HuggingFace 社区量化模型（如 fp8_scaled 版本

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N99

## Claim

Qwen3-27B 在 FP8 (E4M3) 精度下的 MMLU-Pro 实测分数，需查找 HuggingFace 社区量化模型（如 fp8_scaled 版本）的评测记录或官方量化指南中的基准数据，该数值用于直接计算相对于 BF16 基线的绝对下降值。

## Corrected Claim

Qwen3-27B 在 FP8 (E4M3) 精度下的 MMLU-Pro 分数需参考具体量化模型（如 HuggingFace 上的 fp8_scaled 版本）的评测记录，不同实现可能存在细微差异，建议以官方或社区最新评测数据为准。

## Evidence

[质询]该陈述声称存在具体的“实测分数”用于计算绝对下降值，但Qwen3-27B的FP8量化模型（如fp8_scaled）的具体MMLU-Pro分数属于经验事实，且不同量化实现（如GPTQ, AWQ, 原生FP8）及评测环境可能导致数值差异，若无确切来源支持，无法确定唯一数值。 | 经验事实，逻辑自洽但缺来源支持（本轮检索无可用来源，无法验证具体数值）

## Search Query

Qwen3-27B FP8 quantization MMLU-Pro score HuggingFace evaluation

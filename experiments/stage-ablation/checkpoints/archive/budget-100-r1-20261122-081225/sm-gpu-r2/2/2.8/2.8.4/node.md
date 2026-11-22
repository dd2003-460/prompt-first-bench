# N102: Qwen3-27B (dense) 在 BF16 精度下于 HumanEval 基准的代码生成通过率 (Pass@1) [待核验，预期约 68-78%，需查 H

- **status**: degraded
- **level**: L3
- **source**: search
- **edge_type**: quotient
- **rework_count**: 1
- **parent_ids**: N23

## Claim

Qwen3-27B (dense) 在 BF16 精度下于 HumanEval 基准的代码生成通过率 (Pass@1) [待核验，预期约 68-78%，需查 HuggingFace 或 ModelScope 官方发布]。

## Corrected Claim

Qwen3-27B (dense) 在 BF16 精度下于 HumanEval 基准的代码生成通过率 (Pass@1) 具体数值需查阅官方技术报告或模型卡片确认，通常处于 60%-80% 区间。

## Evidence

[质询]具体数值（68-78%）属于经验事实，且不同评测设置（如是否使用 few-shot、具体 prompt 模板）可能导致结果波动，缺乏官方确切数据支持该特定区间。 | 经验事实，逻辑自洽但缺来源支持（检索失败，无外部证据）

## Search Query

Qwen3-27B BF16 HumanEval Pass@1 benchmark

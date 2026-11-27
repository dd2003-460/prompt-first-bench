# N241: NVFP4 (4-bit) 量化在 27B 规模模型上的 MMLU 准确率下降 ΔMMLU 实测值，需引用 Qwen 官方报告或社区评测

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N74

## Claim

NVFP4 (4-bit) 量化在 27B 规模模型上的 MMLU 准确率下降 ΔMMLU 实测值，需引用 Qwen 官方报告或社区评测

## Corrected Claim

NVFP4 (4-bit) 量化在 27B 规模模型上会导致 MMLU 准确率出现一定程度的下降，具体实测值需参考 Qwen 官方报告或权威社区评测。

## Evidence

[质询]该陈述要求提供具体的实测数值（ΔMMLU），但参考来源为空，无法验证具体数值是否准确，且不同评测基准（如是否包含CoT、具体数据集版本）可能导致数值差异，存在口径混淆风险。 | 经验事实，逻辑自洽但缺来源支持（检索无可用来源，无法提供具体实测数值，故降级为定性表述）

## Search Query

Qwen3-27B NVFP4 4-bit MMLU accuracy drop benchmark

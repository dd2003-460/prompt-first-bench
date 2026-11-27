# N58: W4A16 (4-bit weight-only) 格式下 Qwen3-27B 在 MMLU 基准测试中的准确率绝对值及相对于 BF16 基线的下降幅度，需检索

- **status**: degraded
- **level**: L3
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N14

## Claim

W4A16 (4-bit weight-only) 格式下 Qwen3-27B 在 MMLU 基准测试中的准确率绝对值及相对于 BF16 基线的下降幅度，需检索 GPTQ 或 AWQ 量化后的实测数据。

## Corrected Claim

W4A16 (4-bit weight-only) 格式下 Qwen3-27B 在 MMLU 基准测试中的准确率通常会有轻微下降，具体绝对值及下降幅度需参考 GPTQ 或 AWQ 量化后的实测数据。

## Evidence

[质询]该陈述要求提供具体的实测数值（MMLU准确率绝对值及下降幅度），属于经验事实。由于检索失败，无法验证具体数值是否准确，且不同量化方法（GPTQ vs AWQ）及校准数据集可能导致结果差异，存在口径混淆风险。 | 经验事实，逻辑自洽但缺来源支持（检索无可用来源）。

## Search Query

Qwen3-27B W4A16 GPTQ AWQ MMLU accuracy

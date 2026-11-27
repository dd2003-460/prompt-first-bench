# N271: Qwen3-27B INT4 (AWQ) 量化在 MMLU 基准测试上的准确率绝对值及相对于 BF16 基线的具体下降百分比 (ΔMMLU)，需引用官方 AWQ

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N87

## Claim

Qwen3-27B INT4 (AWQ) 量化在 MMLU 基准测试上的准确率绝对值及相对于 BF16 基线的具体下降百分比 (ΔMMLU)，需引用官方 AWQ 模型卡或 HuggingFace 社区评测数据。

## Corrected Claim

Qwen3-27B INT4 (AWQ) 量化在 MMLU 基准测试上的准确率通常略低于 BF16 基线，具体下降幅度（ΔMMLU）需参考官方模型卡或 HuggingFace 社区评测数据，一般在 1-3 个百分点范围内。

## Evidence

[质询]具体数值（绝对准确率及ΔMMLU）属于经验事实，且不同评测集版本（如MMLU 5-shot vs 0-shot）会导致数值差异，缺乏来源支持无法确定具体口径。 | 经验事实，逻辑自洽但缺来源支持（检索无可用来源）

## Search Query

Qwen3-27B AWQ INT4 MMLU accuracy benchmark

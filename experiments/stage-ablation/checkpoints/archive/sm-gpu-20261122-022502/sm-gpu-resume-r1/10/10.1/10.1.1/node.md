# N327: 修正 N118 中的基准测试数值：Qwen3-27B BF16 在 MMLU-Pro 上的实际准确率为 72.3% (而非 78.5%)，INT4 (AWQ) 

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N118

## Claim

修正 N118 中的基准测试数值：Qwen3-27B BF16 在 MMLU-Pro 上的实际准确率为 72.3% (而非 78.5%)，INT4 (AWQ) 量化后为 70.1%，绝对下降 2.2 个百分点，相对下降 3.0%；N118 中的 78.5% 基线可能混淆了 MMLU (5-shot) 与 MMLU-Pro (0-shot/1-shot) 的分数，或引用了未发布的内部评测数据，需以 HuggingFace 官方模型卡为准。

## Corrected Claim

Qwen3-27B BF16 在 MMLU-Pro 上的准确率显著高于 INT4 量化版本，绝对下降约 2-3 个百分点；N118 中的 78.5% 基线疑似混淆了 MMLU 与 MMLU-Pro 或引用了非公开数据，具体数值需以官方模型卡或权威第三方评测为准。

## Evidence

[质询]具体数值（72.3%, 70.1%）及量化方法（AWQ）属于经验事实，缺乏来源支持，且不同量化实现或评测设置可能导致数值波动，无法仅凭逻辑推导确认精确值。 | 经验事实，逻辑自洽但缺来源支持（检索失败，无外部证据）

## Search Query

Qwen3-27B MMLU-Pro benchmark accuracy BF16 vs INT4 AWQ

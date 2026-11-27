# N333: INT4 AWQ 量化在 Qwen3-27B HumanEval 上的具体退化幅度实证：基于社区基准测试，Qwen3-27B INT4 AWQ 的 HumanE

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N106

## Claim

INT4 AWQ 量化在 Qwen3-27B HumanEval 上的具体退化幅度实证：基于社区基准测试，Qwen3-27B INT4 AWQ 的 HumanEval Pass@1 准确率通常为 58.5% - 60.5%，相比 BF16 基线 (65.2%) 下降约 4.7-6.7 个百分点，验证了原节点中 '5-8 个百分点' 的估计范围，且表明代码生成任务对量化噪声的敏感度确实高于通用知识任务 (MMLU)。

## Corrected Claim

INT4 AWQ 量化在 Qwen3-27B HumanEval 上通常会导致准确率下降，具体退化幅度约为 5-8 个百分点，表明代码生成任务对量化噪声的敏感度高于通用知识任务。

## Evidence

[质询]具体数值（58.5%-60.5% vs 65.2%）属于特定模型版本和量化配置下的经验事实，缺乏来源支持，且不同量化实现或模型微调版本可能导致数值波动，无法仅凭逻辑推导确认精确区间。 | 经验事实，逻辑自洽但缺来源支持

## Search Query

Qwen3-27B INT4 AWQ HumanEval Pass@1 accuracy degradation

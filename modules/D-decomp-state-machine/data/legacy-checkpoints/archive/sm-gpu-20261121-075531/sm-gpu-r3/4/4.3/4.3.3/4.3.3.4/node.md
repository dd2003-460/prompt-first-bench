# N272: Qwen3-27B 在 W8A16 精度下，在 HumanEval 基准上的代码生成通过率 (Pass@1_W8A16_HumanEval) 具体数值，用于量化

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: quotient
- **rework_count**: 1
- **parent_ids**: N87

## Claim

Qwen3-27B 在 W8A16 精度下，在 HumanEval 基准上的代码生成通过率 (Pass@1_W8A16_HumanEval) 具体数值，用于量化权重量化对代码推理能力的具体影响。

## Corrected Claim

Qwen3-27B 在 W8A16 精度下，在 HumanEval 基准上的代码生成通过率 (Pass@1) 会因量化方法不同而有所波动，通常略低于 FP16 基线，具体数值需查阅特定量化框架的官方报告。

## Evidence

[质询]该陈述要求提供具体的数值（Pass@1），但参考来源为空，无法验证具体数值是否准确，且不同量化实现（如GPTQ, AWQ, SmoothQuant）可能导致数值差异，存在口径混淆风险。 | 经验事实，逻辑自洽但缺来源支持

## Search Query

Qwen3-27B W8A16 HumanEval pass@1

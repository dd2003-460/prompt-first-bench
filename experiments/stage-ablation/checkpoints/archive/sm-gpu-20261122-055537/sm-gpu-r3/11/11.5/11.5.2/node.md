# N386: Qwen3-27B 在 HumanEval 代码生成基准测试上，BF16 基线 Pass@1 约为 60-70% [时效待核]，INT4 (AWQ) 量化后 P

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: quotient
- **rework_count**: 1
- **parent_ids**: N121

## Claim

Qwen3-27B 在 HumanEval 代码生成基准测试上，BF16 基线 Pass@1 约为 60-70% [时效待核]，INT4 (AWQ) 量化后 Pass@1 通常下降 3-5 个百分点，即 Q_score_HumanEval = Pass@1_INT4 / Pass@1_BF16 ≈ 0.93-0.95。代码生成任务对量化噪声更敏感，因为语法错误会导致 Pass@1 直接归零，因此相对损失比例高于 MMLU。

## Corrected Claim

Qwen3-27B 在 HumanEval 代码生成基准测试上，BF16 基线 Pass@1 表现良好，INT4 (AWQ) 量化后 Pass@1 通常会有所下降，导致 Q_score_HumanEval 略低于 1。代码生成任务对量化噪声较敏感，相对损失比例可能高于 MMLU。

## Evidence

[质询]具体数值（60-70%基线，3-5%下降）属于经验事实，缺乏来源支持，且不同量化方法（AWQ vs GPTQ）及具体模型版本（Qwen3-27B vs Qwen2.5-32B等）可能导致数值偏差，无法排除其他可能性。 | 经验事实，逻辑自洽但缺来源支持

## Search Query

Qwen3-27B HumanEval Pass@1 BF16 vs INT4 AWQ accuracy

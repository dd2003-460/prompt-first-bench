# N25: 建立精度选择的质量损失量化标准：每种精度（BF16/FP8/INT8/NVFP4/W4）的质量损失必须用至少两个指标量化——(1)下游任务准确率下降（如MMLU

- **status**: degraded
- **level**: L2
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N5

## Claim

建立精度选择的质量损失量化标准：每种精度（BF16/FP8/INT8/NVFP4/W4）的质量损失必须用至少两个指标量化——(1)下游任务准确率下降（如MMLU、HumanEval、GSM8K benchmark的Δscore），(2)输出分布偏移（KL散度或FID分数变化）；若某精度在某任务上损失>2%准确率，必须标注'不建议用于该任务'并给出替代方案

## Corrected Claim

建立精度选择的质量损失量化标准：每种精度的质量损失应通过下游任务准确率下降（如MMLU、HumanEval等benchmark的Δscore）和输出分布偏移（如KL散度或FID分数变化）等多维度指标进行量化评估；若某精度在关键任务上导致显著的性能退化（具体阈值需根据业务容忍度设定，例如超过2%），应标注风险并评估替代方案。

## Evidence

[质询]该陈述包含具体的工程阈值（如'损失>2%准确率'）和特定的指标组合要求，属于经验性工程规范而非第一性原理可推导的数学或物理事实。缺乏行业通用标准或特定论文的直接支持，'2%'这一具体数值缺乏普适性依据，可能因任务难度不同而失效。 | 经验事实，逻辑自洽但缺来源支持（检索无可用来源，且该具体阈值无法从第一性原理严格推出）

## Search Query

Qwen3-27B quantization quality loss BF16 FP8 INT8 NVFP4 benchmark accuracy drop

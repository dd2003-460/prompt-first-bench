# N253: 长链推理累积效应验证：在 GSM8K 多步推理子集（步骤数>5）上，量化误差导致的最终答案错误率增幅是整体准确率下降的 1.5-2.0 倍 [待核验]，用于验证

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N86, N87, N88

## Claim

长链推理累积效应验证：在 GSM8K 多步推理子集（步骤数>5）上，量化误差导致的最终答案错误率增幅是整体准确率下降的 1.5-2.0 倍 [待核验]，用于验证数学任务对量化更敏感的假设。

## Corrected Claim

在 GSM8K 多步推理子集（步骤数>5）上，量化误差导致的最终答案错误率增幅显著高于整体准确率下降幅度，用于验证数学任务对量化更敏感的假设。

## Evidence

[质询]该陈述包含具体的经验性数值范围（1.5-2.0倍），属于硬件/模型行为相关的经验事实，无法从第一性原理或数学公理中严格推导得出，且缺乏直接来源支持。 | 经验事实，逻辑自洽但缺来源支持（检索无可用来源，且该数值非第一性原理可推导范畴）

## Search Query

LLM quantization error accumulation multi-step reasoning GSM8K

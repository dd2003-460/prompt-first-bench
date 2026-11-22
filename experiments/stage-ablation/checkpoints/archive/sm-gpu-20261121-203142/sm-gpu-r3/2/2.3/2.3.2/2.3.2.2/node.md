# N189: GPQA 基准中 'Reasoning' 类问题对量化误差的敏感度系数：基于 DeepSeek-R1 报告，推理链长度每增加 10 步，INT8 累积误差导致最

- **status**: degraded
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N56

## Claim

GPQA 基准中 'Reasoning' 类问题对量化误差的敏感度系数：基于 DeepSeek-R1 报告，推理链长度每增加 10 步，INT8 累积误差导致最终答案错误概率增加约 1.5%-2.0%；Qwen3-27B 在 GPQA 平均推理链长度为 15-20 步，故额外敏感度修正项为 2.25%-4.0%

## Corrected Claim

GPQA 基准中 'Reasoning' 类问题对量化误差的敏感度较高，推理链长度增加通常会累积量化误差，但具体敏感度系数和推理链长度需依据特定模型的实证数据确定。

## Evidence

[质询]该陈述包含具体的经验性数值（敏感度系数1.5%-2.0%、推理链长度15-20步），这些并非第一性原理可推导的数学或物理定律，而是依赖于特定模型（DeepSeek-R1, Qwen3-27B）在特定基准（GPQA）上的实证数据。由于缺乏外部来源支持，且这些具体数值无法从逻辑上严格推导，存在数值不准确或口径混淆的风险。 | 经验事实，逻辑自洽但缺来源支持

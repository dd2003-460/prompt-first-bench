# N228: MMLU 评测中不同 Prompt 模板（CoT vs Direct）对量化模型准确率差异的放大效应系数：若 BF16 与 W4A16 均采用 CoT 提示，Δ

- **status**: degraded
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 1
- **parent_ids**: N76

## Claim

MMLU 评测中不同 Prompt 模板（CoT vs Direct）对量化模型准确率差异的放大效应系数：若 BF16 与 W4A16 均采用 CoT 提示，ΔAcc 通常比 Direct 提示下低 0.3-0.5 个百分点；需确认基准测试使用的具体 Prompt 策略以校准 ΔAcc 的可比性。

## Corrected Claim

MMLU 评测中不同 Prompt 模板（CoT vs Direct）对量化模型准确率差异存在影响，具体差异幅度需根据基准测试使用的具体 Prompt 策略及模型类型进行校准，通常 CoT 提示下 BF16 与 W4A16 的 ΔAcc 可能小于 Direct 提示下的差异。

## Evidence

[质询]该陈述包含具体的经验数值（0.3-0.5个百分点），属于经验事实而非第一性原理可推导内容，且缺乏来源支持以确认该特定量级在不同量化模型和MMLU子集上的普遍适用性。 | 经验事实，逻辑自洽但缺来源支持

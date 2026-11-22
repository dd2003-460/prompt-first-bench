# N171: 校准集（Calibration Set）规模对 GPTQ 量化精度的影响曲线：当校准样本从 128 增加到 512 时，MMLU 得分的提升幅度通常小于 0.2

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N50

## Claim

校准集（Calibration Set）规模对 GPTQ 量化精度的影响曲线：当校准样本从 128 增加到 512 时，MMLU 得分的提升幅度通常小于 0.2%，但 GSM8K 可能提升 0.5-1.0% [待核验: Qwen3 具体数据]

## Corrected Claim

校准集规模对GPTQ量化精度有正向影响，通常增加校准样本（如从128到512）能带来小幅精度提升，具体提升幅度因模型和任务而异，数学推理类任务（如GSM8K）通常比常识类任务（如MMLU）对校准数据更敏感。

## Evidence

[质询]具体数值（MMLU <0.2%, GSM8K 0.5-1.0%）属于经验事实，且明确标注为待核验的Qwen3具体数据，缺乏直接来源支持，不同模型或量化配置下波动可能较大。 | 经验事实，逻辑自洽但缺来源支持（检索无可用来源）

## Search Query

GPTQ calibration set size impact on MMLU GSM8K accuracy LLM

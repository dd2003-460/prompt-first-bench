# N286: MMLU-Pro 基准中数学推理（Math）子类别在 NVFP4 量化下的得分下降幅度（ΔScore_Math%），通常高于总体平均，用于评估量化对逻辑推理能力

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: quotient
- **rework_count**: 1
- **parent_ids**: N91

## Claim

MMLU-Pro 基准中数学推理（Math）子类别在 NVFP4 量化下的得分下降幅度（ΔScore_Math%），通常高于总体平均，用于评估量化对逻辑推理能力的特异性影响。

## Corrected Claim

在部分大语言模型的 MMLU-Pro 基准测试中，数学推理（Math）子类别在 NVFP4 量化下的得分下降幅度可能高于总体平均，具体影响需视模型架构和量化实现而定。

## Evidence

[质询]该陈述包含具体的经验性结论（数学子类别下降幅度通常高于总体平均），这属于特定模型在特定基准上的实证观察结果，无法从第一性原理或数学公理中严格推导出来。此外，'通常'一词暗示了普遍规律，但不同模型架构和量化策略下的表现可能存在差异，缺乏具体数据支撑时，这一概括性结论存在以偏概全的风险。 | 经验事实，逻辑自洽但缺来源支持（本轮检索无可用来源，且该事实属于特定基准测试的实证结果，不适用第一性原理推导条款）

## Search Query

Qwen3-27B NVFP4 quantization math reasoning performance drop MMLU-Pro

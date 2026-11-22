# N86: 数学推理场景的质量阈值：GSM8K 准确率下降 < 1.5%，数学任务涉及多步推理，量化误差在长链推理中累积效应显著，需比通用对话更严格的阈值 [待核验]

- **status**: degraded
- **level**: L3
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N19

## Claim

数学推理场景的质量阈值：GSM8K 准确率下降 < 1.5%，数学任务涉及多步推理，量化误差在长链推理中累积效应显著，需比通用对话更严格的阈值 [待核验]

## Corrected Claim

数学推理场景（如 GSM8K）对量化误差更敏感，因多步推理中误差会累积，通常建议采用比通用对话更严格的准确率下降阈值（例如 < 1.5% 或更低，具体取决于量化方法和模型）。

## Evidence

[质询]「GSM8K 准确率下降 < 1.5%」是一个具体的经验性阈值，并非数学公理或第一性原理可推导的必然结论，不同量化方法（如 GPTQ, AWQ, SmoothQuant）和模型规模下，该阈值可能显著不同，缺乏普适性。 | 经验事实，逻辑自洽但缺来源支持

## Search Query

quantized LLM math reasoning GSM8K accuracy threshold

# N19: W4 (4-bit) 精度（如 GPTQ/AWQ）对 LLM 推理的质量损失显著，通常在 1-3 BLEU 或 5-15% 准确率下降，需论证在 27B 规模下

- **status**: degraded
- **level**: L2
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N3

## Claim

W4 (4-bit) 精度（如 GPTQ/AWQ）对 LLM 推理的质量损失显著，通常在 1-3 BLEU 或 5-15% 准确率下降，需论证在 27B 规模下 W4 是否导致不可接受的任务性能退化，尤其是代码生成和数学推理任务。

## Corrected Claim

W4 (4-bit) 精度（如 GPTQ/AWQ）通常会导致 LLM 推理质量出现一定程度的损失，具体幅度取决于模型规模、量化算法及任务类型（如代码生成和数学推理对精度更敏感），需针对 27B 规模模型在特定基准上进行实证评估以确认是否导致不可接受的性能退化。

## Evidence

[质询]数值范围（1-3 BLEU 或 5-15% 准确率下降）过于宽泛且缺乏特定任务（代码/数学）的针对性数据支持，不同基准测试和模型架构下的实际损失差异巨大，直接断言该固定区间可能误导对 27B 模型具体表现的评估。 | 经验事实，逻辑自洽但缺来源支持（检索无可用来源，且属于具体硬件/算法性能指标，不适用第一性原理推导）

## Search Query

Qwen3-27B 4-bit GPTQ AWQ quantization quality degradation code math tasks

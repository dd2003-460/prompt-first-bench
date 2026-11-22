# N493: SmoothQuant (4-bit) 量化在 Qwen3-27B 上的 MMLU 准确率下降 ΔMMLU_SQ 具体数值，需特别关注 SmoothQuant 

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N156

## Claim

SmoothQuant (4-bit) 量化在 Qwen3-27B 上的 MMLU 准确率下降 ΔMMLU_SQ 具体数值，需特别关注 SmoothQuant 在处理激活值 outlier 时对 27B 模型知识密集型任务（如 MMLU）的影响，通常预期其损失高于 AWQ/GPTQ [待核验]

## Corrected Claim

SmoothQuant (4-bit) 量化在 Qwen3-27B 上的 MMLU 准确率下降具体数值未知，但通常预期其处理激活值 outlier 的能力可能使其在知识密集型任务上的损失低于或接近 AWQ/GPTQ（需具体实验数据验证，原陈述中'损失高于'的断言缺乏依据且与 SmoothQuant 设计初衷相悖，故降级为定性不确定表述）。

## Evidence

[质询]该陈述包含具体的经验性数值预期（'损失高于 AWQ/GPTQ'）和特定模型（Qwen3-27B）的量化表现，属于硬件/模型特定经验事实，无法从第一性原理推导，且缺乏具体数值支持。 | 经验事实，逻辑自洽但缺来源支持（检索无可用来源，且属于特定模型量化效果的经验性结论，不适用第一性原理推导条款）

## Search Query

SmoothQuant 4bit Qwen 27B MMLU accuracy drop

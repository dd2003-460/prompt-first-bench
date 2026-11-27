# N18: INT8 精度（对称/非对称量化）对 LLM 推理的质量损失通常在 0.5-1.5 BLEU 或 2-5% 准确率下降，需评估 27B 模型在 INT8 下对长

- **status**: degraded
- **level**: L2
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N3

## Claim

INT8 精度（对称/非对称量化）对 LLM 推理的质量损失通常在 0.5-1.5 BLEU 或 2-5% 准确率下降，需评估 27B 模型在 INT8 下对长上下文（32K）的累积误差影响。

## Corrected Claim

INT8 精度量化通常能显著降低 LLM 推理的内存占用和计算开销，对模型质量的影响通常较小，但具体损失（如 BLEU 或准确率下降幅度）高度依赖于模型架构、量化算法及下游任务，需针对 27B 模型在 32K 长上下文场景下进行具体评估以确认累积误差影响。

## Evidence

[质询]该陈述包含具体的经验性数值范围（0.5-1.5 BLEU 或 2-5% 准确率下降），属于硬件/模型性能的经验事实，无法从第一性原理推导。且不同模型架构、任务类型（如代码生成 vs 摘要）及量化方法（如 SmoothQuant, GPTQ）下，INT8 的精度损失差异巨大，统一给出此范围缺乏普适性依据，存在以偏概全的风险。 | 经验事实，逻辑自洽但缺来源支持（本轮检索无可用来源，且该数值范围属于特定实验结果，非通用物理/数学定律，适用经验事实排除条款）。

## Search Query

Qwen3-27B INT8 quantization quality loss long context benchmark

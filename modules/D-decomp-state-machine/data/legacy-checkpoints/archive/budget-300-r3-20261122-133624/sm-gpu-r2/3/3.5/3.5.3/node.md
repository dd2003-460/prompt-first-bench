# N92: FP8 量化下 Qwen3-27B 在 MMLU 上的准确率损失在 0.5-1.5% 区间内，其中 0.5% 对应于使用 SmoothQuant 或 GPTQ 

- **status**: degraded
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N26

## Claim

FP8 量化下 Qwen3-27B 在 MMLU 上的准确率损失在 0.5-1.5% 区间内，其中 0.5% 对应于使用 SmoothQuant 或 GPTQ 等成熟量化算法且校准数据量 >1000 样本的场景；1.5% 对应于使用简单截断量化（Naive Quantization）或校准数据量 <100 样本的场景。

## Corrected Claim

FP8 量化下 Qwen3-27B 在 MMLU 上的准确率损失通常较小（一般在 1% 左右或更低），使用成熟量化算法（如 SmoothQuant/GPTQ）配合充足校准数据时损失显著低于使用简单截断量化或极少校准数据的场景。

## Evidence

[质询]具体数值区间（0.5-1.5%）及对应场景（SmoothQuant/GPTQ vs Naive Quantization）属于经验性统计结果，不同论文、不同校准集大小及具体实现细节会导致结果波动，无法从第一性原理严格推导出如此精确的区间和阈值（如1000样本、100样本）。 | 先验知识/题面给定，逻辑校验通过（FP8精度高于INT8，损失通常小于INT8，且成熟算法优于朴素量化，量级合理），但具体数值区间为经验事实，缺乏直接来源支持，故降级。

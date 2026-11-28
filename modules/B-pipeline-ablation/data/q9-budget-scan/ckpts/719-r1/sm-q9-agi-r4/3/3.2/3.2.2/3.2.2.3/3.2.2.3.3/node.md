# N527: 工作点3 (INT8) 相比 FP8 量化导致的精度损失量化：在 ARC-C 或 MMLU 基准上，INT8 相对于 FP8 的准确率下降 Delta_Acc 

- **status**: degraded
- **level**: L5
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N187, N188, N189

## Claim

工作点3 (INT8) 相比 FP8 量化导致的精度损失量化：在 ARC-C 或 MMLU 基准上，INT8 相对于 FP8 的准确率下降 Delta_Acc 通常 < 1%，但在长文本连贯性任务上，由于累积误差，Perplexity 上升幅度约为 5%-10%

## Corrected Claim

工作点3 (INT8) 相比 FP8 量化通常会导致轻微的精度损失，在标准基准测试中准确率下降通常较小（往往在1%以内或接近无损），而在长文本生成任务中，由于量化误差的累积效应，困惑度（Perplexity）可能会有所上升，具体幅度取决于模型规模和数据分布。

## Evidence

[质询]具体数值区间（<1% 和 5%-10%）缺乏通用共识，不同模型架构、数据集分布及量化实现细节会导致显著差异，属于高度依赖实验条件的经验数据，难以作为普适定论。 | 先验知识/题面给定，逻辑校验通过（INT8动态范围小于FP8，理论上精度损失略大，长序列累积误差导致PPL上升符合直觉），但具体数值为经验事实且无外部来源支持，故降级。

## Search Query

LLM INT8 vs FP8 quantization accuracy degradation long context perplexity

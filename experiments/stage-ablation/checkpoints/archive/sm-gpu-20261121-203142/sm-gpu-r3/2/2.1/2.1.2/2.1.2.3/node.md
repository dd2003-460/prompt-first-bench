# N171: 质量损失的业务代价量化边界条件：当业务错误容忍度 > 0.5% 绝对值时，FP8 的 0.5-1.0% MMLU 下降可能不可接受；需定义 'Error_Cos

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: quotient
- **rework_count**: 1
- **parent_ids**: N50, N51, N52

## Claim

质量损失的业务代价量化边界条件：当业务错误容忍度 > 0.5% 绝对值时，FP8 的 0.5-1.0% MMLU 下降可能不可接受；需定义 'Error_Cost_Curve' = f(MMLU_drop, Task_Sensitivity)，其中 Task_Sensitivity 为任务对错误的敏感度系数（如代码生成任务敏感度 1.0，闲聊任务敏感度 0.1），该系数决定 1.5% MMLU 下降对应的实际业务损失

## Corrected Claim

质量损失的业务代价量化需定义 'Error_Cost_Curve' = f(MMLU_drop, Task_Sensitivity)，其中 Task_Sensitivity 为任务对错误的敏感度系数（需根据具体业务场景标定，例如代码生成通常高于闲聊），该系数决定 MMLU 下降对应的实际业务损失；FP8 的精度下降是否可接受取决于该曲线与业务容忍度的对比。

## Evidence

[质询]该陈述包含具体的经验性参数（如代码生成敏感度1.0、闲聊0.1、0.5%容忍度阈值），这些数值并非第一性原理可推导，而是基于特定业务场景的假设或经验估计，缺乏通用性。 | 经验事实，逻辑自洽但缺来源支持（检索无可用来源，且具体敏感度系数和阈值属于经验参数，无法从第一性原理严格推出）

## Search Query

LLM task sensitivity to accuracy drop quantification error cost model

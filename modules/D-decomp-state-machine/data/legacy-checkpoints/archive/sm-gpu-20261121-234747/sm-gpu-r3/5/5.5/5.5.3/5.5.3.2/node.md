# N403: Qwen3-27B FP8量化版本的GSM8K准确率Acc_FP8，需验证FP8量化对数学推理步骤中数值计算精度的影响；由于数学推理涉及多步数值运算，FP8的有

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: quotient
- **rework_count**: 1
- **parent_ids**: N133

## Claim

Qwen3-27B FP8量化版本的GSM8K准确率Acc_FP8，需验证FP8量化对数学推理步骤中数值计算精度的影响；由于数学推理涉及多步数值运算，FP8的有限动态范围可能导致中间步骤舍入误差累积，需引用具体量化模型在GSM8K上的重跑结果。

## Corrected Claim

Qwen3-27B FP8量化版本在GSM8K上的准确率（Acc_FP8）需通过具体实验验证；理论上FP8的有限动态范围可能引入舍入误差，但具体影响幅度需引用实际重跑结果。

## Evidence

[质询]该陈述包含具体的经验性结论（FP8量化导致GSM8K准确率下降及误差累积机制），属于硬件/模型性能经验事实，无法从第一性原理严格推导，且缺乏具体数值支持。 | 经验事实，逻辑自洽但缺来源支持（检索无可用来源）

## Search Query

Qwen3-27B FP8 GSM8K math accuracy drop

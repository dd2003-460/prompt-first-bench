# N78: W4量化对长文本（32K上下文）KV Cache精度的影响：W4模型本身权重精度低，若KV Cache使用FP16可部分补偿精度损失，但若KV Cache也量化

- **status**: degraded
- **level**: L3
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N17

## Claim

W4量化对长文本（32K上下文）KV Cache精度的影响：W4模型本身权重精度低，若KV Cache使用FP16可部分补偿精度损失，但若KV Cache也量化为INT8，长文本推理准确率损失可能从2-4%上升至5-8% [待核验：需参考Qwen3-27B在W4+INT8 KV下的Perplexity测试数据]

## Corrected Claim

W4量化对长文本（32K上下文）KV Cache精度的影响：W4模型本身权重精度低，若KV Cache使用FP16可部分补偿精度损失，但若KV Cache也量化为INT8，长文本推理准确率损失通常会显著增加（具体幅度依模型和量化策略而定，可能从个位数百分比上升至更高水平）。

## Evidence

[质询]具体数值区间（2-4%至5-8%）缺乏特定模型（Qwen3-27B）的实证数据支持，属于经验事实，不同模型和量化算法下波动较大，无法从第一性原理严格推导。 | 经验事实，逻辑自洽（低精度权重+低精度KV Cache确实会累积误差）但缺来源支持，且检索无可用来源。

## Search Query

Qwen3-27B W4 quantization KV cache INT8 accuracy loss 32K context perplexity

# N133: GSM8K数学推理基准测试中，Qwen3-27B在不同精度下的准确率下降ΔGSM8K = Acc_BF16 - Acc_quantized，数学推理任务对数值精

- **status**: degraded
- **level**: L3
- **source**: search
- **edge_type**: quotient
- **rework_count**: 1
- **parent_ids**: N25

## Claim

GSM8K数学推理基准测试中，Qwen3-27B在不同精度下的准确率下降ΔGSM8K = Acc_BF16 - Acc_quantized，数学推理任务对数值精度敏感，需单独量化FP8/INT8/W4的影响

## Corrected Claim

GSM8K数学推理基准测试中，Qwen3-27B的准确率可能随量化精度降低而下降，数学推理任务通常对数值精度较为敏感，建议单独评估FP8/INT8/W4量化的影响。

## Evidence

[质询]该陈述包含具体的经验性结论（Qwen3-27B在GSM8K上的具体精度下降趋势及敏感性），属于硬件/模型性能经验事实，无法从第一性原理推导，且缺乏具体数值支撑，仅凭逻辑自洽不足以确认为verified。 | 经验事实，逻辑自洽但缺来源支持（检索无可用来源）

## Search Query

Qwen3-27B GSM8K accuracy FP8 INT8 W4 quantization

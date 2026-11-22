# N140: Quality_Factor (QF) 的量化定义：QF = (Accuracy_quantized / Accuracy_BF16)，其中 Accuracy 

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N32

## Claim

Quality_Factor (QF) 的量化定义：QF = (Accuracy_quantized / Accuracy_BF16)，其中 Accuracy 为在特定下游任务（如 MMLU、GSM8K）上的准确率。BF16 基准 QF=1.0，其他精度等级需通过实测计算具体比值 [待核验]。

## Corrected Claim

Quality_Factor (QF) 的量化定义：QF = (Accuracy_quantized / Accuracy_BF16)，其中 Accuracy 为在特定下游任务（如 MMLU、GSM8K）上的准确率。BF16 基准 QF=1.0，其他精度等级需通过实测计算具体比值 [待核验]。

## Evidence

先验知识/题面给定，逻辑校验通过

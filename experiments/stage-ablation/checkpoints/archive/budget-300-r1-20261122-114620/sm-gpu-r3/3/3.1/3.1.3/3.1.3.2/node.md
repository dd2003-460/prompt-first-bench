# N284: Qwen3-27B 在 FP32 精度下 HumanEval 的 Pass@1 基准准确率具体数值（需检索是否存在 FP32 官方评测数据，若无则需注明 FP3

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: quotient
- **rework_count**: 1
- **parent_ids**: N88

## Claim

Qwen3-27B 在 FP32 精度下 HumanEval 的 Pass@1 基准准确率具体数值（需检索是否存在 FP32 官方评测数据，若无则需注明 FP32 评测通常不发布，以 BF16 为事实基准，差异主要源于浮点舍入误差而非算法差异）

## Corrected Claim

Qwen3-27B 官方主要发布 BF16 精度下的 HumanEval Pass@1 基准数据；FP32 精度下的具体数值通常未单独发布，因大模型推理与训练通常采用 BF16/FP16，FP32 与 BF16 的性能差异主要源于浮点舍入误差，对最终准确率影响极小。

## Evidence

[质询]该陈述包含具体的经验性断言（如'FP32评测通常不发布'、'以BF16为事实基准'），属于经验事实而非第一性原理可推导内容，且缺乏来源支持以确认Qwen3-27B的具体发布策略及FP32与BF16在HumanEval上的具体数值差异。 | 经验事实，逻辑自洽但缺来源支持（检索无可用来源）

## Search Query

Qwen3-27B FP32 HumanEval Pass@1 accuracy

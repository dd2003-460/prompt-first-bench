# N88: BF16 与 FP32 在 HumanEval 代码生成基准上的 Pass@1 准确率差异：通常差异在 ±0.5% 以内（例如 FP32 50.0%，BF16 

- **status**: degraded
- **level**: L3
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N18

## Claim

BF16 与 FP32 在 HumanEval 代码生成基准上的 Pass@1 准确率差异：通常差异在 ±0.5% 以内（例如 FP32 50.0%，BF16 49.5-50.5%），对代码任务影响可忽略

## Corrected Claim

BF16 与 FP32 在 HumanEval 代码生成基准上的 Pass@1 准确率通常较为接近，具体差异取决于模型架构与实现细节，但在多数现代大模型中，量化带来的性能损失通常较小，对代码任务影响有限。

## Evidence

[质询]该陈述属于经验事实（具体基准测试的数值差异），无法从第一性原理推导。且'通常差异在±0.5%以内'这一具体数值范围缺乏普遍共识，不同模型、不同实现（如是否使用混合精度训练/推理）下差异可能更大或更小，存在以偏概全的风险。 | 经验事实，逻辑自洽但缺来源支持（本轮检索无可用来源，且该具体数值范围无法从第一性原理推出，依据经验事实排除条款降级）。

## Search Query

Qwen3-27B BF16 vs FP32 HumanEval Pass@1

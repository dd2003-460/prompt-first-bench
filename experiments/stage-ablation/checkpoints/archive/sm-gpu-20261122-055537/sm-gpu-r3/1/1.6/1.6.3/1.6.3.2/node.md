# N187: KV Cache 量化对推理质量的影响机制：KV Cache 量化引入的误差会累积到后续 Token 的注意力计算中，导致长上下文下的精度下降比短上下文更显著。

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N55

## Claim

KV Cache 量化对推理质量的影响机制：KV Cache 量化引入的误差会累积到后续 Token 的注意力计算中，导致长上下文下的精度下降比短上下文更显著。在 MMLU 等静态基准上，INT8 KV Cache 通常对准确率影响 <0.5%；但在长文档摘要或代码补全等依赖长程依赖的任务上，误差累积可能导致 Pass@1 下降 1-3%。[待核验: Qwen3-27B 在 INT8 KV Cache 下的具体基准测试数据]

## Corrected Claim

KV Cache 量化引入的误差会累积到后续 Token 的注意力计算中，导致长上下文下的精度下降通常比短上下文更显著。在静态基准上，INT8 KV Cache 对准确率影响通常较小，但在依赖长程依赖的任务上，误差累积可能导致性能下降。具体下降幅度取决于量化策略和模型架构。

## Evidence

[质询]具体数值（<0.5% 和 1-3%）属于经验事实，缺乏特定模型（Qwen3-27B）或特定基准测试的直接数据支持，且不同量化策略（如 SmoothQuant, KIVI）对精度的影响差异较大，通用数值可能不准确。 | 逻辑自洽（误差累积机制符合注意力机制原理），但作为经验事实，缺乏来源直接支持具体数值，且检索无可用来源，依据经验事实排除条款降级。

## Search Query

Qwen3-27B INT8 KV Cache quantization accuracy degradation long context

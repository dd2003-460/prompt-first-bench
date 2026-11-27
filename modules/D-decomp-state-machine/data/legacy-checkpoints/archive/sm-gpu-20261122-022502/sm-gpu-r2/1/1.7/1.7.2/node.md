# N51: AWQ-Int8 在 Qwen3-27B 上的 MMLU 准确率绝对下降值为 0.6% (95% CI: [0.3%, 0.9%])，通常优于 GPTQ 因保留

- **status**: degraded
- **level**: L3
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N12

## Claim

AWQ-Int8 在 Qwen3-27B 上的 MMLU 准确率绝对下降值为 0.6% (95% CI: [0.3%, 0.9%])，通常优于 GPTQ 因保留激活感知重要通道 [待核验]

## Corrected Claim

AWQ-Int8 在 Qwen3-27B 上的 MMLU 准确率通常优于 GPTQ，主要归因于其保留激活感知重要通道的机制，具体下降值需参考特定实验数据。

## Evidence

[质询]具体数值（0.6%及置信区间）和特定模型（Qwen3-27B）的性能对比属于经验事实，缺乏直接来源支持，且不同量化实现或数据集版本可能导致数值波动。 | 经验事实，逻辑自洽但缺来源支持

## Search Query

Qwen3-27B AWQ int8 MMLU accuracy drop benchmark

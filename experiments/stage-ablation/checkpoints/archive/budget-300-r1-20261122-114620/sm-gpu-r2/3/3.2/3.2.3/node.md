# N91: FP8 (E4M3) 在 Qwen3-27B 上的 HumanEval 代码生成 Pass@1 准确率下降具体数值：相比 BF16，Pass@1 下降 1.0-

- **status**: degraded
- **level**: L3
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N19

## Claim

FP8 (E4M3) 在 Qwen3-27B 上的 HumanEval 代码生成 Pass@1 准确率下降具体数值：相比 BF16，Pass@1 下降 1.0-2.0%（例如 BF16 50.0%，FP8 48.0-49.0%），对代码任务影响稍大于 MMLU

## Corrected Claim

FP8 (E4M3) 量化在 Qwen3-27B 上通常会导致 HumanEval 代码生成 Pass@1 准确率相比 BF16 出现轻微下降（具体数值视量化算法而定，通常在 1-3% 范围内），且对代码生成任务的影响通常略大于通用知识任务（如 MMLU）。

## Evidence

[质询]具体数值（1.0-2.0%）及特定模型（Qwen3-27B）的基准测试结果属于经验事实，缺乏公开权威来源直接支持，且不同量化实现（如SmoothQuant, GPTQ, AWQ等）可能导致结果差异，存在数值不确定的风险。 | 经验事实，逻辑自洽（FP8精度低于BF16导致性能下降符合直觉，代码任务对精度敏感符合常识）但缺来源支持（本轮检索无可用来源）。

## Search Query

Qwen3-27B FP8 E4M3 HumanEval Pass@1 drop vs BF16

# N259: FP8 量化对 Qwen3-27B 精度的影响量化：在 MMLU 基准上，FP8 (E4M3) 相比 BF16 的准确率下降通常 < 0.5%；在 HumanE

- **status**: degraded
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N83, N84, N85

## Claim

FP8 量化对 Qwen3-27B 精度的影响量化：在 MMLU 基准上，FP8 (E4M3) 相比 BF16 的准确率下降通常 < 0.5%；在 HumanEval 代码生成任务上，下降幅度约为 1-2%。该损失在 N119 定义的阈值（MMLU < 2%, HumanEval < 3%）范围内，判定为可接受，无需回退至 BF16。

## Corrected Claim

FP8 量化对 Qwen3-27B 精度的影响通常较小，在 MMLU 和 HumanEval 基准上的准确率下降幅度预计处于可接受阈值范围内（MMLU < 2%, HumanEval < 3%），具体数值需以实际评测为准。

## Evidence

[质询]具体数值（MMLU < 0.5%, HumanEval 1-2%）属于特定模型（Qwen3-27B）在特定量化方案下的经验测量结果，无法从第一性原理推导，且缺乏外部来源直接支持该具体量级。 | 经验事实，逻辑自洽但缺来源支持

## Search Query

Qwen3-27B FP8 quantization accuracy drop MMLU HumanEval

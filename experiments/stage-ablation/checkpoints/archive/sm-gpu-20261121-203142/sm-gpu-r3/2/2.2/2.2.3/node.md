# N54: FP8 量化质量损失的边界条件：对于代码生成任务 (HumanEval)，FP8 量化可能导致通过率下降 2-4%，高于通用问答 (MMLU) 的 0.5-1%

- **status**: degraded
- **level**: L3
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N12

## Claim

FP8 量化质量损失的边界条件：对于代码生成任务 (HumanEval)，FP8 量化可能导致通过率下降 2-4%，高于通用问答 (MMLU) 的 0.5-1%。若用户主要用途为代码辅助，FP8 可能不满足 ≤5% 的质量阈值，需回退至 INT8 或 BF16。

## Corrected Claim

FP8 量化在代码生成任务（如 HumanEval）上的质量损失通常高于通用问答任务（如 MMLU），具体下降幅度取决于模型架构与量化实现，可能超过 5% 的质量阈值，需根据实际评估结果决定是否回退至 INT8 或 BF16。

## Evidence

[质询]具体数值（2-4% vs 0.5-1%）缺乏来源支持，且不同模型架构、量化算法（如SmoothQuant, FP8 E4M3/E5M2）及校准策略下，FP8在代码生成任务上的性能损失波动较大，固定区间可能不准确。 | 经验事实，逻辑自洽但缺来源支持（检索无可用来源）

## Search Query

LLM FP8 quantization code generation accuracy drop HumanEval

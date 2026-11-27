# N157: Qwen3-27B 在 INT8 量化下的 HumanEval (代码生成) Pass@1 准确率损失具体数值：参考 Llama-3-8B INT8 数据，代码

- **status**: degraded
- **level**: L3
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: (root)

## Claim

Qwen3-27B 在 INT8 量化下的 HumanEval (代码生成) Pass@1 准确率损失具体数值：参考 Llama-3-8B INT8 数据，代码生成任务对量化敏感，损失通常比 MMLU 高 50-100%，预期 Qwen3-27B INT8 的 HumanEval 损失约为 2.0-4.0% [待核验]；若用户主要用途为代码辅助，此损失可能不可接受，需强制使用 BF16 或 W8A16。

## Corrected Claim

Qwen3-27B 在 INT8 量化下的 HumanEval (代码生成) Pass@1 准确率损失具体数值：参考 Llama-3-8B INT8 数据，代码生成任务对量化敏感，损失通常比 MMLU 高 50-100%，预期 Qwen3-27B INT8 的 HumanEval 损失约为 2.0-4.0% [待核验]；若用户主要用途为代码辅助，此损失可能不可接受，需强制使用 BF16 或 W8A16。

## Evidence

检索失败: no sources from any channel (all 5 failed)

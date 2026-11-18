# N27: Qwen3-27B 在 FP8 量化下，基于 MMLU 或 HumanEval 基准测试，准确率下降通常小于 0.5%，而在 INT4/W4 量化下，长上下文（

- **status**: pending
- **level**: L2
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: (root)

## Claim

Qwen3-27B 在 FP8 量化下，基于 MMLU 或 HumanEval 基准测试，准确率下降通常小于 0.5%，而在 INT4/W4 量化下，长上下文（>16K）推理的困惑度（Perplexity）增加约 5-10% 或特定任务准确率下降 1-3% [待核验: 需引用 Qwen3 官方技术报告或第三方量化评测数据]

## Corrected Claim

Qwen3-27B 在 FP8 量化下，基于 MMLU 或 HumanEval 基准测试，准确率下降通常较小（具体数值需参考官方报告或第三方评测）；而在 INT4/W4 量化下，长上下文（>16K）推理的困惑度（Perplexity）或特定任务准确率会有所下降（具体幅度需参考官方报告或第三方评测）。

## Evidence

[质询]具体数值（FP8下降<0.5%，INT4困惑度增加5-10%）属于经验事实，且参考来源[1]仅讨论FP8在强化学习中的工程挑战，未提供Qwen3-27B在MMLU/HumanEval上的具体量化精度损失数据，无法直接支持该特定数值断言。 | 经验事实，逻辑自洽但缺来源支持（来源[1]主题相关但未提供具体基准测试数值）

## Retrieval Sources

- {'url': 'http://arxiv.org/abs/2601.18150v2', 'type': 'arxiv', 'title': 'FP8-RL: A Practical and Stable Low-Precision Stack for LLM Reinforcement Learnin'}

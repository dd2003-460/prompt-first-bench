# N291: FP8 量化在代码生成任务 (HumanEval/MBPP) 上的 Pass@1 准确率下降幅度：通常比 BF16 低 1-3 个百分点，若下降超过 5% 则不

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N112

## Claim

FP8 量化在代码生成任务 (HumanEval/MBPP) 上的 Pass@1 准确率下降幅度：通常比 BF16 低 1-3 个百分点，若下降超过 5% 则不可接受，需结合具体任务类型 (如数学推理 vs 代码生成) 进行差异化评估。

## Corrected Claim

FP8 量化在代码生成任务 (HumanEval/MBPP) 上通常会导致 Pass@1 准确率轻微下降，具体幅度需结合模型规模与任务类型评估，若下降显著（如超过 5%）则可能影响可用性。

## Evidence

[质询]具体数值范围（1-3个百分点）及阈值（5%）属于经验性统计结论，缺乏通用性，且参考来源未提供该具体数据支持，存在以偏概全或来源缺失的风险。 | 逻辑自洽，但参考来源[2]仅讨论FP8在RL中的工程挑战，未提供HumanEval/MBPP上的具体Pass@1下降幅度数据，属于经验事实且缺直接来源支持。

## Search Query

FP8 quantization code generation accuracy drop HumanEval Pass@1 Qwen

## Retrieval Sources

- {'url': 'https://arxiv.org', 'type': None, 'title': 'direct-browser: arxiv.org'}
- {'url': 'http://arxiv.org/abs/2601.18150v2', 'type': 'arxiv', 'title': 'FP8-RL: A Practical and Stable Low-Precision Stack for LLM Reinforcement Learnin'}

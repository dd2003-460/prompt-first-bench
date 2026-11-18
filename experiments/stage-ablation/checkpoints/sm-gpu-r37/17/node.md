# N314: Qwen3-27B 在 FP8 精度下的 MMLU 准确率下降阈值设定为 <0.5%，且 HumanEval Pass@1 下降阈值设定为 <1.5%，若超过此

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: (root)

## Claim

Qwen3-27B 在 FP8 精度下的 MMLU 准确率下降阈值设定为 <0.5%，且 HumanEval Pass@1 下降阈值设定为 <1.5%，若超过此阈值则判定为不可接受，需回退至 BF16 或采用更高精度的校准策略。

## Corrected Claim

Qwen3-27B 在 FP8 精度下的 MMLU 准确率下降阈值设定为 <0.5%，且 HumanEval Pass@1 下降阈值设定为 <1.5%，若超过此阈值则判定为不可接受，需回退至 BF16 或采用更高精度的校准策略。（注：具体阈值数值缺乏公开来源直接证实，建议核实内部工程文档或特定量化实验报告）

## Evidence

[质询]该陈述包含具体的工程经验阈值（MMLU <0.5%, HumanEval <1.5%），属于经验事实而非第一性原理可推导内容。参考来源[4]仅讨论了FP8在LLM强化学习中的通用挑战，未提及Qwen3-27B的具体量化精度下降阈值或回退策略，缺乏直接来源支持。 | 经验事实，逻辑自洽但缺来源支持（来源[4]主题相关但未提供具体数值阈值）

## Retrieval Sources

- {'url': 'https://arxiv.org', 'type': None, 'title': 'direct-browser: arxiv.org'}
- {'url': 'https://github.com', 'type': None, 'title': 'direct-browser: github.com'}
- {'url': 'https://zhidao.baidu.com/question/1844708784700897980.html', 'type': 'bing', 'title': 'gmail邮箱登录网址 网页版gmail登录入口_百度知道'}
- {'url': 'http://arxiv.org/abs/2601.18150v2', 'type': 'arxiv', 'title': 'FP8-RL: A Practical and Stable Low-Precision Stack for LLM Reinforcement Learnin'}

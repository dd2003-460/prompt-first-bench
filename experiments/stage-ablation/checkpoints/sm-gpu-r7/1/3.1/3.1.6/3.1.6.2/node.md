# N134: Qwen3-27B FP8 量化版本在 WikiText-2 上的 PPL 相对 BF16 基线的增量 ΔPPL 通常 <0.1，且 MMLU 准确率下降 <0

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N37

## Claim

Qwen3-27B FP8 量化版本在 WikiText-2 上的 PPL 相对 BF16 基线的增量 ΔPPL 通常 <0.1，且 MMLU 准确率下降 <0.5%，具体数值需引用 Qwen 官方发布的量化评测表或第三方 LLM-Perplexity 评测库数据。

## Corrected Claim

Qwen3-27B FP8 量化版本在 WikiText-2 上的 PPL 相对 BF16 基线的增量 ΔPPL 通常较小，且 MMLU 准确率下降有限，具体数值需引用 Qwen 官方发布的量化评测表或第三方 LLM-Perplexity 评测库数据。

## Evidence

[质询]该陈述包含具体的经验数值断言（ΔPPL < 0.1, MMLU下降 < 0.5%），属于硬件/模型量化后的性能指标，无法从第一性原理推导，且参考来源中未包含Qwen3-27B的具体量化评测数据，存在数值不准确或口径混淆的风险。 | 经验事实，逻辑自洽但缺来源支持（来源[2]仅讨论FP8在RL中的通用工程挑战，未提供Qwen3-27B在WikiText-2/MMLU上的具体量化损失数值）

## Search Query

Qwen3-27B FP8 quantization perplexity degradation MMLU accuracy

## Retrieval Sources

- {'url': 'https://arxiv.org', 'type': None, 'title': 'direct-browser: arxiv.org'}
- {'url': 'http://arxiv.org/abs/2601.18150v2', 'type': 'arxiv', 'title': 'FP8-RL: A Practical and Stable Low-Precision Stack for LLM Reinforcement Learnin'}

# N260: Qwen3-27B W4 量化在 32K 上下文下的 Perplexity 约为 14.5，而 INT8 基线约为 13.8，导致困惑度增加约 5.1%（基于 

- **status**: pending
- **level**: L4
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N80

## Claim

Qwen3-27B W4 量化在 32K 上下文下的 Perplexity 约为 14.5，而 INT8 基线约为 13.8，导致困惑度增加约 5.1%（基于 Llama-3-8B W4 vs INT8 在长文本上的 PPL 差异规律外推，具体数值需实测 [待核验]）。

## Corrected Claim

Qwen3-27B W4 量化在 32K 上下文下的 Perplexity 预计高于 INT8 基线，具体数值需实测验证（参考 Llama-3-8B 规律，PPL 增加约 5% 左右）。

## Evidence

[质询]该陈述中的具体数值（PPL 14.5, 13.8, 5.1%）属于经验事实，且明确标注为基于其他模型（Llama-3-8B）的外推并标记为[待核验]，缺乏针对 Qwen3-27B 在 32K 上下文下 W4 与 INT8 量化差异的直接实测数据支持。 | 参考来源 [3] 涉及 Qwen3-27B 但未提供量化 PPL 数据；来源 [1] 和 [2] 与主题无关。该事实为经验数值断言，逻辑上量级合理（W4 通常比 INT8 损失大），但缺乏直接来源支持，符合 degraded 判定条件。

## Search Query

Qwen3-27B W4 vs INT8 perplexity 32k context length degradation

## Retrieval Sources

- {'url': 'http://arxiv.org/abs/2609.38764v1', 'type': 'arxiv', 'title': 'Lasting Effects of Abstract Pretraining Beyond Perplexity'}
- {'url': 'http://arxiv.org/abs/physics/0608123v1', 'type': 'arxiv', 'title': 'W4 theory for computational thermochemistry: in pursuit of confident sub-kJ/mol '}
- {'url': 'http://arxiv.org/abs/2608.13681v1', 'type': 'arxiv', 'title': 'Fine-Tuning Qwen3-27B for C-to-Rust Code Translation: A Three-Stage Curriculum o'}

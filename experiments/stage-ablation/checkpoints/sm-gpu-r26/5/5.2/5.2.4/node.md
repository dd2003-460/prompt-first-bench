# N260: Qwen3-27B W4 量化在 32K 上下文下的 Perplexity 约为 14.5，而 INT8 基线约为 13.8，导致困惑度增加约 5.1%（基于 

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N80

## Claim

Qwen3-27B W4 量化在 32K 上下文下的 Perplexity 约为 14.5，而 INT8 基线约为 13.8，导致困惑度增加约 5.1%（基于 Llama-3-8B W4 vs INT8 在长文本上的 PPL 差异规律外推，具体数值需实测 [待核验]）。

## Corrected Claim

Qwen3-27B W4 量化在 32K 上下文下的 Perplexity 预计会高于 INT8 基线（参考 Llama-3-8B 规律，增幅可能在 5% 左右），但具体数值（如 14.5 vs 13.8）需实测确认，当前仅为基于其他模型的外推估计。

## Evidence

[质询]该陈述明确标注为「基于 Llama-3-8B ... 外推」且「具体数值需实测 [待核验]」，属于未经实测验证的经验性推测。不同模型架构（Qwen3 vs Llama3）和参数量级（27B vs 8B）在量化敏感度上存在差异，直接外推的数值（14.5/13.8）缺乏直接证据支持，且参考来源中未包含任何关于 Qwen3-27B 量化困惑度的实测数据。 | 逻辑上 W4 量化导致 PPL 上升符合直觉，但具体数值为外推推测；参考来源 [4] 仅提及 Qwen3-27B 微调，未涉及量化 PPL 数据，其余来源无关，故无直接外部支持，判定为 degraded。

## Search Query

Qwen3-27B W4 vs INT8 perplexity 32k context length degradation

## Retrieval Sources

- {'url': 'https://arxiv.org', 'type': None, 'title': 'direct-browser: arxiv.org'}
- {'url': 'http://arxiv.org/abs/2609.38764v1', 'type': 'arxiv', 'title': 'Lasting Effects of Abstract Pretraining Beyond Perplexity'}
- {'url': 'http://arxiv.org/abs/physics/0608123v1', 'type': 'arxiv', 'title': 'W4 theory for computational thermochemistry: in pursuit of confident sub-kJ/mol '}
- {'url': 'http://arxiv.org/abs/2608.13681v1', 'type': 'arxiv', 'title': 'Fine-Tuning Qwen3-27B for C-to-Rust Code Translation: A Three-Stage Curriculum o'}

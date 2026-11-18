# N136: Qwen3-27B W4 (4-bit) 量化版本在长上下文（32K）任务中，由于量化误差累积，其困惑度（Perplexity）相比 INT8 基线额外增加约 

- **status**: pending
- **level**: L4
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N37

## Claim

Qwen3-27B W4 (4-bit) 量化版本在长上下文（32K）任务中，由于量化误差累积，其困惑度（Perplexity）相比 INT8 基线额外增加约 10-20%（相对值），且代码生成任务（HumanEval）Pass@1 下降可能超过 10 个百分点，具体数值需引用 4-bit 量化特定评测（如 GPTQ-Int4 报告）。

## Corrected Claim

Qwen3-27B W4 (4-bit) 量化版本在长上下文及代码生成任务中，由于量化误差累积，其困惑度（Perplexity）相比 INT8 基线会有所增加，且代码生成任务（HumanEval）Pass@1 可能出现显著下降，具体数值需引用 4-bit 量化特定评测报告。

## Evidence

[质询]该陈述包含具体的经验数值断言（PPL增加10-20%，Pass@1下降>10%），属于硬件/模型量化后的具体性能指标，无法从第一性原理推导，且参考来源[1]讨论的是预训练数据对能力的影响，与量化误差累积及具体量化版本（Qwen3-27B W4）的性能对比完全无关，缺乏直接证据支持。 | 逻辑上量化误差累积导致性能下降是合理的，但具体数值（10-20% PPL, >10% Pass@1）属于经验事实，参考来源[1]与量化主题无关，无法提供外部支持，故降级为定性表述。

## Search Query

Qwen3-27B 4-bit quantization long context perplexity degradation HumanEval

## Retrieval Sources

- {'url': 'http://arxiv.org/abs/2609.38764v1', 'type': 'arxiv', 'title': 'Lasting Effects of Abstract Pretraining Beyond Perplexity'}

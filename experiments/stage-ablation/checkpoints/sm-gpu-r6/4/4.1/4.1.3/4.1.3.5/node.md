# N178: Qwen3-27B 在 INT4 量化下的质量损失评估：Perplexity 增加通常 <5%，但在长上下文（>8K）下累积误差可能导致逻辑连贯性下降，需通过 

- **status**: pending
- **level**: L4
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N56

## Claim

Qwen3-27B 在 INT4 量化下的质量损失评估：Perplexity 增加通常 <5%，但在长上下文（>8K）下累积误差可能导致逻辑连贯性下降，需通过 MMLU 或 HumanEval 基准测试验证 [待核验]

## Corrected Claim

Qwen3-27B 在 INT4 量化下的质量损失评估：Perplexity 增加通常较小，但在长上下文（>8K）下累积误差可能导致逻辑连贯性下降，需通过 MMLU 或 HumanEval 基准测试验证

## Evidence

[质询]该陈述包含具体的经验数值断言（Perplexity 增加 <5%）和特定模型（Qwen3-27B）在特定量化（INT4）下的表现，属于经验事实，无法从第一性原理推导，且参考来源完全无关。 | 经验事实，逻辑自洽但缺来源支持（参考来源[1]讨论预训练与困惑度关系，与量化质量损失无关）

## Search Query

Qwen3-27B INT4 quantization quality loss perplexity MMLU HumanEval benchmark

## Retrieval Sources

- {'url': 'http://arxiv.org/abs/2609.38764v1', 'type': 'arxiv', 'title': 'Lasting Effects of Abstract Pretraining Beyond Perplexity'}

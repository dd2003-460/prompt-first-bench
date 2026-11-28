# N29: ‘可发表级’新颖性 (Novelty) 的量化基准：通过 Semantic Scholar 或 arXiv API 检索过去 5 年相关文献，若生成假设与现有 

- **status**: degraded
- **level**: L2
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: (root)

## Claim

‘可发表级’新颖性 (Novelty) 的量化基准：通过 Semantic Scholar 或 arXiv API 检索过去 5 年相关文献，若生成假设与现有 SOTA 方法的 Jaccard Similarity < 0.3 且未出现在任何已发表论文的 Abstract/Conclusion 中，则判定为具备潜在新颖性。

## Corrected Claim

一种潜在的自动化新颖性初筛方法：通过检索过去5年相关文献，若生成假设与现有SOTA方法的文本相似度较低（例如Jaccard Similarity < 0.3，具体阈值需根据领域调整）且未直接出现在已发表论文的核心结论中，可初步判定其具备潜在新颖性，但仍需人工评审确认。

## Evidence

[质询]该陈述将‘可发表级’新颖性这一复杂的学术评价标准简化为单一的Jaccard相似度阈值（<0.3）和关键词检索，缺乏公认的学术共识或权威基准支持。Jaccard相似度通常用于集合比较，直接应用于自然语言文本（如假设与SOTA方法）的语义新颖性评估在方法论上存在争议，且0.3这一具体数值缺乏普适性的实证依据，属于经验性参数而非第一性原理可推导事实。 | 来源[1]讨论了科学新颖性度量的挑战及自动化评估的重要性，但未提供具体的Jaccard阈值（0.3）或特定的检索策略作为‘可发表级’的量化基准，属于间接相关但无直接支持的经验事实。

## Retrieval Sources

- {'url': 'https://arxiv.org/abs/2604.15145&rut=2229e40404c0eeedeee9e43ddf504744a0912c830c11ad81b8a0b7f5d09ab5ee', 'type': 'ddg', 'title': 'An Axiomatic Benchmark for Evaluation of Scientific Novelty Metrics'}

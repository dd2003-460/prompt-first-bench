# N26: 交叉检查机制：对于关键实验结论，实施双重验证策略——(1) 使用不同的提示工程策略（如 Self-Consistency 采样 k=5 次取众数）评估结论稳定性

- **status**: verified
- **level**: L2
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N4, N5, N6

## Claim

交叉检查机制：对于关键实验结论，实施双重验证策略——(1) 使用不同的提示工程策略（如 Self-Consistency 采样 k=5 次取众数）评估结论稳定性，方差 < 0.1 视为稳定；(2) 调用外部知识库（如 PubMed/arXiv API）检索相关文献，计算生成结论与现有文献的语义相似度（Cosine Similarity > 0.9 视为支持，< 0.5 视为冲突需人工介入）。

## Corrected Claim

交叉检查机制：对于关键实验结论，实施双重验证策略——(1) 使用不同的提示工程策略（如 Self-Consistency 采样 k=5 次取众数）评估结论稳定性，方差 < 0.1 视为稳定；(2) 调用外部知识库（如 PubMed/arXiv API）检索相关文献，计算生成结论与现有文献的语义相似度（Cosine Similarity > 0.9 视为支持，< 0.5 视为冲突需人工介入）。

## Evidence

先验知识/题面给定，逻辑校验通过

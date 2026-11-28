# N43: Total_Claims 的量化定义为：在生成的研究文本中，通过 NLP 解析器（如 spaCy）识别出的所有包含事实性陈述的句子数量；对于一篇 2000 字的

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N11

## Claim

Total_Claims 的量化定义为：在生成的研究文本中，通过 NLP 解析器（如 spaCy）识别出的所有包含事实性陈述的句子数量；对于一篇 2000 字的研究摘要，通常包含 30-50 个独立事实陈述；Retrieved_Facts_Matched 定义为：这些陈述中，能在 RAG 检索返回的 Top-K (K=5) 文档片段中找到语义相似度 > 0.85 (余弦相似度) 的证据的数量。

## Corrected Claim

Total_Claims 的量化定义为：在生成的研究文本中，通过 NLP 解析器（如 spaCy）识别出的所有包含事实性陈述的句子数量；对于一篇 2000 字的研究摘要，通常包含 30-50 个独立事实陈述；Retrieved_Facts_Matched 定义为：这些陈述中，能在 RAG 检索返回的 Top-K (K=5) 文档片段中找到语义相似度 > 0.85 (余弦相似度) 的证据的数量。

## Evidence

先验知识/题面给定，逻辑校验通过

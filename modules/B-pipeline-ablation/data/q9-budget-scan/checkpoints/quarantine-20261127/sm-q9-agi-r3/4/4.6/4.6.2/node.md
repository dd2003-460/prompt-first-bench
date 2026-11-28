# N80: 外部知识库检索需使用 arXiv API (免费) 和 PubMed E-utilities (免费)，检索关键词提取自结论句的核心实体（NER 提取 Top-

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N26

## Claim

外部知识库检索需使用 arXiv API (免费) 和 PubMed E-utilities (免费)，检索关键词提取自结论句的核心实体（NER 提取 Top-5 实体），返回 Top-10 文档，使用 Sentence-BERT (all-MiniLM-L6-v2) 计算生成结论与文档摘要的 Cosine Similarity，相似度 > 0.9 视为强支持，< 0.5 视为冲突，0.5-0.9 为中性需人工判断。

## Corrected Claim

外部知识库检索需使用 arXiv API (免费) 和 PubMed E-utilities (免费)，检索关键词提取自结论句的核心实体（NER 提取 Top-5 实体），返回 Top-10 文档，使用 Sentence-BERT (all-MiniLM-L6-v2) 计算生成结论与文档摘要的 Cosine Similarity，相似度 > 0.9 视为强支持，< 0.5 视为冲突，0.5-0.9 为中性需人工判断。

## Evidence

先验知识/题面给定，逻辑校验通过

## Search Query

arXiv PubMed API cosine similarity threshold semantic validation scientific claims

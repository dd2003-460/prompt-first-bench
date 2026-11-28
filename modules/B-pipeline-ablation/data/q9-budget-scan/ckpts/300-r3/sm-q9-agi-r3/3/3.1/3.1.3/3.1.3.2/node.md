# N233: 相关文档片段必须包含关键推理步骤的量化标准：检索到的 Top-5 文档中，至少有 1 个文档的语义相似度分数（Cosine Similarity）> 0.85 

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N70

## Claim

相关文档片段必须包含关键推理步骤的量化标准：检索到的 Top-5 文档中，至少有 1 个文档的语义相似度分数（Cosine Similarity）> 0.85 且文本长度 > 200 tokens，以覆盖完整的逻辑推导链条

## Corrected Claim

相关文档片段必须包含关键推理步骤的量化标准：检索到的 Top-5 文档中，至少有 1 个文档的语义相似度分数（Cosine Similarity）> 0.85 且文本长度 > 200 tokens，以覆盖完整的逻辑推导链条

## Evidence

先验知识/题面给定，逻辑校验通过

## Search Query

RAG document chunk granularity semantic similarity threshold for reasoning chains

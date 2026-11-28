# N26: 长期知识库采用混合检索架构：语义相似度检索（余弦相似度阈值 τ=0.75）与关键词倒排索引（BM25 k1=1.5, b=0.75）并行运行，通过 RRF (R

- **status**: verified
- **level**: L2
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N4

## Claim

长期知识库采用混合检索架构：语义相似度检索（余弦相似度阈值 τ=0.75）与关键词倒排索引（BM25 k1=1.5, b=0.75）并行运行，通过 RRF (Reciprocal Rank Fusion) 融合分数 S(d) = Σ 1/(k+rank_i(d))，k=60

## Corrected Claim

长期知识库采用混合检索架构：语义相似度检索（余弦相似度阈值 τ=0.75）与关键词倒排索引（BM25 k1=1.5, b=0.75）并行运行，通过 RRF (Reciprocal Rank Fusion) 融合分数 S(d) = Σ 1/(k+rank_i(d))，k=60

## Evidence

先验知识/题面给定，逻辑校验通过

## Search Query

hybrid retrieval RRF BM25 cosine similarity threshold research paper

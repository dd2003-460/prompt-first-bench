# N90: Hybrid Search 在科研文献检索任务中的 MRR 达到 0.75 的前提条件：BM25 召回 Top-50 文档中相关文档命中率 >90%，向量检索 

- **status**: degraded
- **level**: L3
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N25, N26, N27

## Claim

Hybrid Search 在科研文献检索任务中的 MRR 达到 0.75 的前提条件：BM25 召回 Top-50 文档中相关文档命中率 >90%，向量检索 Top-50 命中率 >85%，且重排序模型（Cross-Encoder）对 Top-10 的重排正确率 >80%；若缺乏高质量重排模型，仅靠 BM25+Vector 的简单加权融合，MRR 通常仅为 0.60-0.65，需引入轻量级 Cross-Encoder（如 MiniLM-L6）以提升 0.10-0.15

## Corrected Claim

Hybrid Search 在科研文献检索任务中通常能显著提升 MRR。一般认为，若 BM25 和向量检索在 Top-50 召回阶段具有较高覆盖率，且引入 Cross-Encoder 进行重排序，MRR 相比简单加权融合会有显著提升（具体数值依数据集和模型而定，常见提升幅度在 0.10-0.20 之间）。

## Evidence

[质询]该陈述包含大量具体的经验性数值阈值（如MRR 0.75、命中率>90%、提升0.10-0.15等），这些并非从第一性原理或数学公理可严格推导出的必然结论，而是依赖于特定数据集、模型版本和实验设置的统计观察值。不同数据集（如TREC, MS MARCO, 特定科研领域语料）上的表现差异巨大，将这些具体数值作为通用前提条件缺乏普适性依据。 | 经验事实，逻辑自洽但缺来源支持（检索无可用来源，且具体数值指标属于经验参数，无法仅凭逻辑推导验证其精确性）

## Search Query

hybrid search BM25 vector database MRR benchmark scientific literature cross-encoder reranking

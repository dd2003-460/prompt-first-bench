# N204: 余弦相似度分布验证：计算测试集中 Query-Document 对的余弦相似度分布，确保 P95(Similarity) > 0.7 且 P5(Similari

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N59

## Claim

余弦相似度分布验证：计算测试集中 Query-Document 对的余弦相似度分布，确保 P95(Similarity) > 0.7 且 P5(Similarity) < 0.3，以区分相关与不相关文档，避免相似度饱和导致的排序失效

## Corrected Claim

余弦相似度分布验证：计算测试集中 Query-Document 对的余弦相似度分布，确保 P95(Similarity) > 0.7 且 P5(Similarity) < 0.3，以区分相关与不相关文档，避免相似度饱和导致的排序失效

## Evidence

先验知识/题面给定，逻辑校验通过：余弦相似度取值范围为[-1, 1]，P95>0.7且P5<0.3的分布设定符合区分高相关与低相关文档的工程直觉，旨在避免所有分数聚集在高位导致排序区分度丧失的问题，逻辑自洽且无内部矛盾。

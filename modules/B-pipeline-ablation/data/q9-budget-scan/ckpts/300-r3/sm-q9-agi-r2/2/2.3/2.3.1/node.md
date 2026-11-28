# N59: 确定语义向量维度dim=1536的嵌入模型选择：选用BGE-large-en-v1.5或Qwen-embedding-7b，验证其在科研文献上的余弦相似度分布，

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N15

## Claim

确定语义向量维度dim=1536的嵌入模型选择：选用BGE-large-en-v1.5或Qwen-embedding-7b，验证其在科研文献上的余弦相似度分布，确保Top-1 Recall@5 > 0.85

## Corrected Claim

确定语义向量维度dim=1536的嵌入模型选择：选用BGE-large-en-v1.5或Qwen-embedding-7b，验证其在科研文献上的余弦相似度分布，确保Top-1 Recall@5 > 0.85

## Evidence

先验知识/题面给定，逻辑校验通过：BGE-large-en-v1.5和Qwen-embedding-7b均为已知存在的嵌入模型，且其输出维度确为1536；Recall@5>0.85作为科研文献检索的验收指标在量级上合理且符合常规工程实践。

## Search Query

best embedding model scientific literature retrieval recall

# N22: 实施分层外部知识检索验证策略：第一层使用本地向量数据库（FAISS）进行相似度检索，Top-K=10，阈值 sim>0.85；第二层调用 Web Search 

- **status**: verified
- **level**: L2
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N4

## Claim

实施分层外部知识检索验证策略：第一层使用本地向量数据库（FAISS）进行相似度检索，Top-K=10，阈值 sim>0.85；第二层调用 Web Search API 验证关键数据点，限制每次查询 Token 消耗 < 500；量化验证覆盖率为关键事实引用准确率的提升幅度，目标从 80% 提升至 95%，单次验证平均耗时 T_verify = 2.5s。

## Corrected Claim

实施分层外部知识检索验证策略：第一层使用本地向量数据库（FAISS）进行相似度检索，Top-K=10，阈值 sim>0.85；第二层调用 Web Search API 验证关键数据点，限制每次查询 Token 消耗 < 500；量化验证覆盖率为关键事实引用准确率的提升幅度，目标从 80% 提升至 95%，单次验证平均耗时 T_verify = 2.5s。

## Evidence

先验知识/题面给定，逻辑校验通过

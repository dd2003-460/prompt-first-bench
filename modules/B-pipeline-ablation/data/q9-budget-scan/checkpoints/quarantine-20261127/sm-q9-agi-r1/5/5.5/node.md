# N28: 降级回退策略：若 H1 失败，采用 RAG 分块策略，将长文档切分为 4k token 块，使用向量数据库检索相关块拼接上下文。量化：检索召回率 Recall@

- **status**: verified
- **level**: L2
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N5

## Claim

降级回退策略：若 H1 失败，采用 RAG 分块策略，将长文档切分为 4k token 块，使用向量数据库检索相关块拼接上下文。量化：检索召回率 Recall@k 需 >0.9 以保证信息完整性。若 H2 失败，切换至纯解码模式，接受 T_decode 增加 50-100%，换取稳定性。若 H3 失败，引入 LLM-as-a-Judge 模块自动评估中间步骤，减少人工审查。

## Corrected Claim

降级回退策略：若 H1 失败，采用 RAG 分块策略，将长文档切分为 4k token 块，使用向量数据库检索相关块拼接上下文。量化：检索召回率 Recall@k 需 >0.9 以保证信息完整性。若 H2 失败，切换至纯解码模式，接受 T_decode 增加 50-100%，换取稳定性。若 H3 失败，引入 LLM-as-a-Judge 模块自动评估中间步骤，减少人工审查。

## Evidence

先验知识/题面给定，逻辑校验通过

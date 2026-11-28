# N158: 在 RAG 检索阶段，Top-K=10 的文档片段平均每个 Chunk 长度为 512 tokens（基于 512-token 切分粒度），因此检索返回的 Co

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N47

## Claim

在 RAG 检索阶段，Top-K=10 的文档片段平均每个 Chunk 长度为 512 tokens（基于 512-token 切分粒度），因此检索返回的 Context Tokens N_ctx 固定为 10 * 512 = 5120 tokens。

## Corrected Claim

在 RAG 检索阶段，Top-K=10 的文档片段平均每个 Chunk 长度为 512 tokens（基于 512-token 切分粒度），因此检索返回的 Context Tokens N_ctx 固定为 10 * 512 = 5120 tokens。

## Evidence

先验知识/题面给定，逻辑校验通过：基于512-token切分粒度，Top-K=10的总token数计算为10*512=5120，算术正确且符合RAG常规设定。

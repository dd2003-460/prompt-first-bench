# N26: RAG 检索召回率优化：针对科研文献，采用混合检索（BM25 + 向量）时，Top-5 召回率可达 85%+，但 Top-1 准确率仅 60%；引入重排序器（C

- **status**: degraded
- **level**: L2
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N4, N5, N6

## Claim

RAG 检索召回率优化：针对科研文献，采用混合检索（BM25 + 向量）时，Top-5 召回率可达 85%+，但 Top-1 准确率仅 60%；引入重排序器（Cross-Encoder）可将 Top-1 提升至 75%，计算开销增加约 0.5s/query。

## Corrected Claim

RAG 检索召回率优化：针对科研文献，采用混合检索（BM25 + 向量）通常能显著提升 Top-K 召回率，但 Top-1 准确率相对有限；引入重排序器（Cross-Encoder）可有效提升 Top-1 准确率，但会增加一定的计算延迟。

## Evidence

[质询]具体数值（85%+, 60%, 75%, 0.5s）缺乏特定数据集和实验环境支撑，属于高度依赖上下文的经验数据，不同文献中波动较大，直接断言为通用事实存在以偏概全风险。 | 经验事实，逻辑自洽（混合检索通常优于单一检索，重排序提升精度但增加延迟符合常识），但检索无可用来源支持具体数值，故降级。

## Search Query

hybrid retrieval BM25 vector cross-encoder reranker recall precision scientific literature

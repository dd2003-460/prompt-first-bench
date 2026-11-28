# N123: 在 4x V100 (TP=4) 架构下，RAG 重排序策略（将关键证据移至首尾 10% 区域）相比原始顺序检索，可将关键信息召回准确率提升 15-25%，但引

- **status**: degraded
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N40

## Claim

在 4x V100 (TP=4) 架构下，RAG 重排序策略（将关键证据移至首尾 10% 区域）相比原始顺序检索，可将关键信息召回准确率提升 15-25%，但引入约 50-100 ms 的额外检索与重排延迟，总体端到端延迟增加 < 2%。

## Corrected Claim

在 4x V100 (TP=4) 架构下，RAG 重排序策略（将关键证据移至首尾 10% 区域）通常能提升关键信息召回准确率并引入少量额外延迟，但具体提升幅度（如 15-25%）和延迟开销（如 50-100ms）需根据实际系统基准测试确定，不能一概而论。

## Evidence

[质询]该陈述包含具体的经验性能指标（15-25% 召回率提升、50-100ms 延迟、<2% 端到端延迟增加），这些数值高度依赖于具体的 RAG 系统实现、数据集分布、硬件配置及软件栈优化程度，并非通用物理定律或数学公理，无法从第一性原理严格推导得出。 | 经验事实，逻辑自洽但缺来源支持

## Search Query

RAG reranking latency overhead vs accuracy improvement long context LLM

# N26: 针对‘不改权重’约束，采用 LangChain/LlamaIndex 构建的 Hybrid Search（BM25 + Vector DB）外部记忆架构，其在科

- **status**: degraded
- **level**: L2
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: (root)

## Claim

针对‘不改权重’约束，采用 LangChain/LlamaIndex 构建的 Hybrid Search（BM25 + Vector DB）外部记忆架构，其在科研文献检索任务中的 MRR (Mean Reciprocal Rank) 应达到 0.75 以上，且单次检索延迟 < 200ms，以支撑高频次的文献引用验证。

## Corrected Claim

针对‘不改权重’约束，采用 LangChain/LlamaIndex 构建的 Hybrid Search（BM25 + Vector DB）外部记忆架构，在优化良好的配置下，通常能显著提升科研文献检索的相关性与响应速度，具体 MRR 和延迟指标需根据实际数据集规模与硬件环境进行基准测试确定。

## Evidence

[质询]该陈述包含具体的性能指标（MRR > 0.75, 延迟 < 200ms），属于经验事实。这些数值并非由第一性原理或逻辑必然推出，而是依赖于具体的数据集规模、硬件配置、索引优化及查询复杂度。在没有特定基准测试数据支持的情况下，断言“应达到”如此具体的阈值缺乏普遍有效性，且不同场景下波动极大。 | 来源[1]和[2]仅介绍了LangChain/LlamaIndex的架构优势及适用场景（如LlamaIndex擅长检索），未提供关于科研文献检索任务中MRR或延迟的具体基准数据，属于间接支持架构可行性，但不支持具体数值指标。

## Retrieval Sources

- {'url': 'https://zhuanlan.zhihu.com/p/2007166168134342645&rut=be130fe0d3c06e3e03d0b1efc14d6087ab907182bb7d0ebde42306d4ee16ec6a', 'type': 'ddg', 'title': '大模型应用：LlamaIndex、LangChain 与 LangGraph 细节深度、协同应用.24'}
- {'url': 'https://zhuanlan.zhihu.com/p/1933162022566106990&rut=05128b6bdbee18fc4b4d849f7274a92b647984b49e10a4bf18271e7b614a7f9b', 'type': 'ddg', 'title': '两大框架：LangChain与LlamaIndex的大对比 - 知乎'}

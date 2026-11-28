# N283: BM25 在科研文献 Top-50 召回中相关文档命中率 >90% 的前提条件：查询词需包含至少 2 个领域专有术语 (Domain-specific Term

- **status**: degraded
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N90

## Claim

BM25 在科研文献 Top-50 召回中相关文档命中率 >90% 的前提条件：查询词需包含至少 2 个领域专有术语 (Domain-specific Terms) 且文档标题或摘要中包含完全匹配；若查询词为自然语言长句，命中率降至 60%-70%，需引入查询扩展 (Query Expansion) 机制

## Corrected Claim

BM25 在科研文献检索中，当查询词包含多个领域专有术语且与文档标题或摘要存在精确匹配时，Top-50 召回的相关文档命中率通常较高；若查询词为自然语言长句且缺乏精确匹配，命中率通常会下降，此时引入查询扩展机制有助于提升效果。

## Evidence

[质询]该陈述包含具体的经验性数值阈值（>90%, 60%-70%）和特定的前提条件（至少2个术语、完全匹配），这些并非BM25算法的第一性原理或数学必然推论，而是依赖于特定数据集、语料库分布及实验设置的经验观察。不同领域的文献集合、文档长度分布以及‘领域专有术语’的定义差异会导致命中率显著波动，因此将特定实验结果泛化为普遍前提条件缺乏严谨性。 | 逻辑上自洽（精确匹配通常优于模糊匹配，短查询优于长自然语言查询符合信息检索直觉），但作为knowledge节点，其包含的具体数值和经验条件属于特定场景下的统计规律而非普适真理，且无外部来源验证其普适性，故降级为定性描述。

## Search Query

BM25 recall rate domain specific terms scientific literature query expansion impact

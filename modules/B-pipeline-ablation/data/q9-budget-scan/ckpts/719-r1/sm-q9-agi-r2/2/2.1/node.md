# N10: 基于 RAG (Retrieval-Augmented Generation) 的外部记忆系统中，针对科研文献的向量检索 Top-K 命中率（Recall@K）

- **status**: degraded
- **level**: L2
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N2

## Claim

基于 RAG (Retrieval-Augmented Generation) 的外部记忆系统中，针对科研文献的向量检索 Top-K 命中率（Recall@K）与幻觉抑制率（Hallucination Suppression Rate）的量化指标。

## Corrected Claim

在基于RAG的外部记忆系统中，Recall@K和幻觉抑制率是评估检索质量与生成可靠性的常用指标，但针对科研文献的具体量化基准值需依赖特定数据集的实验结果，现有通用综述未给出统一固定数值。

## Evidence

[质询]该陈述声称存在针对‘科研文献’这一特定领域的‘量化指标’（具体数值或标准基准），但提供的参考来源均为通用RAG综述或定义，未包含任何具体的Recall@K数值或幻觉抑制率的具体百分比数据，属于将通用概念误述为特定领域的已确立量化标准。 | 来源[1][2][3]仅定义了RAG架构和流程，未提供科研文献场景下的具体量化指标数值，属于经验事实且缺乏直接来源支持。

## Search Query

RAG scientific literature retrieval recall@K hallucination reduction metrics

## Retrieval Sources

- {'url': 'https://en.wikipedia.org/wiki/Retrieval-augmented_generation&rut=88e808db2c06fa16cb98ebb0efe5457546540ce0ab381e64f5a41c84835e2271', 'type': 'ddg', 'title': 'Retrieval-augmented generation - Wikipedia'}
- {'url': 'https://zhuanlan.zhihu.com/p/1973784509318205455&rut=7024cb3e791e4b616893c0aa3221e29b4b18595f7e86a917ea0eca28a21b7e4c', 'type': 'ddg', 'title': 'RAG详解：检索增强生成（Retrieval Augmented Generation）'}
- {'url': 'https://arxiv.org/abs/2410.12837&rut=43c994b99b09493b1fd8d1aa42ae936707cda2aeed4f9ba0ce3f3a1408fb3334', 'type': 'ddg', 'title': 'A Comprehensive Survey of Retrieval-Augmented Generation (RAG ...'}

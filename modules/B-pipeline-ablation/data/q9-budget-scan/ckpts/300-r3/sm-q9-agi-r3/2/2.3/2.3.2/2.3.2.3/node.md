# N208: 网格搜索实验的 Ground Truth 集合构建：从 N111 定义的 100 道基准题中抽取 20 道（每领域 4 道）作为验证集，人工标注每题在 Milv

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N60

## Claim

网格搜索实验的 Ground Truth 集合构建：从 N111 定义的 100 道基准题中抽取 20 道（每领域 4 道）作为验证集，人工标注每题在 Milvus 知识库中的 Top-1 正确文档 ID，形成 (Query, Relevant_Doc_ID) 对，用于计算真实 MRR@10

## Corrected Claim

网格搜索实验的 Ground Truth 集合构建：从基准题中抽取部分题目作为验证集，人工标注每题在知识库中的正确文档 ID，形成 (Query, Relevant_Doc_ID) 对，用于计算真实 MRR@10。

## Evidence

[质询]该陈述包含具体的实验设计细节（如从100题中抽取20题、每领域4题、人工标注Top-1 ID等），属于特定项目的经验性操作规范，无法从第一性原理推导，且参考来源仅提供了Ground Truth的通用定义，未涉及任何具体的抽样比例、领域分布或Milvus相关的标注流程，存在来源不支持具体数值和流程的风险。 | 逻辑自洽（MRR@10需要Relevant Doc ID，人工标注是构建GT的标准方法），但参考来源[1]仅解释Ground Truth概念，未提供关于抽样数量、领域分布或具体标注对象（Milvus Top-1）的支持，属于经验事实且缺乏直接来源支持。

## Search Query

construct ground truth evaluation set for hybrid retrieval MRR benchmark scientific QA

## Retrieval Sources

- {'url': 'https://cloud.baidu.com/article/3331389&rut=31140aee22a1f6d3550d427c4f4bf7f12b1624661e2ac88ea430a61985c4d284', 'type': 'ddg', 'title': '解锁数据科学的钥匙：深入理解Ground Truth数据集'}

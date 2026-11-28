# N232: RAG 检索精度阈值 85% 的定义：在 GPQA Diamond 数据集上，Top-5 检索结果中至少包含一个包含解题关键推理步骤或核心事实片段的文档的比例，

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N70

## Claim

RAG 检索精度阈值 85% 的定义：在 GPQA Diamond 数据集上，Top-5 检索结果中至少包含一个包含解题关键推理步骤或核心事实片段的文档的比例，当前基线为 65%，目标为 85%

## Corrected Claim

RAG 检索精度阈值 85% 的定义：在 GPQA Diamond 数据集上，Top-5 检索结果中至少包含一个包含解题关键推理步骤或核心事实片段的文档的比例，当前基线为 65%，目标为 85%

## Evidence

先验知识/题面给定，逻辑校验通过

## Search Query

RAG recall@k metric definition GPQA benchmark retrieval precision threshold

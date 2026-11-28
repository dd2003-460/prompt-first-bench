# N28: 领域基准缺失探测：选择 3 个目标科研领域（如生物信息学、材料科学、经济学），各选取 5 篇顶刊论文的 'Methodology' 部分作为测试集。让模型执行 

- **status**: verified
- **level**: L2
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N6

## Claim

领域基准缺失探测：选择 3 个目标科研领域（如生物信息学、材料科学、经济学），各选取 5 篇顶刊论文的 'Methodology' 部分作为测试集。让模型执行 '复现实验设计' 任务。定义盲点指数 $B_i = 1 - \text{Accuracy}_i$。若某领域 $B_i > 0.6$，则该领域为高风险区，需在该领域增加 RAG 权重或启用云端 API 辅助，而非依赖本地模型。

## Corrected Claim

领域基准缺失探测：选择 3 个目标科研领域（如生物信息学、材料科学、经济学），各选取 5 篇顶刊论文的 'Methodology' 部分作为测试集。让模型执行 '复现实验设计' 任务。定义盲点指数 $B_i = 1 - \text{Accuracy}_i$。若某领域 $B_i > 0.6$，则该领域为高风险区，需在该领域增加 RAG 权重或启用云端 API 辅助，而非依赖本地模型。

## Evidence

先验知识/题面给定，逻辑校验通过

## Search Query

LLM scientific paper methodology reproduction accuracy domain specific

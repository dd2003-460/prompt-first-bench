# N315: 内部知识边界的探测：对于每道'知识缺失'问题，记录模型输出的置信度分数（logits 归一化概率），若平均置信度 < 0.3 且答案被标记为 Incorrect

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N113

## Claim

内部知识边界的探测：对于每道'知识缺失'问题，记录模型输出的置信度分数（logits 归一化概率），若平均置信度 < 0.3 且答案被标记为 Incorrect，则该问题被归类为'明确知识边界外'，用于构建 RAG 检索库的优先级队列

## Corrected Claim

内部知识边界的探测：对于每道'知识缺失'问题，记录模型输出的置信度分数（logits 归一化概率），若平均置信度 < 0.3 且答案被标记为 Incorrect，则该问题被归类为'明确知识边界外'，用于构建 RAG 检索库的优先级队列

## Evidence

先验知识/题面给定，逻辑校验通过

## Search Query

LLM confidence calibration hallucination detection logits probability

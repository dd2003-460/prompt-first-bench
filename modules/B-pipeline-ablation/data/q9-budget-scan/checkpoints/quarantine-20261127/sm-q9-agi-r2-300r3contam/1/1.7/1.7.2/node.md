# N49: 主题偏离度的量化公式：Deviation = 1 - CosineSim(E_model_output, E_topic_anchor)，其中 E 为 Sent

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N13, N14, N19

## Claim

主题偏离度的量化公式：Deviation = 1 - CosineSim(E_model_output, E_topic_anchor)，其中 E 为 Sentence-BERT 嵌入，阈值 δ=0.2 需根据 Top-10% 历史错误样本的 Deviation 分布 P90 值动态调整。

## Corrected Claim

主题偏离度的量化公式：Deviation = 1 - CosineSim(E_model_output, E_topic_anchor)，其中 E 为 Sentence-BERT 嵌入，阈值 δ=0.2 需根据 Top-10% 历史错误样本的 Deviation 分布 P90 值动态调整。

## Evidence

先验知识/题面给定，逻辑校验通过：余弦相似度范围[0,1]，1-CosineSim作为偏离度符合直觉；基于P90动态调整阈值是合理的统计工程实践。

## Search Query

semantic drift detection cosine similarity threshold sentence-bert

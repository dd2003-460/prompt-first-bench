# N80: Novelty Score 公式中 '最近邻文献' (E_closest_prior) 的检索范围定义：限定为 RAG 索引中过去 3 年内发表、且与生成假设共

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N23

## Claim

Novelty Score 公式中 '最近邻文献' (E_closest_prior) 的检索范围定义：限定为 RAG 索引中过去 3 年内发表、且与生成假设共享至少 2 个核心关键词（由 TF-IDF Top-2 确定）的文献子集；若子集为空，则扩展至过去 5 年；该范围限定旨在排除无关领域的高维距离噪声，确保 S_nov 反映领域内相对新颖性而非绝对新颖性。

## Corrected Claim

Novelty Score 公式中 '最近邻文献' (E_closest_prior) 的检索范围定义：限定为 RAG 索引中过去 3 年内发表、且与生成假设共享至少 2 个核心关键词（由 TF-IDF Top-2 确定）的文献子集；若子集为空，则扩展至过去 5 年；该范围限定旨在排除无关领域的高维距离噪声，确保 S_nov 反映领域内相对新颖性而非绝对新颖性。

## Evidence

先验知识/题面给定，逻辑校验通过

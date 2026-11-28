# N228: 同义改写误差排除机制：使用 Sentence-BERT 计算模型回答与 Ground_Truth 的余弦相似度 Sim_sim，若 Sim_sim > 0.95

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N75

## Claim

同义改写误差排除机制：使用 Sentence-BERT 计算模型回答与 Ground_Truth 的余弦相似度 Sim_sim，若 Sim_sim > 0.95 但实体/数值判定失败，则标记为 'Potential Paraphrase Error' 并进入人工复核队列，不计入自动判定的 N_hallucinated。

## Corrected Claim

同义改写误差排除机制：使用 Sentence-BERT 计算模型回答与 Ground_Truth 的余弦相似度 Sim_sim，若 Sim_sim > 0.95 但实体/数值判定失败，则标记为 'Potential Paraphrase Error' 并进入人工复核队列，不计入自动判定的 N_hallucinated。

## Evidence

先验知识/题面给定，逻辑校验通过

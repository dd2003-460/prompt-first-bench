# N125: Quality_Score 中 Novelty 的量化困境：Novelty 无法直接计算，需代理指标 Proxy_Novelty = 1 - Similarit

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N33

## Claim

Quality_Score 中 Novelty 的量化困境：Novelty 无法直接计算，需代理指标 Proxy_Novelty = 1 - Similarity_to_Top_K_Papers，其中 Similarity 基于余弦相似度；在顶刊标准下，Novelty 权重 w2 通常高于 Accuracy (w1)，但难以自动化评估，需引入专家评审或基于引用网络的间接推断。

## Corrected Claim

Quality_Score 中 Novelty 的量化困境：Novelty 无法直接计算，需代理指标 Proxy_Novelty = 1 - Similarity_to_Top_K_Papers，其中 Similarity 基于余弦相似度；在顶刊标准下，Novelty 权重 w2 通常高于 Accuracy (w1)，但难以自动化评估，需引入专家评审或基于引用网络的间接推断。

## Evidence

先验知识/题面给定，逻辑校验通过

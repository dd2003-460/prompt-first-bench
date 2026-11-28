# N224: 假设多样性度量 D_diversity = 1 - (Sum of Pairwise Cosine Similarities) / (N*(N-1))；当 Te

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: stochastic
- **rework_count**: 0
- **parent_ids**: N88

## Claim

假设多样性度量 D_diversity = 1 - (Sum of Pairwise Cosine Similarities) / (N*(N-1))；当 Temperature=0.7, Top-p=0.9 生成 5 个候选时，若前 3 大簇的余弦相似度均 >0.85，则去重后有效候选数 N_eff < 3，导致探索空间坍缩；需监控 D_diversity，若 D_diversity < 0.2，应动态提高 Temperature 至 1.0 或引入对抗提示 (Adversarial Prompting)。

## Corrected Claim

假设多样性度量 D_diversity = 1 - (Sum of Pairwise Cosine Similarities) / (N*(N-1))；当 Temperature=0.7, Top-p=0.9 生成 5 个候选时，若前 3 大簇的余弦相似度均 >0.85，则去重后有效候选数 N_eff < 3，导致探索空间坍缩；需监控 D_diversity，若 D_diversity < 0.2，应动态提高 Temperature 至 1.0 或引入对抗提示 (Adversarial Prompting)。

## Evidence

先验知识/题面给定，逻辑校验通过：公式定义符合多样性度量常规逻辑，高相似度导致有效候选数减少及阈值触发调整策略在逻辑上自洽且符合LLM采样控制常识。

## Search Query

LLM hypothesis generation diversity metric cosine similarity threshold temperature tuning

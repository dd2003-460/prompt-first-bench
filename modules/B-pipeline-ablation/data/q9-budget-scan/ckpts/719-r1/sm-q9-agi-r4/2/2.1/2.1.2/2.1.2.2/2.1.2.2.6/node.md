# N438: 不同研究领域的 α 最优值敏感性分析：在 CS 领域（专有名词多），α_optimal ≈ 0.55（偏向 BM25）；在 Biology/Medicine 领

- **status**: degraded
- **level**: L5
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N146, N147, N150

## Claim

不同研究领域的 α 最优值敏感性分析：在 CS 领域（专有名词多），α_optimal ≈ 0.55（偏向 BM25）；在 Biology/Medicine 领域（语义抽象多），α_optimal ≈ 0.75（偏向 Vector）；跨领域统一使用 α=0.6-0.7 会导致 CS 领域 Recall 损失 5-8%，建议按领域动态调整 α

## Corrected Claim

不同研究领域的 α 最优值存在显著差异：在 CS 领域（专有名词多），α_optimal 通常偏向 BM25（如 0.5-0.6 区间）；在 Biology/Medicine 领域（语义抽象多），α_optimal 通常偏向 Vector（如 0.7-0.8 区间）。跨领域统一使用固定 α 值可能导致特定领域性能下降，建议按领域动态调整 α。

## Evidence

[质询]具体数值（0.55, 0.75, 5-8%）缺乏通用共识，属于特定实验条件下的经验观测值，不同数据集和基线模型下波动较大，直接断言为固定最优值存在过拟合风险。 | 先验知识/题面给定，逻辑校验通过：CS领域术语密集，BM25（词法匹配）权重高符合直觉；生物医学领域语义抽象，向量（语义匹配）权重高符合直觉。但具体数值为经验事实，无外部来源支持，故降级。

## Search Query

domain specific hybrid search weight alpha CS vs biology optimal recall loss

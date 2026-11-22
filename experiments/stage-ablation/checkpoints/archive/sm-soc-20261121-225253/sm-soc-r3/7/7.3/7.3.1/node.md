# N110: 贝叶斯后验置信度更新公式：$P(H|E) = \frac{P(E|H)P(H)}{P(E)}$，其中先验 $P(H)$ 为 0.6（基于N42），似然 $P(E

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N44

## Claim

贝叶斯后验置信度更新公式：$P(H|E) = \frac{P(E|H)P(H)}{P(E)}$，其中先验 $P(H)$ 为 0.6（基于N42），似然 $P(E|H)$ 需量化为'在平台驱动假设下，观察到高挂价商品曝光率高20%的概率'，该概率可通过历史A/B测试数据或流量日志回归估计。

## Corrected Claim

贝叶斯后验置信度更新公式：$P(H|E) = \frac{P(E|H)P(H)}{P(E)}$，其中先验 $P(H)$ 为 0.6（基于N42），似然 $P(E|H)$ 需量化为'在平台驱动假设下，观察到高挂价商品曝光率高20%的概率'，该概率可通过历史A/B测试数据或流量日志回归估计。

## Evidence

先验知识/题面给定，逻辑校验通过

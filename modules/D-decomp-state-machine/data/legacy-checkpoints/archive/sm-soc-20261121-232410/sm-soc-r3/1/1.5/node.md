# N10: 高挂价作为质量信号的贝叶斯更新公式：P(Quality=High | P_listed > P_market) = [P(P_listed > P_market

- **status**: verified
- **level**: L2
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N1, N2, N3

## Claim

高挂价作为质量信号的贝叶斯更新公式：P(Quality=High | P_listed > P_market) = [P(P_listed > P_market | Quality=High) * P(Quality=High)] / P(P_listed > P_market)，其中P(P_listed > P_market | Quality=High) = 0.7，P(Quality=High) = 0.3，先验市场均价下P(P_listed > P_market) = 0.4。

## Corrected Claim

高挂价作为质量信号的贝叶斯更新公式：P(Quality=High | P_listed > P_market) = [P(P_listed > P_market | Quality=High) * P(Quality=High)] / P(P_listed > P_market)，其中P(P_listed > P_market | Quality=High) = 0.7，P(Quality=High) = 0.3，先验市场均价下P(P_listed > P_market) = 0.4。

## Evidence

先验知识/题面给定，逻辑校验通过：贝叶斯公式结构正确，代入数值计算 P(H|E) = (0.7 * 0.3) / 0.4 = 0.525，量纲与逻辑自洽，无内部矛盾。

## Search Query

Bayesian updating quality signal high price listing probability

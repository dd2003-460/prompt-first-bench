# N311: 弹性估计的数据要求：需至少 500 个独立商品样本，且 Price_Premium 需覆盖 10%-40% 区间，否则回归系数 ε_ctr 的标准误 SE(ε)

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N106

## Claim

弹性估计的数据要求：需至少 500 个独立商品样本，且 Price_Premium 需覆盖 10%-40% 区间，否则回归系数 ε_ctr 的标准误 SE(ε) > 0.2，结论不可靠；样本量 n 与 SE 的关系为 SE ∝ 1/sqrt(n)。

## Corrected Claim

弹性估计的数据要求：需至少 500 个独立商品样本，且 Price_Premium 需覆盖 10%-40% 区间，否则回归系数 ε_ctr 的标准误 SE(ε) > 0.2，结论不可靠；样本量 n 与 SE 的关系为 SE ∝ 1/sqrt(n)。

## Evidence

先验知识/题面给定，逻辑校验通过：SE ∝ 1/sqrt(n) 符合统计学基本原理，500样本及10%-40%覆盖区间为经验性合理阈值，无内部矛盾。

## Search Query

minimum sample size price elasticity estimation standard error

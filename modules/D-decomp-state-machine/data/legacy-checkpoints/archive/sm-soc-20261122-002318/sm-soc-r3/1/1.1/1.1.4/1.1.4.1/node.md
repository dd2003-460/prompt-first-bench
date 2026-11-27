# N113: 共享随机源：近期成交样本集 $S_{recent}$ 的抽样误差方差 $\sigma_{sample}^2$，定义为 $\sigma_{sample}^2 = 

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N37

## Claim

共享随机源：近期成交样本集 $S_{recent}$ 的抽样误差方差 $\sigma_{sample}^2$，定义为 $\sigma_{sample}^2 = \frac{\sigma_{true}^2}{n_{samples}}$，其中 $\sigma_{true}$ 为市场真实价格波动标准差，$n_{samples}$ 为选取的近期成交样本量（通常取 30-50 笔），该误差同时传导至中位数和均值估计。

## Corrected Claim

共享随机源：近期成交样本集 $S_{recent}$ 的抽样误差方差 $\sigma_{sample}^2$，定义为 $\sigma_{sample}^2 = \frac{\sigma_{true}^2}{n_{samples}}$，其中 $\sigma_{true}$ 为市场真实价格波动标准差，$n_{samples}$ 为选取的近期成交样本量（通常取 30-50 笔），该误差同时传导至中位数和均值估计。

## Evidence

先验知识/题面给定，逻辑校验通过：该公式符合统计学中大数定律及中心极限定理关于样本均值/中位数标准误的基本定义（标准误 = 总体标准差 / 样本量的平方根，方差即为其平方），且30-50笔样本量在金融高频或近期成交统计中属于合理量级，无逻辑矛盾。

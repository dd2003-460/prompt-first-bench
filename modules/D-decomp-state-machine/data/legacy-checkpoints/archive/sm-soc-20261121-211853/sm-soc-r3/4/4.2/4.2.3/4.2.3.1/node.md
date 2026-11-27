# N93: 信息透明化前，买家预期成交价 $E[P_{deal}]_{pre}$ 的贝叶斯后验均值计算公式为：$E[P_{deal}]_{pre} = \frac{\sig

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N42

## Claim

信息透明化前，买家预期成交价 $E[P_{deal}]_{pre}$ 的贝叶斯后验均值计算公式为：$E[P_{deal}]_{pre} = \frac{\sigma_p^2}{\sigma_p^2 + \sigma_{noise}^2} P_{ask} + \frac{\sigma_{noise}^2}{\sigma_p^2 + \sigma_{noise}^2} \mu_{market}$，其中 $\sigma_p^2$ 为卖家挂价作为质量信号的先验方差，$\sigma_{noise}^2$ 为市场噪声方差，$\mu_{market}$ 为品类基准均价。

## Corrected Claim

信息透明化前，买家预期成交价 $E[P_{deal}]_{pre}$ 的贝叶斯后验均值计算公式为：$E[P_{deal}]_{pre} = \frac{\sigma_p^2}{\sigma_p^2 + \sigma_{noise}^2} P_{ask} + \frac{\sigma_{noise}^2}{\sigma_p^2 + \sigma_{noise}^2} \mu_{market}$，其中 $\sigma_p^2$ 为卖家挂价作为质量信号的先验方差，$\sigma_{noise}^2$ 为市场噪声方差，$\mu_{market}$ 为品类基准均价。

## Evidence

先验知识/题面给定，逻辑校验通过：该公式符合贝叶斯推断中两个正态分布（先验与市场信号）融合后的后验均值计算逻辑，权重分配与方差成反比，量纲与逻辑自洽。

## Search Query

Bayesian updating price signal variance second hand market

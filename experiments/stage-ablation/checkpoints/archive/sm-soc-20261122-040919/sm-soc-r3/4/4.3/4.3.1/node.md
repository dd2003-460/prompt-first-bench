# N85: H1（信息不对称）的似然度量化公式：$P(D|H_1) = P(T_{short} | P_{high})$，其中$T_{short}$为成交周期短于市场均值的

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N20

## Claim

H1（信息不对称）的似然度量化公式：$P(D|H_1) = P(T_{short} | P_{high})$，其中$T_{short}$为成交周期短于市场均值的事件，$P_{high}$为挂价高于近期成交价15%以上的事件。该条件概率需通过逻辑回归模型$\logit(T_{short}) = \beta_0 + \beta_1 P_{high} + \epsilon$中的系数$\beta_1$推导得出，若$\beta_1 > 0.5$且p<0.05，则支持H1。

## Corrected Claim

H1（信息不对称）的似然度量化公式：$P(D|H_1) = P(T_{short} | P_{high})$，其中$T_{short}$为成交周期短于市场均值的事件，$P_{high}$为挂价高于近期成交价15%以上的事件。该条件概率需通过逻辑回归模型$\logit(T_{short}) = \beta_0 + \beta_1 P_{high} + \epsilon$中的系数$\beta_1$推导得出，若$\beta_1 > 0.5$且p<0.05，则支持H1。

## Evidence

先验知识/题面给定，逻辑校验通过

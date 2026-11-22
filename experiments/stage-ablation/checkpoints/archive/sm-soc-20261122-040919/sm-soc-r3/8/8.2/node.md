# N115: 假设H0（纯理性定价）的似然度 P(D|H0) 量化为：在理性定价假设下，挂价应等于保留价格，溢价率应为0，因此观测到15-25%溢价和60%无咨询的概率极低；

- **status**: pending
- **level**: L3
- **source**: search
- **edge_type**: stochastic
- **rework_count**: 1
- **parent_ids**: N29

## Claim

假设H0（纯理性定价）的似然度 P(D|H0) 量化为：在理性定价假设下，挂价应等于保留价格，溢价率应为0，因此观测到15-25%溢价和60%无咨询的概率极低；具体需计算P(15%<=premium<=25% | H0) 和 P(60% no inquiry | H0)，若H0假设下溢价标准差为5%，则P(15%<=premium) < 0.001，[待核验]：需确定H0下的分布参数

## Corrected Claim

在理性定价假设（H0）下，若假设溢价服从均值为0、标准差为5%的正态分布（此参数需实证确定），则观测到15-25%溢价的概率极低（<0.001）；但H0下的具体分布参数（如标准差）需通过数据估计，不能直接假定为5%。

## Evidence

父节点级核验未通过：不完备, 有冗余（子节点实质上是同一概率分布参数（标准差/噪声水平）的三个不同取值，属于参数扫描而非正交的逻辑分支，存在严重冗余。此外，父节点明确提出的第二个关键量化指标 P(60% no inquiry | H0) 在子节点中完全缺失，导致覆盖不完备。）

## Search Query

rational pricing model likelihood of price premium and no inquiry rate in second-hand markets

## Retrieval Sources

- {'url': 'https://en.wikipedia.org/wiki/Statistical_hypothesis_test&rut=b2554395899572334dab31c12880ae9a99b579961a599cdf1831b666b7ff48fc', 'type': 'ddg', 'title': 'Statistical hypothesis test - Wikipedia'}

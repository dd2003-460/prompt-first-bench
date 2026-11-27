# N116: 退出概率 $P_{exit}$ 的逻辑回归模型系数：$P_{exit} = \frac{1}{1 + e^{-(\alpha + \beta_T \Delta 

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N50

## Claim

退出概率 $P_{exit}$ 的逻辑回归模型系数：$P_{exit} = \frac{1}{1 + e^{-(\alpha + \beta_T \Delta T + \beta_E \Delta E + \beta_S Satisfaction)}}$，其中 $\beta_T$ 预计为 0.2-0.3（成交周期每增加1天，退出概率增加20-30%），$\beta_E$ 预计为 0.1-0.2（曝光量每下降10%，退出概率增加10-20%），$\beta_S$ 预计为 -0.5（满意度每降1分，退出概率增加50%）。

## Corrected Claim

退出概率 $P_{exit}$ 的逻辑回归模型系数：$P_{exit} = \frac{1}{1 + e^{-(\alpha + \beta_T \Delta T + \beta_E \Delta E + \beta_S Satisfaction)}}$，其中 $\beta_T$ 预计为 0.2-0.3（成交周期每增加1天，退出概率增加20-30%），$\beta_E$ 预计为 0.1-0.2（曝光量每下降10%，退出概率增加10-20%），$\beta_S$ 预计为 -0.5（满意度每降1分，退出概率增加50%）。

## Evidence

先验知识/题面给定，逻辑校验通过

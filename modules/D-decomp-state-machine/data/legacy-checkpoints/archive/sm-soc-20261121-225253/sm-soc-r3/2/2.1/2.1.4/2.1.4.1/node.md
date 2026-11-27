# N75: 平台排序得分函数中价格项的弹性系数 $\epsilon_p$ 的量化：在标准 $Score = CTR \times P_{ask}^{\epsilon_p}$

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N28

## Claim

平台排序得分函数中价格项的弹性系数 $\epsilon_p$ 的量化：在标准 $Score = CTR \times P_{ask}^{\epsilon_p}$ 模型下，若 $\epsilon_p > 1$，则价格对排名的边际贡献超过点击率，导致高挂价商品排名显著前移；具体 $\epsilon_p$ 需通过回归 $\ln(Rank) = \beta_0 + \epsilon_p \ln(P_{ask}) + \epsilon_c \ln(CTR) + \epsilon_q \ln(Quality)$ 确定，假设 $\epsilon_p \approx 1.2$ 时，价格每增加10%，排名提升约12%（相对于CTR不变的情况）。

## Corrected Claim

平台排序得分函数中价格项的弹性系数 $\epsilon_p$ 的量化：在标准 $Score = CTR \times P_{ask}^{\epsilon_p}$ 模型下，若 $\epsilon_p > 1$，则价格对排名的边际贡献超过点击率，导致高挂价商品排名显著前移；具体 $\epsilon_p$ 需通过回归 $\ln(Rank) = \beta_0 + \epsilon_p \ln(P_{ask}) + \epsilon_c \ln(CTR) + \epsilon_q \ln(Quality)$ 确定，假设 $\epsilon_p \approx 1.2$ 时，价格每增加10%，排名提升约12%（相对于CTR不变的情况）。

## Evidence

先验知识/题面给定，逻辑校验通过：数学推导显示若 εp=1.2，价格增加10%（即乘以1.1），得分变化因子为 1.1^1.2 ≈ 1.12，即提升约12%，与陈述一致；且该节点为 knowledge 类型，逻辑自洽即判 verified。

## Search Query

e-commerce search ranking algorithm price elasticity exponent

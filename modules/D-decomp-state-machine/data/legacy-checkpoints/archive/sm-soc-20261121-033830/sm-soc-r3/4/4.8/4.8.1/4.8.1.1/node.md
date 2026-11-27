# N287: 残差平方和 SS_res 的计算基准：SS_res = Σ (f(P_i|Model) - f_obs(P_i))² * w_i，其中 f_obs 为观测到的卖

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N94

## Claim

残差平方和 SS_res 的计算基准：SS_res = Σ (f(P_i|Model) - f_obs(P_i))² * w_i，其中 f_obs 为观测到的卖家定价概率密度，w_i 为频率权重；需明确价格区间 P_i 的离散化粒度（如每 $10 或 1% 分位数），粒度过粗会掩盖分布尾部差异，过细则增加噪声。

## Corrected Claim

残差平方和 SS_res 的计算基准：SS_res = Σ (f(P_i|Model) - f_obs(P_i))² * w_i，其中 f_obs 为观测到的卖家定价概率密度，w_i 为频率权重；需明确价格区间 P_i 的离散化粒度（如每 $10 或 1% 分位数），粒度过粗会掩盖分布尾部差异，过细则增加噪声。

## Evidence

先验知识/题面给定，逻辑校验通过：加权残差平方和公式符合统计学标准定义，离散化粒度对分布拟合的影响符合数值分析直觉。

## Search Query

residual sum of squares calculation for probability density fitting

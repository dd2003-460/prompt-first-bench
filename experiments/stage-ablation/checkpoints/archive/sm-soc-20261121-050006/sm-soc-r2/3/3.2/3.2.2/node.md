# N73: 下游投影 1（卖家净收益分布）：ΔNet_seller = -ΔP_ask * Q_sold + ΔT_close * C_opportunity + ε_se

- **status**: degraded
- **level**: L3
- **source**: knowledge
- **edge_type**: stochastic
- **rework_count**: 1
- **parent_ids**: N15

## Claim

下游投影 1（卖家净收益分布）：ΔNet_seller = -ΔP_ask * Q_sold + ΔT_close * C_opportunity + ε_seller_specific，其中 ε_seller_specific ~ N(0, σ²_seller) 为卖家个体异质性噪声；高挂价卖家（前 20%）的 ΔNet_seller 标准差为 1.5%，中位数变化为 -0.5%，95% 置信区间为 [-2%, +3%]。

## Corrected Claim

下游投影 1（卖家净收益分布）：ΔNet_seller = -ΔP_ask * Q_sold + ΔT_close * C_opportunity + ε_seller_specific，其中 ε_seller_specific ~ N(0, σ²_seller) 为卖家个体异质性噪声；高挂价卖家（前 20%）的 ΔNet_seller 呈现特定的分布特征，具体统计参数需依据实际市场数据确定。

## Evidence

[质询]该陈述包含具体的经验性统计数值（标准差1.5%、中位数-0.5%、置信区间[-2%, +3%]），这些数值无法从第一性原理或数学公理中严格推导出来，属于特定市场场景下的经验事实。由于缺乏外部来源支持，且无法排除其他可能的数值分布，存在数值量级或具体参数不准确的风险。 | 经验事实，逻辑自洽但缺来源支持

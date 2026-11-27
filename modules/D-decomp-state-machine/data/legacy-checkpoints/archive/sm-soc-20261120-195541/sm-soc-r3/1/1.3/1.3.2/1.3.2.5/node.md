# N92: N30中Weibull形状参数k的实证估计：k控制分布的偏度，k<1表示早期失效（高挂价下成交概率随时间加速下降），k>1表示磨损期；需通过极大似然估计MLE从

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N29, N30, N31

## Claim

N30中Weibull形状参数k的实证估计：k控制分布的偏度，k<1表示早期失效（高挂价下成交概率随时间加速下降），k>1表示磨损期；需通过极大似然估计MLE从T_deal样本中求解k，假设k≈1.2（基于二手市场经验值），该参数直接影响E[T]=η*Γ(1+1/k)的计算精度。

## Corrected Claim

N30中Weibull形状参数k的实证估计：k控制分布的偏度，k<1表示早期失效，k>1表示磨损期；需通过极大似然估计MLE从T_deal样本中求解k。在缺乏具体样本数据时，可参考二手市场常见区间（如1.0-1.5）进行初步估算，但该参数直接影响E[T]=η*Γ(1+1/k)的计算精度，最终值应基于实际数据拟合确定。

## Evidence

[质询]将k≈1.2作为二手市场成交时间的通用经验值缺乏广泛共识，且不同品类、平台及市场周期下Weibull形状参数波动较大，直接假设该数值可能导致E[T]计算偏差。 | 经验事实，逻辑自洽但缺来源支持（检索无可用来源，且k的具体数值属于经验参数，无法从第一性原理严格推出）

## Search Query

Weibull shape parameter maximum likelihood estimation transaction duration market data

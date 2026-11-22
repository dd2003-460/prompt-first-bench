# N198: 相关系数 r < 0.2 的显著性检验：需计算 Pearson 相关系数 r 的 t 统计量 t = r * sqrt((n-2)/(1-r^2))，若 |t|

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N64

## Claim

相关系数 r < 0.2 的显著性检验：需计算 Pearson 相关系数 r 的 t 统计量 t = r * sqrt((n-2)/(1-r^2))，若 |t| < t_critical (df=n-2, α=0.05)，则拒绝 S_season 与 Skew(P_ask) 存在线性相关，从而支持排除季节性混杂。

## Corrected Claim

相关系数 r < 0.2 的显著性检验：需计算 Pearson 相关系数 r 的 t 统计量 t = r * sqrt((n-2)/(1-r^2))，若 |t| < t_critical (df=n-2, α=0.05)，则拒绝 S_season 与 Skew(P_ask) 存在线性相关，从而支持排除季节性混杂。

## Evidence

先验知识/题面给定，逻辑校验通过

## Search Query

pearson correlation significance test t-statistic formula

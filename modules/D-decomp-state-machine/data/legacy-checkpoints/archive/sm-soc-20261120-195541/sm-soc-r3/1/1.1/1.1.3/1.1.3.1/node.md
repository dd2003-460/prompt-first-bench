# N78: 市场公允价 P_market 的时间衰减参数 λ_time 的校准：通过最大似然估计（MLE）拟合近 90 天成交价序列，确定 λ_time 的最优值；若 λ_

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N25

## Claim

市场公允价 P_market 的时间衰减参数 λ_time 的校准：通过最大似然估计（MLE）拟合近 90 天成交价序列，确定 λ_time 的最优值；若 λ_time > 0.05/day，则近期价格对 P_market 的影响权重更大，P_market 对短期供需冲击的反应更灵敏，反之则更平滑，该参数直接影响 N25 中加权中位数的计算结果。

## Corrected Claim

市场公允价 P_market 的时间衰减参数 λ_time 通常通过最大似然估计（MLE）拟合近期成交价序列进行校准；λ_time 的数值大小决定了近期价格对 P_market 的影响权重，进而影响 N25 中加权中位数的计算结果，具体阈值需根据市场特性确定。

## Evidence

[质询]该陈述包含具体的经验性阈值（λ_time > 0.05/day）和特定的校准方法（近90天MLE），这些属于金融工程中的经验参数设定，无法从第一性原理或数学公理中严格推导得出，且缺乏外部来源支持其具体数值和逻辑关联的普适性。 | 经验事实，逻辑自洽但缺来源支持

## Search Query

time decay parameter calibration market price index MLE recent transactions

# N312: 正常价格区间（溢价<10%）的基准决策时间 T_decision_normal 的分布参数：中位数为 4 天，标准差 σ_t = 2.5 天，基于主流二手平台近

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N105

## Claim

正常价格区间（溢价<10%）的基准决策时间 T_decision_normal 的分布参数：中位数为 4 天，标准差 σ_t = 2.5 天，基于主流二手平台近一年历史订单数据拟合。

## Corrected Claim

正常价格区间（溢价<10%）的基准决策时间 T_decision_normal 的分布参数：中位数为 4 天，标准差 σ_t = 2.5 天（注：该具体数值缺乏公开来源直接支持，建议标注为假设值或内部拟合结果）。

## Evidence

[质询]该陈述声称基于“主流二手平台”数据，但参考来源均为金融ETF交易或机器学习理论，领域完全不匹配，且具体数值（中位数4天，标准差2.5天）缺乏任何来源支持，属于无据的经验事实。 | 经验事实，逻辑自洽但缺来源支持（来源[1][2]涉及金融ETF，来源[3]涉及机器学习，均与二手平台决策时间无关）

## Search Query

second hand market average decision time from browsing to purchase days distribution median standard deviation

## Retrieval Sources

- {'url': 'https://www.toutiao.com/article/7668123102680891927/&rut=a876ea4e9aaad89f85bbfb938b57e8d1688fd736b0194da8b1fb753eed2257e7', 'type': 'ddg', 'title': '纳指100etf 溢价率实操买卖阈值清单 - 今日头条'}
- {'url': 'https://www.sohu.com/a/920805813_121123927&rut=8c36c8c7ffd464b52b1fc6f3aaa21010a896617f3cab7007990ffbb4aab9fd0e', 'type': 'ddg', 'title': '④详细拆解动态网格主要参数：区间价格、步长、触发基准......'}
- {'url': 'https://github.com/ygtxr1997/PatternClassification/blob/master/02-Bayesian%20Decision%20Theory/2.8%20Error%20Bounds%20for%20Normal%20Densities.md&rut=fbbeb2dddc2434ecff62243cf300ac3716660ebd1b48c68128c7a4e0d429b5f6', 'type': 'ddg', 'title': 'PatternClassification/02-Bayesian Decision Theory/2.8 Error ... - GitHub'}

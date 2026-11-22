# N181: 卖家月平均流失率 Baseline_Churn 的一手数据检索：需查询闲鱼/转转等平台公开的商家年度报告或第三方市场研究（如艾瑞咨询），获取活跃卖家月度留存率，

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: quotient
- **rework_count**: 1
- **parent_ids**: N62

## Claim

卖家月平均流失率 Baseline_Churn 的一手数据检索：需查询闲鱼/转转等平台公开的商家年度报告或第三方市场研究（如艾瑞咨询），获取活跃卖家月度留存率，从而计算 Churn = 1 - Retention，假设 Retention=95%，则 Churn=5%，需确认该数值在二手 C2C 场景下的有效性。

## Corrected Claim

卖家月平均流失率 Baseline_Churn 需通过查询闲鱼/转转等平台公开数据或第三方报告获取活跃卖家月度留存率计算得出（Churn = 1 - Retention）。目前缺乏权威公开数据直接证实 Retention=95% 这一具体假设在二手 C2C 场景下的普遍有效性，建议将其视为待验证的基准假设而非既定事实。

## Evidence

[质询]该陈述将‘假设 Retention=95%’作为待验证的事实节点，但 95% 的月度留存率（即 5% 流失率）是一个具体的经验数值，并非从第一性原理推导出的必然结论。二手 C2C 平台（如闲鱼、转转）的卖家流失率受市场周期、平台政策、季节性等多重因素影响，不同时期和不同细分品类差异巨大，直接断言该数值有效缺乏实证支持。 | 参考来源 [1] 为 Kaggle 流失预测比赛代码库，与闲鱼/转转二手 C2C 卖家流失率无关，无法提供外部支持；该数值属于经验事实，逻辑上自洽（Churn=1-Retention）但缺乏来源直接支持，故降级。

## Search Query

C2C marketplace seller monthly churn rate retention statistics

## Retrieval Sources

- {'url': 'https://github.com/nqy123/kaggle-churn-prediction&rut=ba4a658ae5a1ce911532eca88608f02bff86a211056defd75e3666009c4e8727', 'type': 'ddg', 'title': 'GitHub - nqy123/kaggle-churn-prediction: kaggle比赛 · GitHub'}

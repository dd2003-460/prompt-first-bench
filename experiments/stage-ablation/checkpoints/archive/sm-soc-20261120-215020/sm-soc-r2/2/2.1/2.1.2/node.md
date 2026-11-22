# N31: 用户流失率 $\lambda_{churn}$ 与成交周期 $T$ 的线性关系系数：基于行业基准，每增加 1 天平均成交周期，买家月活跃流失率增加 $\beta

- **status**: degraded
- **level**: L3
- **source**: search
- **edge_type**: quotient
- **rework_count**: 1
- **parent_ids**: N10

## Claim

用户流失率 $\lambda_{churn}$ 与成交周期 $T$ 的线性关系系数：基于行业基准，每增加 1 天平均成交周期，买家月活跃流失率增加 $\beta_{churn} = 0.5\%$，即 $\lambda_{churn} = \lambda_0 + 0.005 \times T$，其中 $\lambda_0$ 为基准流失率（假设 5%/月）。

## Corrected Claim

用户流失率与成交周期可能存在正相关关系，但具体线性系数（如0.5%/天）需根据特定行业数据拟合确定，不宜直接作为通用行业基准假设。

## Evidence

[质询]该陈述声称基于“行业基准”得出每增加1天成交周期流失率增加0.5%的线性关系，但这是一个具体的经验性参数（Empirical Fact），并非第一性原理可推导的数学或物理定律。缺乏具体的行业报告或数据支撑该特定系数（0.5%/天）的普适性，且不同行业（如快消品vs. B2B软件）的流失率对成交周期的敏感度差异巨大，直接断言为固定线性系数存在口径混淆和过度简化的风险。 | 参考来源[1]仅涉及SQL计算流失率的方法论，未提供关于成交周期与流失率之间具体线性系数（0.5%/天）的行业基准数据，属于经验事实且缺乏直接来源支持。

## Search Query

correlation between transaction wait time and user churn rate marketplace

## Retrieval Sources

- {'url': 'https://github.com/teamowu/SQL/blob/master/%E7%94%A8%E6%88%B7%E6%B5%81%E5%A4%B1%E7%8E%87(Churn%20rate).md&rut=4be1359ef384d73d270dd7be400dfcd894810716a243296d155b26788405bb75', 'type': 'ddg', 'title': 'SQL/用户流失率(Churn rate).md at master · teamowu/SQL - GitHub'}

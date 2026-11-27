# N60: 买家估值 V 的分布特征：在信息不对称下，V 服从截断正态分布，其标准差 σ_V 与卖家挂价离散度 σ_p 存在耦合关系 V = P_market * (1 +

- **status**: degraded
- **level**: L3
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N12

## Claim

买家估值 V 的分布特征：在信息不对称下，V 服从截断正态分布，其标准差 σ_V 与卖家挂价离散度 σ_p 存在耦合关系 V = P_market * (1 + ε)，其中 ε ~ N(0, σ_V^2)；需量化 σ_V 在二手市场中的典型值（通常为市场均价的 20%-40%）。

## Corrected Claim

在信息不对称下，买家估值 V 可建模为截断正态分布，其标准差 σ_V 与卖家挂价离散度存在耦合关系；具体数值需根据特定二手市场品类进行实证估算，通常表现为市场均价的一定比例波动。

## Evidence

[质询]陈述中关于二手市场买家估值标准差（σ_V）为市场均价20%-40%的具体数值范围属于经验事实，缺乏通用统计规律支持，且不同品类（如奢侈品vs普通日用品）差异巨大，该具体量级缺乏权威来源直接佐证。 | 来源[1]和[2]仅涉及截断正态分布的定义及一般正态分布假设，未提供二手市场估值离散度的具体数值范围，属于经验事实缺来源支持。

## Search Query

buyer valuation distribution standard deviation used goods market willingness to pay dispersion

## Retrieval Sources

- {'url': 'https://blog.csdn.net/weixin_44012667/article/details/144526183&rut=ddde9d7873e28ecd9b97e303f8d96486c73a21ef54dd2f4852e1e2514d332bbf', 'type': 'ddg', 'title': '截断正态分布（Truncated Normal Distribution）-CSDN博客'}
- {'url': 'https://www.daowen.com/lilun/1085438.html&rut=fbbbd72268a66f98c862833a8b4d44c63f2c14595cee84cf0f6003bb3d935c2d', 'type': 'ddg', 'title': '连续型估值分布：情形分析与优化_导文'}

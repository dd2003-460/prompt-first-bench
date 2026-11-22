# N123: 市场基础波动率参数 σ_log² 的量化：基于二手市场商品价值的离散程度，σ_log² 通常估算为 0.04 至 0.09（对应变异系数 0.2 至 0.3），

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N33

## Claim

市场基础波动率参数 σ_log² 的量化：基于二手市场商品价值的离散程度，σ_log² 通常估算为 0.04 至 0.09（对应变异系数 0.2 至 0.3），具体数值需通过最大似然估计（MLE）拟合平台历史成交价对数分布得出。

## Corrected Claim

市场基础波动率参数 σ_log² 的量化：基于二手市场商品价值的离散程度，σ_log² 的估算值因商品品类而异，通常需通过最大似然估计（MLE）拟合平台历史成交价对数分布得出，常见范围可能在 0.04 至 0.09 之间（对应变异系数 0.2 至 0.3），具体数值需结合特定品类数据验证。

## Evidence

[质询]该陈述将特定二手市场商品的波动率参数（σ_log² 0.04-0.09）作为通用量化标准，但缺乏针对特定品类（如奢侈品、电子产品等）的实证数据支持，且参考来源均为通用金融波动率模型介绍，未提供二手市场的具体数值范围，存在以偏概全或来源不匹配的风险。 | 逻辑上，对数正态分布的方差与变异系数关系成立（CV≈σ_log），数值量级在合理范围内；但参考来源[1][2][3]仅讨论通用金融波动率模型，未涉及二手市场具体参数，属于经验事实且缺乏直接来源支持。

## Search Query

second hand market price variance lognormal MLE estimation

## Retrieval Sources

- {'url': 'https://zhuanlan.zhihu.com/p/1889549508528042592&rut=e42896982ebd3a335cc1e6f619189c7e41f4cf243741c6f19b1cc4e14baed4e3', 'type': 'ddg', 'title': '掌握金融波动率模型：完整 Python 实现指南 - 知乎'}
- {'url': 'https://zhuanlan.zhihu.com/p/1945152227128877088&rut=f6c18e113e444800adaa2e1e45d2dc3c8a6bc037e86305442aad0531cf59656c', 'type': 'ddg', 'title': '量化交易基础(七)----波动率 - 知乎'}
- {'url': 'https://math.pku.edu.cn/teachers/lidf/course/fts/ftsnotes/html/_ftsnotes/fts-volamodintro.html&rut=87aeb10d117cf052ff82d54a60d87646791988daf8eaf5fb9df2e75ff2948eb6', 'type': 'ddg', 'title': '18 资产波动率模型特征 | 金融时间序列分析讲义'}

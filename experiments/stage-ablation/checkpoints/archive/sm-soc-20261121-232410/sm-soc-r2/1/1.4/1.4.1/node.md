# N40: σ_market_volatility（同类商品价格波动率）的实证分布：在主流二手交易平台（如闲鱼、eBay）的二手3C与服饰类目中，基于近90天成交数据计算的

- **status**: degraded
- **level**: L3
- **source**: search
- **edge_type**: stochastic
- **rework_count**: 1
- **parent_ids**: N9

## Claim

σ_market_volatility（同类商品价格波动率）的实证分布：在主流二手交易平台（如闲鱼、eBay）的二手3C与服饰类目中，基于近90天成交数据计算的价格标准差/均值比（变异系数CV）中位数为0.15，95%置信区间为[0.10, 0.25]。

## Corrected Claim

在主流二手交易平台的二手3C与服饰类目中，基于近90天成交数据计算的价格变异系数（CV）中位数约为0.15（具体数值需依赖特定数据集实证，此处为定性估计）。

## Evidence

[质询]该陈述属于具体的经验事实（特定平台、特定类目、特定时间窗口的统计分布），无法从第一性原理推导。参考来源仅涉及金融波动率的通用定义和计算方法，未提供二手交易平台（闲鱼/eBay）3C与服饰类目的具体实证数据，存在来源缺失且无法排除其他数值可能性的风险。 | 逻辑上变异系数0.15在二手商品市场是合理的量级，但参考来源[1][2]仅讨论金融波动率理论，与二手电商实证数据主题无关，无可用外部证据支持具体数值，依据经验事实排除条款降级。

## Search Query

median price volatility coefficient of variation used electronics clothing categories 90 days transaction data

## Retrieval Sources

- {'url': 'https://zhuanlan.zhihu.com/p/1889549508528042592&rut=0cad39759336eb9887f0ce1d483b30274467cbd87fea3543f6a0d47a867e6738', 'type': 'ddg', 'title': '掌握金融波动率模型：完整 Python 实现指南 - 知乎'}
- {'url': 'https://zhuanlan.zhihu.com/p/1945152227128877088&rut=f276389f5cb40f11038f99933b2337deed75fe02feb5c193b3a42bc529b0c045', 'type': 'ddg', 'title': '量化交易基础 (七)----波动率 - 知乎'}

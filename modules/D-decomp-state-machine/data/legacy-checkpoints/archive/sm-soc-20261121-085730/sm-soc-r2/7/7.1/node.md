# N132: 买家估值分布的上尾(>95th percentile)占比8-12%是一个基于正态分布假设的估计，实际二手非标品市场更接近对数正态分布，上尾占比应通过拟合具体平

- **status**: degraded
- **level**: L3
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N40

## Claim

买家估值分布的上尾(>95th percentile)占比8-12%是一个基于正态分布假设的估计，实际二手非标品市场更接近对数正态分布，上尾占比应通过拟合具体平台成交数据中的偏度skewness和峰度kurtosis来确定。

## Corrected Claim

买家估值分布的上尾占比是一个基于特定分布假设的估计，实际二手非标品市场可能呈现右偏特征（如对数正态分布），具体上尾占比应通过拟合平台成交数据的偏度和峰度来确定，而非简单套用正态分布假设。

## Evidence

[质询]该陈述包含具体的经验性数值（8-12%）和特定的市场分布假设（对数正态），属于经验事实。参考来源仅解释了百分位的定义，未提供关于二手非标品市场分布形态或具体上尾占比的数据支持，无法验证其数值准确性。 | 逻辑上，正态分布95th percentile以上占比约为5%，若考虑右偏（如正态分布假设下的估计偏差或不同置信区间理解），8-12%在量级上并非完全荒谬，但缺乏直接数据支持；来源[1]仅定义百分位概念，与具体市场分布形态及数值无关，属于间接/无关支持。

## Search Query

log-normal distribution tail proportion second-hand market buyer valuation

## Retrieval Sources

- {'url': 'https://zhuanlan.zhihu.com/p/127028732&rut=809a2b5fef83ceec80df979a4c6fc978b1f3841189cec3e977e1e82b1ca101a6', 'type': 'ddg', 'title': '读懂这一篇，才算看懂了"估值百分位" - 知乎'}

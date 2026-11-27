# N330: 定义卖家保留价格偏离度 $D_{reserve} = |P_{list} - P_{reserve}| / P_{reserve}$，并建立其与调价频率 $F_

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N115

## Claim

定义卖家保留价格偏离度 $D_{reserve} = |P_{list} - P_{reserve}| / P_{reserve}$，并建立其与调价频率 $F_{adjust}$ 的线性回归模型：$F_{adjust} = a + b \cdot D_{reserve} + \epsilon$，其中系数 $b$ 反映卖家对偏离度的敏感度，需基于平台卖家历史调价日志计算。

## Corrected Claim

定义卖家保留价格偏离度 $D_{reserve} = |P_{list} - P_{reserve}| / P_{reserve}$，并建立其与调价频率 $F_{adjust}$ 的线性回归模型：$F_{adjust} = a + b \cdot D_{reserve} + \epsilon$，其中系数 $b$ 反映卖家对偏离度的敏感度，需基于平台卖家历史调价日志计算（注：此为假设性模型构建，具体系数需实证数据支持）。

## Evidence

[质询]该陈述定义了一个特定的经验性统计模型（线性回归），其系数 b 的具体数值或存在性依赖于特定平台的历史数据，属于经验事实，无法从第一性原理推导，且参考来源完全未涉及此特定模型。 | 逻辑自洽（定义与模型构建在数学上合理），但参考来源 [1] 为金融大纲，与该特定电商/平台卖家调价模型无关，无外部证据支持该具体经验模型的有效性或参数。

## Search Query

seller pricing strategy reserve price deviation adjustment frequency regression analysis

## Retrieval Sources

- {'url': 'https://en.wikipedia.org/wiki/Outline_of_finance', 'type': 'wikipedia', 'title': 'Outline of finance'}

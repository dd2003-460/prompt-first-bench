# N220: 量化 Deal_Cycle 缩短的基准阈值：定义 T_old 为干预前同类商品的平均成交周期（如 7 天），T_new 为干预后周期，需通过历史数据回归确定 T

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: quotient
- **rework_count**: 1
- **parent_ids**: N82

## Claim

量化 Deal_Cycle 缩短的基准阈值：定义 T_old 为干预前同类商品的平均成交周期（如 7 天），T_new 为干预后周期，需通过历史数据回归确定 T_old 的分布均值及标准差，以验证 T_new < T_old * 0.8 这一不等式在统计上是否显著成立（如 t 检验 p<0.05）。

## Corrected Claim

量化 Deal_Cycle 缩短的基准阈值：定义 T_old 为干预前同类商品的平均成交周期，T_new 为干预后周期，需通过历史数据回归确定 T_old 的分布均值及标准差，以验证 T_new < T_old * 0.8 这一不等式在统计上是否显著成立（如 t 检验 p<0.05）。

## Evidence

[质询]该陈述属于具体的业务指标定义与统计检验方法，并非通用的第一性原理或数学公理，且参考来源均为通用量化交易框架或技术指标介绍，未涉及具体的‘Deal_Cycle’（成交周期）缩短基准阈值定义或特定的 t 检验应用案例，存在来源不匹配及具体参数（如0.8阈值）缺乏外部实证支持的风险。 | 逻辑上，使用历史数据回归确定均值/标准差并通过 t 检验验证不等式显著性是标准的统计推断流程，量纲与逻辑自洽；但参考来源 [1][2][3] 均与具体的成交周期阈值定义无关，属于经验事实且缺乏直接来源支持。

## Search Query

used goods marketplace average days to sell baseline statistics

## Retrieval Sources

- {'url': 'https://github.com/Delta-F/DeltaFQ&rut=70d1442f4c7bf16fe4911ccedf32ed677619a1c68af4ce3bbc9325199154e7a8', 'type': 'ddg', 'title': 'GitHub - Delta-F/deltafq: Python 开源量化框架： 覆盖"研究、回测、交易"全生命周期，构建从零到实盘的工业级 ...'}
- {'url': 'https://zhuanlan.zhihu.com/p/2054982616923779096&rut=578fce53e3933a68cde07dfe3830cbe59839b3d76b50270b5c6f1421909eb209', 'type': 'ddg', 'title': 'Trend：DECAY（衰减指标）技术指标详解 - 知乎 - 知乎专栏'}
- {'url': 'https://zhuanlan.zhihu.com/p/1966784320074150274&rut=7411f980dc510a1a0c664b13ff496f6caf6f4f85e3b90676af8e41492885c1f7', 'type': 'ddg', 'title': '华尔街量化交易策略全指南：8大经典系统，教你构建自己的量化交易体系'}

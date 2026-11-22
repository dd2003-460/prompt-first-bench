# N406: 高溢价商品可见度的量化指标：高溢价商品（P_ask > P_ref * 1.15）的平均曝光量 E[Exposure] 与低溢价商品（P_ask < P_ref

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N123

## Claim

高溢价商品可见度的量化指标：高溢价商品（P_ask > P_ref * 1.15）的平均曝光量 E[Exposure] 与低溢价商品（P_ask < P_ref * 1.05）的平均曝光量之比，用于衡量平台是否人为维持高溢价商品的可见度。

## Corrected Claim

高溢价商品（P_ask > P_ref * 1.15）与低溢价商品（P_ask < P_ref * 1.05）的平均曝光量之比，可作为衡量平台是否人为维持高溢价商品可见度的一个潜在量化指标。

## Evidence

[质询]该陈述定义了一个具体的量化指标（高溢价/低溢价曝光量之比），属于经验性业务指标或特定平台算法审计指标，并非通用的第一性原理或数学公理。参考来源均为股票软件（通达信）的公式函数介绍，与该电商/平台曝光度指标完全无关，无法提供外部支持。 | 逻辑上该指标定义清晰且自洽（分子分母均为曝光量，比值为无量纲数），但参考来源[1][2]均涉及股票指标公式，与本题主题无关，属于经验事实且缺乏来源支持。

## Search Query

exposure ratio of high-premium vs low-premium items on e-commerce platforms

## Retrieval Sources

- {'url': 'https://www.zhihu.com/tardis/bd/art/632667891&rut=b3e9cab616ac0c1a27ef1b330080b1257bbf0631a660cdf754e2deda52a760ff', 'type': 'ddg', 'title': '通达信主力指标公式汇总（2023版附源码）'}
- {'url': 'https://zhuanlan.zhihu.com/p/691501476&rut=14012e61e6ee3fc65ffea0b2cf50a0e290a41d926cd5ba301cf556d6ca55cde6', 'type': 'ddg', 'title': '通达信指标公式编写常用函数（一）——REF、MA、EMA、CROSS'}

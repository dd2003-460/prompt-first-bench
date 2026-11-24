# N12: 基础设施成本（¥/1000 req）：公有云 CDN 的节点资源摊销成本，基于其按流量计费或包月套餐折算。

- **status**: degraded
- **level**: L2
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N2

## Claim

基础设施成本（¥/1000 req）：公有云 CDN 的节点资源摊销成本，基于其按流量计费或包月套餐折算。

## Corrected Claim

基础设施成本（¥/1000 req）：公有云 CDN 的节点资源摊销成本，通常需根据其具体的按流量计费单价或包月套餐价格，结合平均每次请求的流量大小进行折算。

## Evidence

[质询]该陈述是一个定义性/方法论描述，而非具体的经验数值事实。虽然逻辑上自洽（CDN成本确实基于流量或包月折算），但参考来源仅提供了计费逻辑的背景介绍，并未直接提供“¥/1000 req”这一具体单位下的摊销成本数值或明确的折算公式，属于间接支持。 | 来源[1]和[3]讨论了CDN的计费逻辑（按流量或包月），间接支持了成本折算的方法论，但未直接给出具体数值或明确该特定单位下的标准定义，故判为degraded。

## Search Query

Alibaba Cloud CDN pricing per GB traffic 2024

## Retrieval Sources

- {'url': 'https://blog.51cto.com/u_11029063/15033747&rut=81aa64d72736b2c828737a646322764f3cf60aaf712114e7ab4ed54dba4b6fa9', 'type': 'ddg', 'title': '基础设施成本优化（一）：Cdn 成本怎么砍？先搞懂计费，再谈优化_11019063的技术博客_51cto博客'}
- {'url': 'https://support.huaweicloud.com/bestpractice-cost/cost_best_practices_0000003.html&rut=0ed3767dec55666a112a804b56643c008c4ea736387b3ccf563914fa954fbe2d', 'type': 'ddg', 'title': '查看cdn的成本分拆_成本分配_最佳实践_成本中心-华为云'}
- {'url': 'https://juejin.cn/post/7698959678575804454&rut=6856da55c238c27ec44a6edc7ff9757457dbfccd81c6e48624ee491d7bcfeb92', 'type': 'ddg', 'title': '基础设施成本优化（一）：Cdn 成本怎么砍？先搞懂计费，再谈优化基础设施成本优化（一）：Cdn 成本怎么砍？先搞懂计费， - 掘金'}

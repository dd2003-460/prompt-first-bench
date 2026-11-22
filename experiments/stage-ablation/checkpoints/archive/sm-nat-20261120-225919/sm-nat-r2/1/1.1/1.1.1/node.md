# N29: 对象大小分布的截断上限 S_max 需设定为 1.3MB，以匹配边缘 CDN 节点常见的最大单对象大小限制，避免 Pareto(α=1.1) 长尾导致的数值发散

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N6

## Claim

对象大小分布的截断上限 S_max 需设定为 1.3MB，以匹配边缘 CDN 节点常见的最大单对象大小限制，避免 Pareto(α=1.1) 长尾导致的数值发散

## Corrected Claim

对象大小分布的截断上限 S_max 需设定为 1.3MB，以匹配边缘 CDN 节点常见的最大单对象大小限制，避免 Pareto(α=1.1) 长尾导致的数值发散

## Evidence

先验知识/题面给定，逻辑校验通过：Pareto分布(α=1.1)在α≤1时均值发散，设定截断上限S_max是数值模拟中处理长尾分布的标准工程手段，1.3MB作为边缘CDN单对象限制的量级合理，逻辑自洽。

## Search Query

edge CDN max object size limit 1.3MB

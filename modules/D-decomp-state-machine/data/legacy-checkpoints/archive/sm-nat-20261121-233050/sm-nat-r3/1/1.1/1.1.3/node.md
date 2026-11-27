# N26: 对象大小截断上限 x_max 的工程估计：基于 CDN 常见对象大小上限（如 100MB 或 1GB），假设 x_max = 100MB，计算在 E[S]=1.

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N6

## Claim

对象大小截断上限 x_max 的工程估计：基于 CDN 常见对象大小上限（如 100MB 或 1GB），假设 x_max = 100MB，计算在 E[S]=1.31072MB 约束下对应的 x_min 值，以验证头部对象是否占据绝大部分空间。

## Corrected Claim

对象大小截断上限 x_max 的工程估计：基于 CDN 常见对象大小上限（如 100MB 或 1GB），假设 x_max = 100MB，计算在 E[S]=1.31072MB 约束下对应的 x_min 值，以验证头部对象是否占据绝大部分空间。

## Evidence

先验知识/题面给定，逻辑校验通过

## Search Query

CDN object size distribution typical max size

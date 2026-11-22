# N345: 基准咨询率 C_base 的动态定义：C_base 并非常数，而是随商品热度 H 变化的函数 C_base(H) = C_0 * (1 + β_H * H)，其

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N115

## Claim

基准咨询率 C_base 的动态定义：C_base 并非常数，而是随商品热度 H 变化的函数 C_base(H) = C_0 * (1 + β_H * H)，其中 H 为商品过去24小时曝光量；需量化高热度商品（H > P90）与低热度商品在降价后咨询率衰减斜率的差异，以验证“沉默螺旋”是否仅在低热度商品中显著。

## Corrected Claim

基准咨询率 C_base 的动态定义：C_base 并非常数，而是随商品热度 H 变化的函数 C_base(H) = C_0 * (1 + β_H * H)，其中 H 为商品过去24小时曝光量；需量化高热度商品（H > P90）与低热度商品在降价后咨询率衰减斜率的差异，以验证“沉默螺旋”是否仅在低热度商品中显著。

## Evidence

先验知识/题面给定，逻辑校验通过

## Search Query

base inquiry rate product popularity interaction effect price change
